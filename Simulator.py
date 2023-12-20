from BdiAgent import*
from enum import Enum
import time
from textblob import TextBlob
from MessageTree import createTree, getNextResponse
from UserModelling import updateUserModel,updateTypingSpeed,updateTrollProbability


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
        return "["+self.sender+"]: "+self.text+" (polarity: "+str(self.polarity)+\
        return "["+self.sender.value+"]: "+self.text+" (polarity: "+str(self.polarity)+\
         ", angryness: "+str(self.angry)+', scaredness: '+str(self.scared)+\
         ", troll_score: "+str(self.troll)+")"

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
    def add_message(self,message):
        i=self.log.index(message)
        typing_speed=TextBlob(message.text).word_counts/self.log[i - 1].time - message.time
        if message.sender not in self.user_inf.keys():
            self.user_inf[message.sender]={'message_number':1,'avg_speed':typing_speed}
        else:
            old_avg=self.user_inf[message.sender]['avg_speed']
            n=self.user_inf[message.sender]['message_number']
            self.user_inf[message.sender]['avg_speed']=(n*old_avg+typing_speed)/(n+1)
            self.user_inf[message.sender]['message_number']+=1
    def get_avg_typing_speed(self,sender):
        return self.user_inf[sender]['avg_speed']




class SupportHelpLineAgent(BdiAgent):
    def belief_revision(self,conversation):
<<<<<<< HEAD
        message=conversation[-1]
        avg_typing_speed=conversation.get_avg_typing_speed(message.sender)
=======
        ontology = self.beliefs
        updateTypingSpeed(conversation, ontology)
        updateUserModel(conversation[-1], ontology)
        updateTrollProbability(conversation, ontology)
        # avg_rp=0
        # avg_speed=0
        # i=1
        # n=0
        # for i in range(len(conversation)):
        #     if conversation[i].sender == Actor.SupportSeeker:
        #         for j in range(i-1,-1):
        #             if conversation[j].sender != Actor.SupportSeeker:
        #                 new_rp=conversation[j].time-conversation[i].time
        #                 avg_rp=((n-1)*avg_rp+new_rp)/n
        #                 n+=1
        #                 i=j
        # self.beliefs=percept
>>>>>>> pr/1

    def plan(self):
        self.plan_buffer.append('Dialoge action: '+self.beliefs)

    def execute(self):
        action=super(SupportHelpLineAgent, self).execute()
        print(action)

class Chatbot:
    def __init__(self):
        self._chatbotTree = createTree()
        self._chatbotActive = True
    
    def print_next_message(self, userMessage):
        return getNextResponse(self,userMessage)

support_help_line=SupportHelpLineAgent(beliefs=None,intentions=None,mode=BdiMode.singleMinded)

conversation=[Message(sender=Actor.chatbot.value,text='simulation started',time=time.time())]
conversation=[Message(sender=Actor.chatbot,text='simulation started',time=time.time())]

print(conversation[-1],"\n")

chatbot = Chatbot()

while True:
    message=input()
    # conversation.append()
    conversation.append(Message(sender=Actor.SupportSeeker.value, text=message,time=time.time()))
    conversation.append(Message(sender=Actor.SupportSeeker, text=message,time=time.time()))
    # print(conversation[-1],"\n")
    support_help_line.update(conversation)
    print()
    if chatbot._chatbotActive:
        conversation.append(Message(sender=Actor.chatbot.value,text=chatbot.print_next_message(message),time=time.time()))
        conversation.append(Message(sender=Actor.chatbot,text=chatbot.print_next_message(message),time=time.time()))
        print("\033[94m"+conversation[-1].text,"\033[0m\n") # The strange number are here to change the text color in the terminal
    # reply=support_help_line.update(conversation)
