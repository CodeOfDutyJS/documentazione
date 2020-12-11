import sys
import os

textPath = os.getcwd() + sys.argv[1]
gloPath= sys.argv[2]
fileList=[]
for root, dir, files in os.walk(textPath):
    for file in files:
        if file.endswith(".tex"):
            fileList.append(os.path.join(root,file))

for f in fileList:
    try:
        text = open( f , "r+")
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
        textData = textData.replace(word + ")", wordReplacement + ")")
        #textData = textData.replace("{" + word + "}", "{" + wordReplacement + "}")
        #textData = textData.replace("{" + word, "{" + wordReplacement)
        #textData = textData.replace(word + "}", wordReplacement + "}")
        textData = textData.replace(word + "\n", wordReplacement + "\n")

    text.seek(0)
    text.truncate()
    text.write(textData)
    text.close()

