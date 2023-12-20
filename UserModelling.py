from owlready2 import *


def __init__():
    """ Initialize conversation, both user model"""
    onto = get_ontology("file://ChildSupportHelplineOntology.owx").load()

    rt = onto.ResponseTime("rt1")
    rt.hasTime.append(15)
    rt.isShortResponseTime.append(False)

    with onto:
        sync_reasoner_pellet(infer_property_values=True)

    print(rt.hasTime)
    print(rt.isShortResponseTime)


__init__()

def sentimentAnalysis():
    """compute emotions from the message and returns the emotions of the user"""

def update():
    """ update user model with information from message and sentiment analysis"""