#!/usr/bin/python

import os
import re

import readCaseFile as rf

#the file will get the case execution details from TGF and draw them in to a table.
#the latest tgjob id will be selected and checking from which it is triggered.
class CheckCaseDetail(object):
    def __init__(self):
        self.readFileIns = rf.ReadFile()
        self.suiteExecutionDetail = {}
        self.caseDict = self.readFileIns.readFileAndGetCaseDict()

    def checkOneCase(self,key):
        allCaseUnderASuite = []
        try :
            for case in self.caseDict[key]:
                caseDict = {}
                caseExecutionDetail = []
                #calculate case pass number.
                casePassCmd = "tgr suite "+ key + " 100 v pool=nbc_jcat | grep \'"+ case[:11]+"\' | awk '{print $5}' | grep ok | grep -v nok | wc -l"
                #print "DEBUG : PASS NO : ",casePassCmd
                caseActuralExecuteNoCmd = "tgr suite "+ key + " 100 v pool=nbc_jcat | grep \'" + case[:11]+ "\' | wc -l "
                #print "DEBUG : ACTRUAL CMD : ",caseActuralExecuteNoCmd
                caseActuralExecuteNo = os.popen(caseActuralExecuteNoCmd).readlines()[0].strip()
                casePassNo = os.popen(casePassCmd).readlines()[0].strip()

                #get NBC/NBV
                caseNBCVCmd = "tgr suite "+ key + " 100 v pool=nbc_jcat | egrep \'"+key[:-4] + "|" + case[:11] + "\' | tail -2 | head -1 | awk '{print $1}'"
                suiteJobId = os.popen(caseNBCVCmd).readlines()[0].strip()
                NBCVResult = os.popen("tgr "+ suiteJobId + " | grep jenkins" ).readlines()
                if 0 == len(NBCVResult):
                    #print "[ INFO ] : CASE :[ %s ], The latest job was not triggered from jenkins."%(case)
                    NBCVResult = 'Manual Case'                   
                else :
                    NBCVResult = re.findall("job\/(.*?)\/.*",NBCVResult[0])[0]
                
                #store the case pass number and NBC/NBV result to a list.
                caseExecutionDetail.append(casePassNo)
                caseExecutionDetail.append(caseActuralExecuteNo)
                caseExecutionDetail.append(NBCVResult)
                caseDict[case] = caseExecutionDetail
                allCaseUnderASuite.append(caseDict)
        except Exception, e :
            print Exception,":", e
        return allCaseUnderASuite
    def checkCase(self):
        for suite in self.caseDict:
            caseDict = self.checkOneCase(suite)
            self.suiteExecutionDetail[suite] = caseDict
        #print "suite Detail : ",self.suiteExecutionDetail
    
    def printStatisticsInFormat(self):    
        caseNeedToCheck = {}
        print "--------------------------------------------------------------------------------"     
        print "|%12s | %12s | %12s | %12s | %18s|"%("CASE NAME","PASS","TOTAL","PASS RATE","LOOP")
        for key in self.suiteExecutionDetail: 
            for item in self.suiteExecutionDetail[key] : 
                for case in item.keys() : 
                    passRate = round(float(item[case][0])/float(item[case][1]),2)*100
                    if passRate >= 99.0 and "NBV" in item[case][2]:
                        caseNeedToCheck[case] = item[case][2]
#                    passRate = str(passRate).strip()
                    print "|%12s | %12s | %12s | %12s | %18s|"%(case[:11],item[case][0],item[case][1],passRate,item[case][2])
        print "--------------------------------------------------------------------------------"     
        print "case Need to Check : "
        print "|%12s | %12s |"%("CASE NAME","Trigger Loop")
        for key in caseNeedToCheck:
            print "|%12s | %12s|"%(key[:11],caseNeedToCheck[key])
        print "------------------------------"     
if __name__ == "__main__":
    caseDetail = CheckCaseDetail()
    #print "Checking Case from TGF, Please wait..."
    caseDetail.checkCase()
    caseDetail.printStatisticsInFormat()
