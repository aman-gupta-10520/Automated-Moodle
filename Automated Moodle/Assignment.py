import moodle
import sys
cmt_args=sys.argv
print("Running",cmt_args[0])
username=cmt_args[1]
password=cmt_args[2]
teacher_name=cmt_args[3]
file=cmt_args[4]
if(len(cmt_args)==6):
    number=cmt_args[5]
else:
    number=0
if(len(cmt_args)==7):
    ext=cmt_args[6]
else:
    ext=".pdf"
obj=moodle.Moodle(username,password)
obj.Assignment(teacher_name,file,number,ext)
