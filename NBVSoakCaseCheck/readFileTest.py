#!/usr/bin/python

import sys
import os

parentDir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.insert(0,parentDir)
from Common import readCaseFile as rf

class ReadCaseFolder(rf):
    def readCaseFolder(self):
        caseDetailInFolder = []
         
fname0 = "/home/fabio/share/soakPerf/nbv_main_ssrbs_soak24h_performance_ki.spec"

rfIns = rf.ReadFile(fname0)
result = rfIns.readFileAndGetCaseDict()
print "result : ",result 
