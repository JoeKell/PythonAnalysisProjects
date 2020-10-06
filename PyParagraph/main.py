#All code designed to be run from the PythonAnalysisProjects folder. If you have file path issues, look there.
import os

ParagraphIndex=1

#The file the code reads from
File = open(os.path.join("PyParagraph", "Resources", f"paragraph_{ParagraphIndex}.txt"),"r")
Paragraph=File.read().replace("\n"," ").replace("  "," ")
print(Paragraph)