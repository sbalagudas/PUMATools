you can get the specified case details in the last 100 execution history.

Just Execute  :  < nohup ./run.sh & > or < nohup /bin/tcsh ./run.sh & > to start the script

the Script will collect the all test cases which configured in the file <caseFile.txt> once a day. (execute in every 86400 seconds)

If more cases need to be added, please add it/them in the following way : 
starts with a '#', e.g. 
	#suite name 
		case name which belongs to the suite.

if you have any questions. just let me know. [fugui.xu@tieto.com]
