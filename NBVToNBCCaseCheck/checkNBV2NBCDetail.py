#!/usr/bin/python

import sys
import os
parentDir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.insert(0,parentDir)
from Common import readCaseFile as rf
from Common import checkCaseBasicInfo as cb

class CheckNBV2NBCCaseDetail(object):
    def __init__(self):
        self.caseFile = os.getcwd()+os.sep+"caseFile.txt"
        readFileIns = rf.ReadFile()
        self.caseDict = readFileIns.readFileAndGetCaseDict(self.caseFile)
        print "self.caseDict",self.caseDict
        self.suiteExecutionDetail = {}
        self.basicInfoIns = cb.CheckCaseDetail(100,"pool=nbc_jcat")
        self.checkPoint = ('caseName','TotalCaseNo','PassNo','Pass Rate','Trigger Loop')
        
    def checkOneCaseDetail(self,key):
        allCaseUnderASuite = []
        try :
            for case in self.caseDict[key]:
                caseDict = {}
                caseExecutionDetail = []
                caseActuralExecuteNo,casePassNo = self.basicInfoIns.getCasePassNoAndActuralExecuteCaseNo(key,case)
                NBCVResult = self.basicInfoIns.getCaseTriggerLoop(key,case)
                passRate = self.basicInfoIns.getPassRate(caseActuralExecuteNo,casePassNo)
                print "caseActuralExecuteNo : ",caseActuralExecuteNo
                print "casePassNo : ",casePassNo
                print "NBCVResult : ",NBCVResult
                print "passRate : ",passRate
                print "---------------------------------------"
                #store the case pass number and NBC/NBV result to a list.
                caseExecutionDetail.append(case[:11])
                caseExecutionDetail.append(caseActuralExecuteNo)
                caseExecutionDetail.append(casePassNo)
                caseExecutionDetail.append(passRate)
                caseExecutionDetail.append(NBCVResult)
                caseDict[case] = caseExecutionDetail
                allCaseUnderASuite.append(caseDict)
        except Exception, e :
            print Exception,":", e
        return allCaseUnderASuite

    def checkCase(self):
        for suite in self.caseDict.keys():
            caseDict = self.checkOneCaseDetail(suite)
            self.suiteExecutionDetail[suite] = caseDict
        print "suite result : ",self.suiteExecutionDetail
        return self.suiteExecutionDetail
      
if __name__ == "__main__":
    checkCaseIns = CheckNBV2NBCCaseDetail()
    checkCaseIns.checkCase()
    checkCaseIns.basicInfoIns.printStatistics(checkCaseIns.suiteExecutionDetail,checkCaseIns.checkPoint)
