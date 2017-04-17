#!/bin/tcsh

#set TIMEFORMAT="%Y-%m-%d %H:%M:%S"
set CURDIR=`pwd`
set LOGDIR="${CURDIR}/soak.log"

while (1)
    echo "==========================" >> ${LOGDIR}
    echo `date +"%Y-%m-%d %H:%M:%S"` >> ${LOGDIR}
    echo "==========================" >> ${LOGDIR}    
    nohup /usr/bin/python checkNBVSoakCase.py >> ${LOGDIR} &
    sleep 86400 
end


