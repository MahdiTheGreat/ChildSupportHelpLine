from owlready2 import *


def __init__():
    onto = get_ontology("file://ChildSupportHelplineOntology.owx").load()

    for classes in list(onto.classes()):
        print(classes) 

    support_seeker = onto.User("support_seeker")
    volunteer = onto.User("volunteer")

    conversation = onto.Conversation("conversation")

    