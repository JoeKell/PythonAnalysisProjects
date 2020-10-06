#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import re

ParagraphIndex=3

#The file the code reads from
File = open(os.path.join("PyParagraph", "Resources", f"paragraph_{ParagraphIndex}.txt"),"r")
Paragraph=File.read().replace("\n"," ").replace("  "," ")
Sentences=re.split("(?<=[.!?]) +", Paragraph)
ApproxSCount=len(Sentences)
AvSLen=0
Words=[]
for Sentence in Sentences:
    AvSLen+=len(Sentence.split(" "))
    Words+=Sentence.split(" ")
AvSLen=round(AvSLen/ApproxSCount,1)
print(Words)


#Printing with the desired format
print("Paragraph Analysis\n----------------------")
print(f"Approximate Word Count: ")
print(f"Approximate Sentence Count: {ApproxSCount}")
print(f"Average Letter Count: ")
print(f"Average Sentence Length: {AvSLen}")
