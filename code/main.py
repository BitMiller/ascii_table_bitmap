#BEGIN#

#help: https://www.w3schools.com/python/default.asp

import os
from datetime import datetime

def clrscr():
 os.system("cls" if os.name == "nt" else "clear")


clrscr()

# Program creation timestamp:
prgVer = "@"

# Program description:
prgDsc = ""

# Program template version:
prgTemplateVer = "241105-5-1221"

# Program run command in Android:Termux:Python :
runCmd = "python /storage/emulated/0/BitMiller/Pradhana/Dropbox/bitmiller_hu/progs/python_for_termux/__projects/ascii_table_bitmap/code/main.py"

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
prjRoot = runCmd[7:]
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

hexa = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

with open("input/ASCII-table.php", "r") as f:
 raw_data = f.readlines()

data:list = []

for l in raw_data:
 d = l.strip().split()
 for i in range(len(d)):
  d[i] = int(d[i])
 data.append(d)

#print(data)

fn = "_no_sync/output/ascii_bitmaps.txt"

ver = 3

match ver:
 case 1:
  with open(fn, "w") as f:
   for i in range(len(data)):
    f.write(f"#{i//100}{i//10%10}{i%10}#\n")
    bm:list = []
    for j in range(len(data[i])):
     l = data[i][j]
     bm.append([])
     for k in range(16):
      if l%2 == 0:
       bm[j].append(".")
      else:
       bm[j].append("O")
      l //= 2

    for j in range(16):
     for k in range(len(data[i])):
      f.write(bm[k][j])
     f.write("\n")
    f.write("\n")

 case 2:
  with open(fn, "w") as f:
   for i in range(len(data)):
    f.write(f"#{i//100}{i//10%10}{i%10}#\n")
    bm:list = []
    for j in range(len(data[i])):
     l = data[i][j]
     bm.append([])
     for k in range(16):
      if l%2 == 0:
       bm[j].append(".")
      else:
       bm[j].append("O")
      l //= 2

    f.write("   01234567\n")
    for j in range(16):
     f.write(f"{j//10}{j%10}|")
     for k in range(len(data[i])):
      f.write(bm[k][j])
     f.write("\n")
    f.write("   01234567\n")
    f.write("\n")

 case 3:
  with open(fn, "w") as f:
   for i in range(len(data)):
    f.write(f"#{i//100}{i//10%10}{i%10}# ")
    f.write(f"&{hexa[i//16]}{hexa[i%16]}&\n")
    bm:list = []
    for j in range(len(data[i])):
     l = data[i][j]
     bm.append([])
     for k in range(16):
      if l%2 == 0:
       bm[j].append(".")
      else:
       bm[j].append("O")
      l //= 2

    f.write("   12345678\n")
    for j in range(16):
     f.write(f"{(j+1)//10}{(j+1)%10}|")
     for k in range(len(data[i])):
      f.write(bm[k][j])
     f.write("\n")
    f.write("   12345678\n")
    f.write("\n")



#----------------------------------------#

print("\n\n----------------------")
print("      PROGRAM END")
print("==*******************==")
print()

#END#