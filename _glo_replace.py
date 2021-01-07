import sys
import os
import re

textPath = os.getcwd() + sys.argv[1]
gloPath = sys.argv[2]
fileList = []
for root, dir, files in os.walk(textPath):
    for file in files:
        if file.endswith(".tex"):
            fileList.append(os.path.join(root, file))

for f in fileList:
    try:
        text = open(f, "r+")
    except:
        print("failed to open text file")
    try:
        glossary = open(gloPath, "r")
    except:
        print("failed to open glossary file")
    glossaryList = glossary.read().splitlines()
    glossary.close()
    textData = text.read()

    for word in glossaryList:
        wordReplacement = word + "\glo{}"
        textData = textData.replace(word + " ", wordReplacement + " ")
        textData = textData.replace(word + ",", wordReplacement+",")
        textData = textData.replace(word + ".", wordReplacement+".")
        textData = textData.replace(word + ":", wordReplacement + ":")
        textData = textData.replace(word + "(", wordReplacement + "(")
        textData = textData.replace(word + ")", wordReplacement + ")")
        textData = textData.replace(word + "}", wordReplacement + "}")
        textData = textData.replace(word + "\n", wordReplacement + "\n")
        textData = textData.replace(word + ";", wordReplacement + ";")
        textData = textData.replace(word + "\"", wordReplacement + "\"")

    m = re.search("(startTable(.|\n)*?endTable)", textData)
    if m:
        print(m.group(1))
        if m.group(1):
            found = m.group(1)
            newtext = found
            for word in glossaryList:
                wordReplacement = word + "\\noexpand\glo{}"
                newtext = newtext.replace(
                    word + "\glo{} ", wordReplacement + " ")
                newtext = newtext.replace(
                    word + "\glo{},", wordReplacement+",")
                newtext = newtext.replace(
                    word + "\glo{}.", wordReplacement+".")
                newtext = newtext.replace(
                    word + "\glo{}:", wordReplacement + ":")
                newtext = newtext.replace(
                    word + "\glo{}(", wordReplacement + "(")
                newtext = newtext.replace(
                    word + "\glo{})", wordReplacement + ")")
                newtext = newtext.replace(
                    word + "\glo{}}", wordReplacement + "}")
                newtext = newtext.replace(
                    word + "\glo{}\n", wordReplacement + "\n")
                newtext = newtext.replace(
                    word + "\glo{};", wordReplacement + ";")
                newtext = newtext.replace(
                    word + "\glo{}\"", wordReplacement + "\"")
            textData = textData.replace(found, newtext)

    text.seek(0)
    text.truncate()
    text.write(textData)
    text.close()
