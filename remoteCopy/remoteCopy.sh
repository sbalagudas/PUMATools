#!/bin/bash

serverLKP="150.132.35.142"
curUserName="efuguxu"
defaultSource="/home/${curUserName}/tmp"
#defaultDest="/home/fabio/tmp/tmp"
defaultDest="/c/tmp"

Usage()
{
    echo "param [-s STRING|-d STRING]"
}

function initialization()
{
    path=`pwd`

    echo "checking remote directories...${curUserName}"
    ssh ${curUserName}@150.132.35.142 "mkdir -p /home/${curUserName}/tools" 
    echo "checking autoCopy.sh script..."
    scp ${path}/autoCopy.sh ${curUserName}@150.132.35.142:/home/${curUserName}/tools 
    if [ $? -eq 0 ];then
        echo "initialization finished..."
    fi
}


while getopts ':is:d:h' OPT &> /dev/null;do
    case ${OPT} in
    i)
        initialization
        exit
        ;;
    s)
        echo "source : "${OPTARG}
        source=${OPTARG}
        ;;
    d)
        echo "dest : "${OPTARG}
        dest=${OPTARG}
        ;;
    h)
        echo "------------------------------------"
        echo "-i : initialization for the scripts"
        echo "-s : indicate the source directory"
        echo "    parameter : the source folder in 935 server"
        echo "    default value : /home/935homedir/tmp"
        echo "-d : indicate the dest directory"
        echo "    parameter : the local folder you want the file stored" 
        echo "    default value : /c/tmp/"
        echo "-h : print help message"
        echo "------------------------------------"
        exit 7
        ;;
    \?)
        echo "not supported paramters..."${OPTARG}
        exit 
        ;;
    esac
done

if [ ! -d ${defaultDest} ];then
    mkdir ${defaultDest}
fi

if [ -z "${source}" ];then
    echo "INFO : source is null, using default path :  ${defaultSource}."
    source=${defaultSource}
fi
if [ -z "${dest}" ];then
    echo "INFO : dest is null, using default value : ${defaultDest}"
    dest=${defaultDest}
else
    if [ ! -d ${dest} ];then
        mkdir -p ${dest}
    fi
fi

echo "DEBUG : source -> "${source}
echo "DEBUG : dest -> "${dest}

ssh efuguxu@150.132.35.142 "/bin/tcsh /home/efuguxu/tools/autoCopy.sh ${source}"
scp efuguxu@150.132.35.142:/home/efuguxu/tmp/* ${dest}/



