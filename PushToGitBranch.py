#! python

import time
import os

#This python file will perform the necessary comments to push all the information in this directory to the correct branch on the GitHub directory!

OneFile = raw_input(" All information in this directory will be pushed to the DocumentationFile branch on GitHub \n Press (n) if only a specific file should be pushed and not the entire directory. \n (y) will push the entire directory.  ")

if OneFile == "y" or OneFile == "Y":
    print "In 'y' option "
    os.system("git add *")
elif OneFile == "n" or OneFile == "N":
    print "In 'n' option "
    WhichFile = raw_input("--> Which file should be added?  ")
    os.system("git add "+WhichFile)   

GitHubComment = ""
if OneFile == "y" or OneFile == "Y" or OneFile == "n" or OneFile == "N":
    CommentInfo = raw_input(" Which information should be given to the commit ?  ")
    for ii in range(len(CommentInfo.strip())):
        GitHubComment += CommentInfo[ii]+""
    os.system("git commit -m '"+str(GitHubComment)+"'")
    print "-------------------------------------------------------------"
    PerformPush = raw_input("Should the commit be pushed to 'anomCouplings' remote and 'DocumentationFile' branch or should this be done only later?  (y/n)")
    if PerformPush == "y" or PerformPush == "Y":
        os.system("git push anomCouplings DocumentationFile")
    elif PerformPush == "n" or PerformPush == "N":
        print "\n Commit is done but will only be sent later to GitHub!"

