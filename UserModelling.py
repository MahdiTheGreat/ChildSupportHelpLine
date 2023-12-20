from owlready2 import *
from transformers import pipeline

def sentimentAnalysis(message):
    """ Compute polarity from the message """ 

    sentiment_pipeline = pipeline("sentiment-analysis")
    data = [message]
    result = sentiment_pipeline(data)[0]['label']
    return result


messageNb = 0
def updateUserModel(message, ontology):
    """ Updates message instance by adding informations on sentiment analysis """
    
    if sentimentAnalysis(message.text) == "NEGATIVE":
        message.polarity = -1
    else:
        message.polarity = 1
    
    messageName = "message_"+messageNb
    messageInd = ontology.Message(messageName)
    message.sender.hasMessage = messageInd

    with ontology:
        sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

    message.angry = messageInd.hasAngryTone
    message.scared = messageInd.hasScaredTone

    messageNb +=1

def updateTrollProbability(conversation, ontology):
    """ Computes the new probability of the"""
    pass

def updateTypingSpeed(conversation, ontology):
    """ Update the typing speed of the user model"""
    user = conversation[-1].sender
    supportSeekerNbMessages = len(list(filter(lambda message: message.sender == user, conversation)))
    dt = conversation[-1].time - conversation[-2].time
    messageSize = len(conversation[-1].text)

    typing_speed = messageSize/dt

    currentAvg = ontology.TypingSpeed[0].hasSpeed

    updatedAvg = (currentAvg * (supportSeekerNbMessages-1) + typing_speed) / supportSeekerNbMessages
    ontology.TypingSpeed[0].hasSpeed = updatedAvg


