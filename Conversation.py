from MessageTree import createTree, getNextResponse

class Conversation:

    def __init__(self) -> None:
        self._chatbotTree = createTree() # Save all the tree for the chatbot answers
        self._chatbot = True # Indicates if the chatbot is able to continue the conversation or not
        self._convHistory = None # Saves all messages that have been sent for now
        self.supportSeekerModel = None # Stores the user Model

    # Don't know where to call the getNextResponse function, here or in the BDI Agent ?