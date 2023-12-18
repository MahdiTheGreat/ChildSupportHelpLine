# from textblob import TextBlob
# from better_profanity import profanity
# dirty_text = "Go kill yourself you fucking whore!"
# dirty_text_blob = TextBlob(dirty_text)
# dirty_text_blob=dirty_text_blob.correct()
# print(dirty_text_blob.sentiment)
# if profanity.contains_profanity(dirty_text):
#     print("has swear word")

from owlready2 import *
onto_path.append("")
onto = get_ontology("ChildSupportHelplineOntology.owx")
onto.load()
onto.