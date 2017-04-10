#!/usr/bin/python

import os

class ReadFile(object):
    def __init__(self):
        self.caseFile = os.getcwd()+os.sep+'caseFile.txt'
        if not os.path.isfile(self.caseFile):
            print "ERROR, No such a file : ",self.caseFile

    def readFileAndGetCaseDict(self):
        caseDict = {}
        caseList = []
        with open(self.caseFile) as caseFile:
            for line in caseFile.readlines():
                #remove the spaces to make the match more accuracy.
                line = line.strip()
                if '\n' not in line and "#" not in line:
                    if line.endswith("xml") and not caseList:
                        suiteName = line
                    #when the file reach EOF, it returns a empty string.
                    if (line.endswith("xml") and caseList) or line == '' :
                        caseDict[suiteName] = caseList
                        suiteName = line
                        caseList = []
                    if line.startswith("LTE"):
                        caseList.append(line)
                else :
                    continue
        #print "caseDict : ",caseDict
        return caseDict

if __name__ == "__main__":
    rf = ReadFile()
    result = rf.readFileAndGetCaseDict()

