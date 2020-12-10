import sys

textPath=sys.argv[1]
gloPath=sys.argv[2]

try:
    text = open(textPath, "r")
except:
    print("failed to open text file")
try:
    glossary = open(gloPath, "r")
except:
    print("failed to open glossary file")

glossaryList=glossary.read().splitlines()
glossary.close()
textData=text.read()
text.close()

for word in glossaryList:
    wordReplacement= word + "\glo{}"
    textData = textData.replace(word + " ",wordReplacement+ " ")
    textData = textData.replace(word+ ",",wordReplacement+",")
    textData = textData.replace(word + ".", wordReplacement+".")
    textData = textData.replace(word + ":", wordReplacement + ":")

try:
    text=open(textPath,"wt")
except:
    print("failed to open in write")

text.write(textData)




