import sys
import os

textPath = os.getcwd() + sys.argv[1]
gloPath= sys.argv[2]
fileList=[]
tmp = os.listdir(textPath)
for word in tmp:
    if word.endswith(".tex"):
        fileList.append(word)

for f in fileList:
    try:
        text = open(textPath + f , "r+")
    except:
        print("failed to open text file")
    try:
        glossary = open(gloPath, "r")
    except:
        print("failed to open glossary file")
    glossaryList=glossary.read().splitlines()
    glossary.close()
    textData=text.read()

    for word in glossaryList:
        wordReplacement= word + "\glo{}"
        textData = textData.replace(word + " ",wordReplacement+ " ")
        textData = textData.replace(word+ ",",wordReplacement+",")
        textData = textData.replace(word + ".", wordReplacement+".")
        textData = textData.replace(word + ":", wordReplacement + ":")
        textData = textData.replace(word + "(", wordReplacement + "(")

    text.seek(0)
    text.truncate()
    text.write(textData)
    text.close()

