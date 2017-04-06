The scripts in this folder is going to copy the files from remote server sekilx935/sekilx936 to local, this will reduce some time for the multi-scp process.
the copy route is : 
	[your local Machine] <-- [Linkoping] <-- [sekilx7776] <-- [sekilx935/936]

the home directory on 935 and 936 server are the same.

################################################################
Before Start, you should have done some preparations:
	1. register the SSH Keys between the servers shown above. then you can copy the files from remote to local without any password.
		e.g. copy the local SSH Key to Linkoping
		     copy the Linkoping SSH Key to 7776
		     copy the 7775 SSH Key to sekilx935
	2. install a software called <Git Bash> by which you can use the shell commands in windows.

################################################################
################################################################
----------------------------------------------------------------
autoCopy.sh
	this script will be deployed to linkoping at location :/home/yourhomedir/tools automatically.you can just ignore it.
----------------------------------------------------------------
remoteCopy.sh
	this script is executed at local. you can type ./remoteCopy.sh -h to get more details.
----------------------------------------------------------------

How to Start : 
	1. execute the command ./remoteCopy.sh -i
	2. ./remoteCopy with corresponding paramters.
