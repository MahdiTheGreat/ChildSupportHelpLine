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
    openingTree.addChild(openingTree.root,"Eating Disorder")#0
    openingTree.addChild(openingTree.root,"Suicide")#1
    openingTree.addChild(openingTree.root,"Sexual Abuse")#2
    openingTree.addChild(openingTree.root,"Depression")#3

    openingTree.addChild(openingTree.root.children[1],"I'm sorry to hear that. You should never feel like that. Is there anything I can do for you ?")#0
    openingTree.addChild(openingTree.root.children[3],"I am sad to hear this is happening to you, have you tried talking to someone about this ? Or do you wnat to tell me more about what you are experiencing ?")#0
