#!/bin/tcsh

#copy the specified file(s) from 935 to linkoping
#the files will be stored on linkoping at location :
#/home/usrname/tmp
#the scripts executed on local will copy these files to local

set curUserName=`whoami`
set server7776="134.138.177.56"
set server935="137.58.159.173"
set defaultLocation="/home/${curUserName}/tmp"

#make directories if they don't existed both on linkoping and 7776
mkdir -p ${defaultLocation}
ssh ${server7776} "mkdir -p ${defaultLocation}"

if ("X" == "X$1") then
    set source=${defaultLocation}
else
    set source=$1
endif
#echo "ssh ${server7776} 'scp ${curUserName}@${server935}:${source}/\* ${defaultLocation}'"
ssh ${server7776} "scp ${curUserName}@${server935}:${source}/\* ${defaultLocation}"
scp ${server7776}:${defaultLocation}/\* ${defaultLocation}

