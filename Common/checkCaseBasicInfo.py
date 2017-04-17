#!/usr/bin/python

import os
import re
import sys
parentDir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.insert(0,parentDir)
from Common import readCaseFile as rf

#the file will get the case execution details from TGF and draw them in to a table.
#the latest tgjob id will be selected and checking from which it is triggered.
class CheckCaseDetail(object):
    def __init__(self,totalCaseNo,pool):
#    def __init__(self,caseDict,totalCaseNo):
#        self.readFileIns = rf.ReadFile()
#        self.suiteExecutionDetail = {}
#        self.caseDict = self.readFileIns.readFileAndGetCaseDict(os.getcwd()+os.sep+"caseFile.txt")
#        self.caseDict = caseDict
        self.totalCaseNo = totalCaseNo
        self.pool = pool
    
        self.suiteExecutionDetail = {}

    def getCasePassNoAndActuralExecuteCaseNo(self,suiteName,caseName):
        casePassNoCmd = "tgr suite "+ suiteName + " "+str(self.totalCaseNo)+" v "+self.pool+" | grep \'"+ caseName[:11]+"\' | awk '{print $5}' | grep ok | grep -v nok | wc -l" 
        caseActuralExecuteNoCmd = "tgr suite "+ suiteName + " "+str(self.totalCaseNo)+" v "+self.pool+" | grep \'" + caseName[:11]+ "\' | wc -l "
        print "casePassNoCmd : ",casePassNoCmd
        print "caseActuralExecuteNoCmd : ",caseActuralExecuteNoCmd
        caseActuralExecuteNo = os.popen(caseActuralExecuteNoCmd).readlines()[0].strip()
        casePassNo = os.popen(casePassNoCmd).readlines()[0].strip() 
        return caseActuralExecuteNo,casePassNo

    def getPassRate(self,acturalExecuteNo,passNo):
        print "actual : %s | passNo : %s"%(acturalExecuteNo,passNo)
        if '0' == acturalExecuteNo or '0' == passNo:
            print "divide 0000000000"
            return 0
        return round(float(passNo)/float(acturalExecuteNo),2)*100  

    def getCaseTriggerLoop(self,suiteName,caseName): 
        caseNBCVCmd = "tgr suite "+ suiteName + " "+str(self.totalCaseNo)+" v "+self.pool+" | egrep \'"+suiteName[:-4] + "|" + caseName[:11] + "\' | tail -2 | head -1 | awk '{print $1}'"
        suiteJobId = os.popen(caseNBCVCmd).readlines()[0].strip()
        NBCVResult = os.popen("tgr "+ suiteJobId + " | grep jenkins" ).readlines()
        if 0 == len(NBCVResult):
            #print "[ INFO ] : CASE :[ %s ], The latest job was not triggered from jenkins."%(case)
            NBCVResult = 'Manual Case'
        else :
            NBCVResult = re.findall("job\/(.*?)\/.*",NBCVResult[0])[0] 
        return NBCVResult

    def getExecutedUPNo(self):
        pass
    
    def printStatistics(self,caseData,checkPoint):
        defaultSpaceIndents = ' |%18s '
        numberOfData = len(checkPoint)
        if 0 == numberOfData:
            print "no data to print, exit."
            return 
        title = defaultSpaceIndents * numberOfData+"|"
        print "-"*((int(defaultSpaceIndents[-4:-2])+3)*numberOfData)
        print title%checkPoint
        for suite in caseData.keys():
            for case in caseData[suite]:
                 data = tuple(case.values()[0])
                 print title%data
        print "-"*((int(defaultSpaceIndents[-4:-2])+3)*numberOfData)
if __name__ == "__main__":
    readFileIns = rf.ReadFile()
    caseDict = readFileIns.readFileAndGetCaseDict("/home/efuguxu/tools/PUMATools/NBVToNBCCaseCheck"+os.sep+"caseFile.txt")
    print "caseDict : ",caseDict
    #print "Checking Case from TGF, Please wait..."
    caseDetail = CheckCaseDetail(caseDict,100,"")
    caseDetail.checkCase()
    #caseDetail.printStatisticsInFormat()
