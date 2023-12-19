# from textblob import TextBlob
# from better_profanity import profanity
# dirty_text = "fuck you?"
# dirty_text_blob = TextBlob(dirty_text)
# dirty_text_blob=dirty_text_blob.correct()
# print(dirty_text_blob.sentiment)
# if profanity.contains_profanity(dirty_text):
#     print("has swear word")

# from owlready2 import *
# owlready2.JAVA_EXE = "C:\\Program Files (x86)\\Java\\jre-1.8\\bin\\java.exe"
# onto = get_ontology("ChildSupportHelplineOntology.owx")
# onto.load()
# responseTime=onto.ResponseTime("responseTime")
# responseTime.hasTime=[10]
# responseTime.isShortResponseTime=[True]
# temp=onto.get_instances_of(onto.ResponseTime)
# with onto:
#  sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
#  onto.save("buffer.owx")
# buffer_onto = get_ontology("buffer.owx")
# temp1=buffer_onto.get_instances_of(buffer_onto.ResponseTime)
# for instance in temp1:
#  print(instance.isShortResponseTime)

temp=[1,2,3]
head=temp.pop()
pass



