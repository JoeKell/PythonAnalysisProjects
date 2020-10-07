#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os
import re

#The file the code reads from. Choose a Paragraph Index between 1 and 3 to determine which is used.
ParagraphIndex=1
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

#This removes any spectial characters when determining the average length of a word.
AvWLen=0
for i in range(len(Words)):
    Words[i]=''.join(letter for letter in Words[i] if letter.isalnum())
    AvWLen+=len(Words[i])
AvWLen=round(AvWLen/ApproxWCount,1)

#Printing with the desired format
print("\nParagraph Analysis\n----------------------")
print(f"Approximate Word Count: {ApproxWCount}")
print(f"Approximate Sentence Count: {ApproxSCount}")
print(f"Average Letter Count: {AvWLen}")
print(f"Average Sentence Length: {AvSLen}")
