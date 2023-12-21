# from textblob import TextBlob
# from better_profanity import profanity
# dirty_text = "I want to kill myself."
# dirty_text_blob = TextBlob(dirty_text)
# dirty_text_blob=dirty_text_blob.correct()
# print(dirty_text_blob.sentiment)
# if profanity.contains_profanity(dirty_text):
#     print("has swear word")

from owlready2 import *
owlready2.JAVA_EXE = "C:\\Program Files (x86)\\Java\\jre-1.8\\bin\\java.exe"
onto = get_ontology("ChildSupportHelplineOntology.rdf")
onto.load()
typingSpeed=onto.TypingSpeed("typingSpeed")
typingSpeed.hasSpeed=1.0
temp=onto.get_instances_of(onto.TypingSpeed)
with onto:
 sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True,debug=2).explain()


 #onto.save("buffer.owl")
# buffer_onto = get_ontology("buffer.owl")
# buffer_onto.load()

temp1=onto.get_instances_of(onto.TypingSpeed)
for instance in temp1:
 print(instance.hasSpeed)
 print(instance.isSlow)



