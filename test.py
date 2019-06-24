#Import dependencies
from subprocess import call
import os
from datetime import datetime

def Make_Directory():
    dirName='Backup'
    print("########## ",os.getcwd())
    try:
        os.mkdir(dirName)
    except FileExistsError:
        pass

    try:   
        os.chdir(dirName)
    except OSError:
        pass

    dateTimeObj = datetime.now()
    print(dateTimeObj)
    date=(str)(dateTimeObj.day+6) +'-'+ (str)(dateTimeObj.month)+'-'+ (str)(dateTimeObj.year)  
        
    dirName=date
    try:
        os.mkdir(dirName)
    except FileExistsError:
        pass
        
    try:   
        os.chdir(dirName)
    except OSError:
        pass
#Commit Message
call('git init',shell = True)
try:
    call('git remote add origin https://github.com/singhimanshu123456/test2.git',shell = True)
except:
    print("except")
#Make_Directory()
with open("hello.txt" ,"w") as f:
    f.write("hellhho")
with open("hello1.txt" ,"w") as f:
    f.write("hellhdho")
with open("hello2.txt" ,"w") as f:
    f.write("hellhho")
with open("hello4.txt" ,"w") as f:
    f.write("hellgggghho")
commit_message = "Adding sample files"

#Stage the file 

call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)