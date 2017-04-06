#!/bin/tcsh

#config git base information for the current user.
#username and user email
#also clone the performance code to local at the dedicated folder.

if ($# != 2) then 
    echo "\033[31mTWO paramtersi required. first is your EID second is your E/// email adress\033[0m"
    exit()
else 
    set userName=$1
    set email=$2
endif

set user=`whoami`
set PERFREPO="gerrit.ericsson.se:29418/msran-jcat/msran-test-performance"
#configure the git 
git config --global user.name "${userName}"
git config --global user.name "${email}"

set GITBASEDIR="/home/${user}/git"
if (! -d ${GITBASEDIR}) then
    echo "folder \033[31m[ ${GITBASEDIR} ]\033[0m does not exist, creating..."
    mkdir -p ${GITBASEDIR}
endif
echo "cleanning the directory [ ${GITBASEDIR}/msran-test-performance ]..."
rm -rf ${GITBASEDIR}/msran-test-performance
echo "start cloning the repository [ msran-test-performance ] to ${GITBASEDIR}"
echo "this may cost around 30 seconds, please wait..."
cd ${GITBASEDIR}
git clone ssh://${user}@${PERFREPO}
echo "clone completed..."
