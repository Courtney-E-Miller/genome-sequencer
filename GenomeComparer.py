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

def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]


def compare(firstFile, secondFile):
    count = 0
    sequence1 = sequenceMaker(firstFile)
    sequence2 = sequenceMaker(secondFile)
    differenes = returnNotMatches(sequence1, sequence2)
    print(differences)
        
        


compare("clipOfAcythosiphonDNA.txt", "clipOfAdinetaDNA.txt")
