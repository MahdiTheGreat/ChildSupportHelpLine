from owlready2 import *
from transformers import pipeline
from random import random
from better_profanity import profanity


def sentimentAnalysis(message):
    """ Compute polarity from the message """
    # sentiment_pipeline = pipeline("sentiment-analysis")
    # data = [message]
    # result = sentiment_pipeline(data)[0]['label']
    result= "NEGATIVE" if random()>0.5 else "POSITIVE"
    return result


messageNb = 0


def updateUserModel(message, ontology):
    """ Updates message instance by adding informations on sentiment analysis """
    global messageNb
    messageName = "message_" + str(messageNb)
    messageInd = ontology.Message(messageName)
    messageVocab=ontology.Vocabulary(messageName+'vocab')
    messageInd.hasVocabulary=messageVocab
    message.sender.hasMessage = messageInd

    if sentimentAnalysis(message.text) == "NEGATIVE":
        message.polarity = -1
        messageInd.hasSadTone=True
    else:
        message.polarity = 1
        messageInd.hasSadTone = False

    if profanity.contains_profanity(message.text):
        messageVocab.hasSwearWords=True
    else:
        messageVocab.hasSwearWords = False
    with ontology:
        sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)
    message.angry = messageInd.hasAngryTone
    messageNb +=1

def updateTrollProbability(conversation, ontology):
    """ Computes the new probability for the user to be a troll """
    """Some temporal analysis can be done here"""
    positive_message_threshold=0.7
    angry_message_threshold=0.7
    positive_messages=0
    angry_messages=0
    for message in conversation:
        if message.polarity==1:positive_messages+=1
        if message.angry==True:angry_messages+=1
    positive_message_percent=positive_messages/len(conversation)
    angry_message_percent = angry_messages / len(conversation)
    typing_speed=ontology.get_instances_of(ontology.TypingSpeed)[0]
    pass
    if positive_message_percent>positive_message_threshold or angry_message_percent>angry_message_threshold\
        or typing_speed.isSlow==False:
        return True
    else:return False


def updateTypingSpeed(conversation, ontology):
    """ Update the typing speed of the user model"""
    """ Update the typing speed of the user model"""
    user = conversation[-1].sender
    supportSeekerNbMessages = len(list(filter(lambda message: message.sender == user, conversation)))
    dt = conversation[-1].time - conversation[-2].time
    messageSize = len(conversation[-1].text)
    typing_speed = messageSize / dt

    currentAvg = ontology.TypingSpeed.instances()[0].hasSpeed

    if currentAvg == None:
        ontology.TypingSpeed.instances()[0].hasSpeed = typing_speed
    else:
        updatedAvg = (currentAvg * (supportSeekerNbMessages - 1) + typing_speed) / supportSeekerNbMessages
        ontology.TypingSpeed.instances()[0].hasSpeed = updatedAvg




