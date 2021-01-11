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
        textData = re.sub(r"(\b{}\b)".format(
            word), r"\1\\glo{}", textData, flags=re.IGNORECASE)

    m = re.findall("(startTable(.|\n)*?endTable)", textData)
    if m:
        for table in m:
            found = table[0]
            newtext = found
            for word in glossaryList:
                newtext = re.sub(r"(\b{}\b)(\\glo{{}})".format(
                    word), r"\1\\noexpand\2", newtext, flags=re.IGNORECASE)
            textData = textData.replace(found, newtext)

    m = re.findall("(url{(.|\n)*?})", textData)
    if m:
        for link in m:
            found = link[0]
            newtext = found
            newtext = re.sub(r"(\\glo{})", "", newtext)
            textData = textData.replace(found, newtext)

    text.seek(0)
    text.truncate()
    text.write(textData)
    text.close()
