from BdiAgent import*
from enum import Enum
import time
from textblob import TextBlob

class Message:
    def __init__(self,sender,text,time,polarity=0.0,angry=0.0,scared=0.0,troll=0.0):
        self.sender = sender
        self.text = text
        self.time = time
        self.polarity = polarity
        self.angry = angry
        self.scared =scared
        self.troll=troll
    def __str__(self):
        return "["+self.sender+"]: "+self.text+"(polarity: "+str(self.polarity)+\
         ", angryness: "+str(self.angry)+', scaredness: '+str(self.scared)+\
         ", troll_score: "+str(self.troll)

class Actor(Enum):
    SupportSeeker='SupportSeeker'
    chatbot='chatbot'
    SupportAdmin='SupportAdmin'

class Conversation:
    def __init__(self):
        self.log=[]
        self.user_inf={}
        self.user_message_number={}
        self.user_response_number={}
    def __getitem__(self, item):
        return self.log[item]
    def __get_message_speed(self,message):
        i=self.log.index(message)
        return self.log[i-1].time-message.time
    def add_message(self,message):
        if message.sender not in self.user_inf.keys():
            self.user_inf[message.sender]={'message_number':1,'avg_speed':
                                               TextBlob(message.text).word_counts/self.__get_message_speed(message),
                                           }
class SupportHelpLineAgent(BdiAgent):
    def belief_revision(self,conversation):
        pass

    def plan(self):
        self.plan_buffer.append('Dialouge action: '+self.beliefs)

    def execute(self):
        action=super(SupportHelpLineAgent, self).execute()
        print(action)

support_help_line=SupportHelpLineAgent(beliefs=None,intentions=None,mode=BdiMode.singleMinded)

conversation=[Message(sender=Actor.chatbot,text='simulation started',time=time.time())]

print(conversation[-1])

while True:
    message=input()
    conversation.append(conversation.append(Message(sender=Actor.SupportSeeker, text='message',
                                                    time=time.time())))
    print(conversation[-1])
    reply=support_help_line.update(conversation)

