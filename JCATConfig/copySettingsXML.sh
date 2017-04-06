#!/bin/tcsh

#this file is to copy the corresponding settings.xml to local 
#the .m2 folder will be created if it does not exist
#NOTE that this script doesn't support the Ottawa site.
#will add it if it is necessary.

set curTime=`date +'%Y-%m-%d %H:%M:%S'`

set ERICLOUD="/app/durata/settings/maven/settings_eiffel_nexus_kista_modified_local_repo_path_for_ericcloud_linkoping.xml"
set LKPKISTA="/app/durata/settings/maven/settings_eiffel_nexus_kista.xml"
set OTTAWA="/app/durata/settings/maven/settings_Ottawa.xml"

set username=`whoami`
set serverName=`hostname`
set CopyDestPath="/home/${username}/.m2"
set LOGDIR="/home/${username}/tools/copy.log"

#unalias the cp, the cp command will override the existed files if the -f is given.
#cp ~/.cshrc.user ~/.cshrc.user_bak
#echo "unalias cp" >> ~/.cshrc.user
#source ~/.cshrc.user


echo "[ ${curTime} ] INFO hostname : ${serverName}"
echo "[ ${curTime} ] INFO username : ${username}" 

#get the server localtion and choose the correct file path
#here linkoping and kista use the same filepath
if (`echo ${serverName}|grep 'ki'|wc -l` == 1) then
    echo "[ ${curTime} ] INFO current server : KISTA "
    set CopySourcePath=${LKPKISTA}
else if (( `echo ${serverName}|grep 'li'|wc -l` == 1)) then
    echo "[ ${curTime} ] INFO current server : LINKOPING " 
    set CopySourcePath=${LKPKISTA}
endif

#copy the file to /home/username/.m2/settings.xml
if (! -d ${CopyDestPath}) then 
    echo "[ ${curTime} ] the path ${CopyDestPath} doesn't existed, creating..." 
    mkdir -p ${CopyDestPath}
endif
#start copy
echo "[ ${curTime} ] copying the file [ ${CopySourcePath} ] to [ ${CopyDestPath}/settings.xml  ]"    
cp -f ${CopySourcePath} ${CopyDestPath}/settings.xml
if (0 == $?) then 
    echo "\033[34m[ ${curTime} ] copy succeeded.\033[0m"
else 
    echo "\033[31m[ ${curTime} ] copy failed...\033[0m"
endif
