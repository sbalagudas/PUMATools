This document describing How to configure the JCAT Environment in the Eclipse. After these configuration,
you can execute test cases in the Eclipse.

###################################        
###################################        
There are 3 scripts included in this folder, if you are interest for more details, just go to the code :)
	copySettingsXML.sh
	gitConfigAndClonePerf.sh
	startEclipse.sh

If you find any error or have any suggestion, just let me know : fugui.xu@tieto.com
All the steps in this document are refer from page : [ https://wiki.lmera.ericsson.se/wiki/DURA_JCAT_Wiki/Environment ] 

###################################        
###################################        
To executing the test cases via Eclipse, please do those configurations on server not HUB.
For Performance, the servers available below:
	sekilx514
        sekilx238
for other team, please refer to below page for more detail : 
	[ https://wiki.lmera.ericsson.se/wiki/DURA_JCAT_Wiki/Environment#Kista_Servers_-_Available ] 

###################################
###################################
Before you executing the scripts, you should have done : 
	1. VX terminal Configuration which can make you log in to the remote server(e.g.linkoping or kista7776)

	2. Registered to the Gerrit with your own SSH-KEYs. need help, please see the section <HOW TO REGISTER TO GERRIT>
	3. Corresponding Access rights need to be applied, see [ https://wiki.lmera.ericsson.se/wiki/DURA_JCAT_Wiki/Environment#Required_Access ] for more details.

###################################        
###################################
After you have done the steps above, you can ;
	1. Execute script : <copySettingsXML.sh>. this will copy the maven configure file from the correct place to your HOMEDIR/.m2/ and rename it as settings.xml.(if the xml is not correct, the compiling of the code will be failed.)

	2. Execute script : <gitConfigAndClonePerf.sh UserName UserEmail>. this will configure the git username and email of your own. and also clone the performance code to the directory : HOMEDIR/git/ by default. This script need two paramters, first is your EID second is yor E/// email address. This script will remove all the contents in folder [/home/yourname/git/], so please backup them if there's any.

	3. Execute script : <startEclipse.sh>. the modules needed by Eclipse will be added automatically. but a restrict was given that there is only one Eclipse instance can be created. which means, you can only open ONE Eclipse window.

	4. After you opened the Eclispe, please do some configuration before you import the Maven Project.
	please refer to the page [ https://wiki.lmera.ericsson.se/wiki/DURA_JCAT_Wiki/Environment#Eclipse_plugins_installation ]
        When completed the Eclipse configuration, import the project you just cloned in folder [ /home/yourname/git/msran-test-performance File -> Import -> Maven -> Existing Maven Projects ]. 
	5. The Eclipse will import the Maven dependencies and java resources, just wait for a few minutes. (you can see the progress and details at the right-bottom)
	

###################################
###################################
So far, your Eclipse configuration is completed.
there is only one more thing need to consider : import the MJE properties to your project.
	1. Clone the stp_cfg to your local. [ git clone ssh://yourEID@gerrit.ericsson.se:29418/cirv/stp_cfg ] 
	2. Project -> Right Click -> build path -> configure build path -> libraries -> Add External Class Folder -> Select the MJE properties you just cloned -> Order and Export -> select the folder you just imported -> OK
	Now, you can run the case. Good luck!

###################################        
#Trouble Shootings
###################################        
-------------------------------------
Problem : HOW TO REGISTER TO GERRIT
Solution : Actually, this is a secure machanism in GIT. if you want to clone the code from GIT, you should make the GIT server knows who you are. A good way is register your SSH-KEY to the GIT server. 
	1. Check whether your own SSH-KEY is generated. [ ls ~/.ssh/ to see if there is a file named id_rsa.pub ]
        2. If no such a id_rsa.pub file, please execute [ ssh-keygen -t rsa and following coupole of ENTER, two files will be generated id_rsa.pub and id_rsa ] 
        3. Now you have your own SSH-KEY, open the link : [ https://gerrit.ericsson.se/#/q/status:open ], sign in and go to settings -> SSH Public Keys -> Add Key
	4. Copy the id_rsa.pub content and paste it into the page. Click Add. Now you are registered into the GERRIT. 
-------------------------------------
Problem : How to deal with the problem when you can't use < module > command 
Solution : Just copy the .cshrc and .cshrc.user to your server's home directory. and source them.

