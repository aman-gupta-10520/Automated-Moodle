import moodle
import sys
cmt_args=sys.argv
print("Running",cmt_args[0])
username=cmt_args[1]
password=cmt_args[2]
teacher_name=cmt_args[3]
if(len(cmt_args)==5):
    number=cmt_args[4]
else:
    number=0

obj=moodle.Moodle(username,password)
obj.Attendance(teacher_name,number)
