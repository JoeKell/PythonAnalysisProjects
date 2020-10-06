#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import re

#The file the code reads from
ParagraphIndex=3
File = open(os.path.join("PyParagraph", "Resources", f"paragraph_{ParagraphIndex}.txt"),"r")
Paragraph=File.read().replace("\n"," ").replace("  "," ")

#Splitting the paragraph into sentences
Sentences=re.split("(?<=[.!?]) +", Paragraph)

#Derermining values of ApproxWCount, ApproxSCount, and AvSLen
ApproxSCount=len(Sentences)
AvSLen=0
Words=[]
for Sentence in Sentences:
    AvSLen+=len(Sentence.split(" "))
    Words+=Sentence.split(" ")
AvSLen=round(AvSLen/ApproxSCount,1)
ApproxWCount=len(Words)

#This is to make average word length more accurate. Removing special chars with translate
CharacterLibrary=[]
for i in range(33,48):
    CharacterLibrary.append(chr(i))
for i in range(58,65):
    CharacterLibrary.append(chr(i))
for i in range(91,97):
    CharacterLibrary.append(chr(i))
for i in range(123,127):
    CharacterLibrary.append(chr(i))
print(CharacterLibrary)
#for Word in Words:




#Printing with the desired format
print("Paragraph Analysis\n----------------------")
print(f"Approximate Word Count: {ApproxWCount}")
print(f"Approximate Sentence Count: {ApproxSCount}")
print(f"Average Letter Count: ")
print(f"Average Sentence Length: {AvSLen}")

#print("\n",Words)
