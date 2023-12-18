from enum import Enum
class BdiMode(Enum):
 blind=0
 singleMinded=1
 openMinded=2

class BdiAgent():
    def __init__(self,beliefs,intentions,mode=BdiMode.blind):
        self.beliefs=beliefs
        self.intentions=intentions
        self.plan_buffer=[]
        self.mode=mode
    def belief_revision(self,percept):
        pass
    def options(self):
        """Based on beliefs and intentions"""
        pass
    def succeeded(self):
        """Based on beliefs and intentions"""
        pass
    def filter(self,desires):
        """Based on beliefs, intentions and desires"""
    def plan(self):
        """Based on beliefs and intentions"""
    def exectue(self,action):
        """Based on actions"""
    def update(self,percept):
        self.belief_revision(percept)
        desires=self.options()
        intentions=self.intentions
        if not self.plan_buffer: self.plan_buffer=self.plan()
        if self.mode==BdiMode.blind:
            self.exectue(self.plan_buffer)
        else:
            a=self.plan_buffer.pop()
            self.exectue(a)






