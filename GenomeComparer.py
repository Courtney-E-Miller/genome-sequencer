import io
import string


def sequenceMaker(fileName):
    firstLine = True
    genomeSpecies = []
    file = io.open(fileName, mode="r", encoding="utf-8")
    for line in file:
        if firstLine == True:
            firstLine = False
            continue
        if firstLine == False:
            for char in line:
                if char == "N":
                    line = line.replace(char, "")
            genomeSpecies.extend(line)                                              
    return genomeSpecies


def compare(firstFile, secondFile):
    count = 0
    sequence1 = sequenceMaker(firstFile)
    sequence2 = sequenceMaker(secondFile)
    for [i] in sequence1:
        if sequence1[i] != sequence2[i]:
            count = count + 1
    return count
        
        



compare("clipOfAcythosiphonDNA.txt", "clipOfAdinetaDNA.txt")
