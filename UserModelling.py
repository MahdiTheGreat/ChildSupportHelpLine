from owlready2 import *
from transformers import pipeline

onto = get_ontology("file://ChildSupportHelplineOntology.owl").load()

def __init__():
    """ Initialize conversation and both user model"""

    rt = onto.ResponseTime()
    rt.hasTime =[15]
    # rt.isShortResponseTime.append(False)

    with onto:
        sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

    print(rt.hasTime)
    print(rt.isShortResponseTime)


def sentimentAnalysis(message):
    """compute emotions from the message and returns the emotions of the user""" 

    sentiment_pipeline = pipeline("sentiment-analysis")
    data = [message]
    result = sentiment_pipeline(data)[0]['label']
    return result


sentimentAnalysis("I hate life")

messageNb = 0

def update(message):
    """ update user model with information from message and sentiment analysis"""
    
    if sentimentAnalysis(message.text) == "NEGATIVE":
        message.polarity = -1
    else:
        message.polarity = 1
    
    messageName = "message_"+messageNb
    
    responseTimeInd = onto.ResponseTime("rtmessage_"+messageNb)
    responseTimeInd.hasTime = message.time

    messageLengthInd = onto.TextLength("messagelen_"+messageNb)
    messageLengthInd.hasLength = len(message.text)

    messageInd = onto.Conversation(messageName)
    messageInd.hasResponseTime = responseTimeInd
    messageInd.hasTextLength = messageLengthInd

    message.sender.hasConversation = messageInd

    with onto:
        sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

    messageNb +=1