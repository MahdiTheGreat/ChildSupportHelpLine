from BdiAgent import*
from enum import Enum
import time
from textblob import TextBlob
from MessageTree import createTree, getNextResponse
from UserModelling import updateUserModel,updateTypingSpeed,updateTrollProbability
from owlready2 import *

class Actor(Enum):
    SupportSeeker='supportSeeker'
    chatbot='chatbot'
    SupportAdmin='supportAdmin'

onto = get_ontology("ChildSupportHelplineOntology.rdf")
onto.load()
# with onto:
#  sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
emotion=onto.Emotion("emotion")
message=onto.Message("message")
punc=onto.Punctuation('punctuation')
typingSpeed=onto.TypingSpeed('typingSpeed')
supportSeeker=onto.SupportSeeker(Actor.SupportSeeker.value)
userProfile=onto.UserProfile('userProfile')
vocab=onto.Vocabulary('vocab')
crisis=onto.Crisis('crisis')

class Message:
    def __init__(self,sender,text,time,polarity=False,angry=0.0,scared=0.0,troll=0.0):
        self.sender = sender
        self.text = text
        self.time = time
        self.polarity = polarity
        self.angry = angry
        self.scared =scared
        self.troll=troll
    def __str__(self):
        message="["+self.sender.value+"]: "+self.text
        if self.sender==Actor.SupportSeeker:
            message+=" (polarity: "+str(self.polarity)+\
         ", angryness: "+str(self.angry)+', scaredness: '+str(self.scared)+\
         ", troll_score: "+str(self.troll)+")"
        return message

class SupportHelpLineAgent(BdiAgent):
    def __init__(self,beliefs,intentions,mode):
        super(SupportHelpLineAgent, self).__init__(beliefs=beliefs, intentions=intentions, mode=mode)
        self.chatbot=Chatbot()
        self.current_message=''
        pass

    def belief_revision(self,conversation):
        # message=conversation[-1]
        # avg_typing_speed=conversation.get_avg_typing_speed(message.sender)
        ontology = self.beliefs
        updateTypingSpeed(conversation, ontology)
        self.current_message=conversation[-1]
        updateUserModel(conversation[-1], ontology)
        updateTrollProbability(conversation, ontology)

    def plan(self):
        dialouge_action=self.chatbot.print_next_message(self.current_message)
        self.plan_buffer.append(dialouge_action)


class Chatbot:
    def __init__(self):
        self._chatbotTree = createTree()
        self._chatbotActive = True
    
    def print_next_message(self, userMessage):
        return getNextResponse(self,userMessage)

support_help_line=SupportHelpLineAgent(beliefs=onto,intentions=None,mode=BdiMode.singleMinded)

conversation=[Message(sender=Actor.chatbot,text="\033[94m Hello! You are in the queue and will talk to a human as soon as possible. In the meantime we can chat a little if you want ! What is the reason of your call? Please select one from Suicide, Depression, Eating Disorder and Sexual Abuse.\033[0m\n",time=time.time())]

print(conversation[-1],"\n")

chatbot = Chatbot()

while True:
    message=input()
    conversation.append(Message(sender=Actor.SupportSeeker, text=message,time=time.time()))
    print(conversation[-1])
    reply=support_help_line.update(conversation)
    conversation.append(Message(sender=Actor.chatbot,text=reply,time=time.time()))
    print(conversation[-1])

    #if chatbot._chatbotActive:
    #    conversation.append(Message(sender=Actor.chatbot,text=chatbot.print_next_message(message),time=time.time()))
    #    print("\033[94m"+conversation[-1].text,"\033[0m\n") # The strange number are here to change the text color in the terminal

