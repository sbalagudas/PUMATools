#!/usr/bin/python

import os

class ReadFile(object):
#    def __init__(self,fileName):
#        self.caseFile = fileName
#        if not os.path.isfile(self.caseFile):
#            print "ERROR, No such a file : ",self.caseFile

    def readFileAndGetCaseDict(self,fileName):
        self.caseFile = fileName
        if not os.path.isfile(self.caseFile):
            print "ERROR, No such a file : ",self.caseFile
            return 

        caseDict = {}
        caseList = []
        with open(self.caseFile) as caseFile:
            for line in caseFile.readlines():
                #remove the spaces to make the match more accuracy.
                line = line.strip()
                if '\n' not in line and "#" not in line:
                    if line.endswith("xml"):
                        if not caseList:
                            suiteName = line
                            continue
                        else :
                            caseDict[suiteName] = caseList
                            suiteName = line
                            caseList = []
                    if line.startswith("LTE"):
                        caseList.append(line)
                else :
                    continue
            if 0 != len(caseList):
                caseDict[suiteName] = caseList
        #print "caseDict : ",caseDict
        return caseDict

    def readCaseFolder(self,folderPath):
        caseFolderResult = []
        if not os.path.exists(folderPath):
            print "ERROR : the folder : [ %s ] does not exist."%(folderPath) 
            return
        for eachFile in os.listdir(folderPath):
            fileBaseDir = folderPath+os.sep+eachFile
            if os.path.isfile(fileBaseDir):
                print "read file : ",fileBaseDir
                caseResultInOneFile = self.readFileAndGetCaseDict(fileBaseDir)
                caseFolderResult.append(caseResultInOneFile)
                print "result :",caseResultInOneFile
                print "------------------------------------------------"
        return caseFolderResult

if __name__ == "__main__":
    defaultFile = "/home/fabio/share/PUMATools/NBVToNBCCaseCheck/caseFile.txt"
    path = "/home/fabio/share/soakPerf"
    rf = ReadFile()
    #result = rf.readFileAndGetCaseDict(defaultFile)
    result = rf.readCaseFolder(path)
    print "result : ",result
