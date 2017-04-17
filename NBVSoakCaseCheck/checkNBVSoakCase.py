#!/usr/bin/python

import sys
import os
import re
parentDir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.insert(0,parentDir)
from Common import readCaseFile as rf
from Common import checkCaseBasicInfo as cb

class CheckNBVSoakCase(object):
    def __init__(self):
        self.specPath = "/home/efuguxu/git/nbv-config/main/nbv/soak/exec/performance"
        #self.specPath = "/home/efuguxu/tools/PUMATools/NBVSoakCaseCheck/specs"
        readFileIns = rf.ReadFile()
        self.caseDict = readFileIns.readCaseFolder(self.specPath)
        #print "self.caseDict : ",self.caseDict
        self.suiteExecutionDetail = {}
        self.basicInfoIns = cb.CheckCaseDetail(20,"")
        self.checkPoint = ('caseName','TotalCaseNo','PassNo','Pass Rate','UP Number')
 
    def getUPVersion(self,suite,case):
        caseRawLogCmd = "tgr suite "+suite+" 20 v | egrep 'CXP|"+case[:11]+"\'"
        print "caseRawLogCmd : ",caseRawLogCmd
        caseRawLog = os.popen(caseRawLogCmd)
        upNameList = [] 
        upNamePattern = re.compile("CXP.*? ")
        for line in caseRawLog.readlines():
#            print "line : ",line
            if 'xml' in line:
                try : 
                    upName = re.findall(upNamePattern,line)[0].strip()
                    continue
                except IndexError:
                    upName = ""
            if 'LTE' in line and 'ok' in line and 'nok' not in line:
                upNameList.append(upName)
        upNameList = list(set(upNameList))
        print "upNameList : ",upNameList
        return len(upNameList)
        
    def checkCaseDetail(self):
        number = 0
        allCaseUnderASuite = []
        for item in self.caseDict:
            #print "item : ",item
            if 0 != len(item):
                for suite in item.keys():
                    print "checking suite : ",suite
                    for case in item[suite]:
                        suite = suite[suite.rfind("/")+1 : ]
#                        print "    --case : ",case
                        oneCaseDetail = {}
                        caseExecutionDetail = []
                        #allCaseUnderASuite = []
                        caseActuralExecuteNo,casePassNo = self.basicInfoIns.getCasePassNoAndActuralExecuteCaseNo(suite,case)
                        passRate = self.basicInfoIns.getPassRate(caseActuralExecuteNo,casePassNo)
                        #store the case pass number and NBC/NBV result to a list.
                        caseExecutionDetail.append(case[:11])
                        caseExecutionDetail.append(caseActuralExecuteNo)
                        caseExecutionDetail.append(casePassNo)
                        caseExecutionDetail.append(passRate)
                        caseExecutionDetail.append(self.getUPVersion(suite,case))
                        oneCaseDetail[case] = caseExecutionDetail
                        allCaseUnderASuite.append(oneCaseDetail)
                    self.suiteExecutionDetail[suite] = allCaseUnderASuite
                    allCaseUnderASuite = []
#       return allCaseUnderASuite

if __name__ == "__main__":
    checkCaseIns = CheckNBVSoakCase()
    #checkCaseIns.checkCase()
    checkCaseIns.checkCaseDetail()
    checkCaseIns.basicInfoIns.printStatistics(checkCaseIns.suiteExecutionDetail,checkCaseIns.checkPoint)
