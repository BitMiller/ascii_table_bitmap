#BEGIN#

#help: https://www.w3schools.com/python/default.asp

import os
from datetime import datetime

# Program creation timestamp:
prgVer = "@"

# Program description:
prgDsc = ""

# Program template version:
prgTemplateVer = "241105-5-1221"

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__base_projects/_base_at241016-3-1004/code/main.py"

runStartTime = datetime.now()
runInstanceDateTimeStamp = "at" \
+ str(runStartTime.year)[2:].zfill(2) \
+ str(runStartTime.month).zfill(2) \
+ str(runStartTime.day).zfill(2) \
+ "-" + str(runStartTime.weekday()+1) + "-" \
+ str(runStartTime.hour).zfill(2) \
+ str(runStartTime.minute).zfill(2) \
+ str(runStartTime.second).zfill(2) \
+ "-" \
+ str(runStartTime.microsecond).zfill(6)

# Change working directory to project's root directory
prjRoot = "storage/shared/"+runCmd[27:]
prjRoot = os.path.dirname(prjRoot)
prjRoot = os.path.dirname(prjRoot)
os.chdir(prjRoot)

print()
print("==*******************==")
print("     PROGRAM BEGIN    ")
print(f"> Version: {prgVer}")
print(f"> Description: {prgDsc}")
print(f"> Working dir/Project's root dir: {os.getcwd()}")
print(f"> Run start time: {runStartTime}")
print(f"> runInstanceDateTimeStamp: {runInstanceDateTimeStamp}")
print("----------------------\n\n")

#----------------------------------------#





#----------------------------------------#

print("\n\n----------------------")
print("      PROGRAM END")
print("==*******************==")
print()

#END#