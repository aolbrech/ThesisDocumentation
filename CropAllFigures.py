# ---------------------------------------------------------------- #
# --- Use this file to crop all PDF's in the Figures directory --- #
# ---  * Give the correct Chapters directory as input          --- #
# ---------------------------------------------------------------- #

import sys
import os

whichDir = ""
if len(sys.argv) > 1:
    whichDir = str(sys.argv[1])
    print "Will be looking at directory: ", whichDir

# Change the working directory to the specified one!
os.chdir(whichDir)

# Now loop over all the pdf files present in this directory and crop them!
for pdf in os.listdir('.'):
    if pdf.endswith(".pdf"):
        print "* Will be cropping file ", pdf
        os.system('pdfcrop --margins 2 ' + pdf + " " + pdf)


