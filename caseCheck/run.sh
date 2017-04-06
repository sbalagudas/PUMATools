#!/bin/tcsh

#set TIMEFORMAT="%Y-%m-%d %H:%M:%S"
set CURDIR=`pwd`
set LOGDIR="${CURDIR}/caseLog.log"

while (1)
    echo "==========================" >> ${LOGDIR}
    echo `date +"%Y-%m-%d %H:%M:%S"` >> ${LOGDIR}
    echo "==========================" >> ${LOGDIR}    
    /usr/bin/python checkCaseDetailToFile.py >> ${LOGDIR}
    sleep 86400 
end


