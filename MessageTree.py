class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def addRoot(self, val):
        self.root = TreeNode(val)

    def addChild(self, parent_node, val):
        child_node = TreeNode(val)
        parent_node.children.append(child_node)

    def cutTree(self, node):
        new_tree = Tree()
        new_tree.root = node
        return new_tree
    
def createTree():
    openingTree = Tree()

    openingTree.addRoot("Start")#root
    openingTree.addChild(openingTree.root,"Suicide")#0
    openingTree.addChild(openingTree.root,"Depression")#1
    openingTree.addChild(openingTree.root,"Eating Disorder")#2
    openingTree.addChild(openingTree.root,"Sexual Abuse")#3

    # Suicide Tree
    openingTree.addChild(openingTree.root.children[0],"I'm sorry to hear that. You should never have to feel like that. Is there anything I can do for you ?")
    openingTree.addChild(openingTree.root.children[0].children[0],"not,be here,unworthy,alone,forgotten,never,change,better")
    openingTree.addChild(openingTree.root.children[0].children[0].children[0],"I feel that it is good that you talk about this and are brave enough to open up about haw you feel. We all feel like that at some point in our life, and it always helps to talk to someone instaed of taking drastic measures.")
    
    # Depression Tree
    openingTree.addChild(openingTree.root.children[1],"I'm sorry to hear that. Might I know what caused you feeling this way ?")

    openingTree.addChild(openingTree.root.children[1].children[0],"alone,ignored,bullying,bully,hit,afraid,hurt") # Bullying subtree
    openingTree.addChild(openingTree.root.children[1].children[0].children[0],"I am sad to hear that this is happening to you, have you tried talking to someone about this? Or do you want to tell me more about what you are experiencing?")
    openingTree.addChild(openingTree.root.children[1].children[0].children[0].children[0],"no,listen,no one,alone,helpless,change,same,often")
    openingTree.addChild(openingTree.root.children[1].children[0].children[0].children[0].children[0],"It is awful that you experience that no one is listening to you, and it is not ok to be treated like that. If you have tried talking to someone and nothing has happened, maybe try reaching out again to someone else for help. In the meantime, I will be happy to help you the best I can !")
    openingTree.addChild(openingTree.root.children[1].children[0].children[0].children[0],"Yes,tell,talk,happened,experiencing")
    openingTree.addChild(openingTree.root.children[1].children[0].children[0].children[0].children[1],"What you are experiencing is awful and not okay at all. If you haven't tried talking to someone maybe try reaching out to someone you trust for help.")
                     
    openingTree.addChild(openingTree.root.children[1].children[0],"alone,left out,depressed,no one,forgotten,lonely,ignored") #Alone sub tree
    openingTree.addChild(openingTree.root.children[1].children[0].children[1],"Sometimes it is hard and you feel like you are alone, but you should know that you aren't ! I am here for you and so are the people around you that you trust.")
    openingTree.addChild(openingTree.root.children[1].children[0].children[1].children[0],"No,change,same,help,alone")
    openingTree.addChild(openingTree.root.children[1].children[0].children[1].children[0].children[0],"I understand that it can feel like no one understands and that it is hard when there is no change. You can feel alone, even if you have people around you, and that is okay. If you want to feel a bi better try to create a goal, for example, say 'Hi!' to a stranger once a day, or try to do something where you meet someone once a week or even once a month so you don't feel as lonely as you do now.")
                         
    # Eating Disorder Tree
    openingTree.addChild(openingTree.root.children[2],"I can understand that it is both hard and scary, but you are not alone. A lot of people suffer from problems with food. Do you know what caused it?")
    openingTree.addChild(openingTree.root.children[2].children[0],"no,I don't know")
    openingTree.addChild(openingTree.root.children[2].children[0].children[0],"Let us see if we can figure something out.")
    openingTree.addChild(openingTree.root.children[2].children[0],"yes,gain,weigth,fit in,not")
    openingTree.addChild(openingTree.root.children[2].children[0].children[1],"You should never feel that you have to change to fit into someone else standard. I know that it is hard to not care about others or be afraid to be different, but causing yourself harm is never a sustainable and good option.")

    # Sexual Abuse Tree
    openingTree.addChild(openingTree.root.children[3],"That's so sad to hear. No one should have to go through that. Do you want to talk about it or do you want to know other ways you can use to move forward ?")
    openingTree.addChild(openingTree.root.children[3].children[0],"yes,talk,tell,like,too,happened")
    openingTree.addChild(openingTree.root.children[3].children[0].children[0],"That is awful. I can definitely see why it has been a traumatic experience for you. Is there anything you want me to do for you to help you move forward ?")
    openingTree.addChild(openingTree.root.children[3].children[0],"no,forward,heal,overcome,past,move")
    openingTree.addChild(openingTree.root.children[3].children[0].children[1],"To move forward from something like this I would recommend...")

    return openingTree      


def get_message_score(word_list, message):
    """ Checks how many of the words are in the actual message"""
    w_count = 0
    parsed_word_list = word_list.lower().split(',')
    parsed_message = message.lower()
    for word in parsed_word_list:
        if word in parsed_message:
            w_count += 1
    return w_count

def getNextResponse(chatbot, message):
    """ Checks wich answer is the best fit """
    tree = chatbot._chatbotTree
    max_score = 0
    max_i = -1
    for i in range(len(tree.root.children)):
        score = get_message_score(tree.root.children[i].val, message)
        if score > max_score:
            max_score = score
            max_i = i
    if max_i != -1:
        best_response = tree.root.children[max_i].children[0]
        chatbot._chatbotTree = tree.cutTree(best_response)
    else:
        best_response = "Sadly, as I am a chatbot, I am not able to help you to your full extent, but you are in a queue to talk to one of my human colleagues. If you just want to talk while you wait I am here for you and will be listening to what you have to say."
        chatbot._chatbotActive = False
        return best_response

    return best_response.val