#!/bin/tcsh

#add modules and open the eclipse automatically
#if the user has already opened one eclipse, the openning process will be aborted.

#define the modules which need to be added.
#if there is some more modules needed, just add it/them at this place
set JDK="jdk/1.8.0_92"
set EECS="eecs/4.6.2"
set GIT="git/2.7.4"
set MAVEN="maven/3.3.9"
set UNZIP="unzip/6.0"

set currentUser=`whoami`
#check if the eclipse has already opened.
set eclipseInsNo=`ps -ef | grep eclipse | grep ${currentUser} |grep -v "grep" |  wc -l`

if (${eclipseInsNo} >= 1) then
    echo "\033[34m [NOTE] the [ ${currentUser} ] has already opened one eclipse instance.\033[0m"
else 
    echo "adding modules ...\n"
    echo "${JDK}\n${EECS}\n${GIT}\n${MAVEN}\n${UNZIP}\n"
    module add ${JDK}
    module add ${EECS}
    module add ${GIT}
    module add ${MAVEN}
    module add ${UNZIP}

    echo "\033[34m starting eclipse ...\033[0m"
    nohup eclipse &
endif
