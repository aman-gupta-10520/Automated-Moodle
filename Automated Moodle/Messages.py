import moodle
import sys
cmt_args=sys.argv
print("Running",cmt_args[0])
username=cmt_args[1]
password=cmt_args[2]
obj=moodle.Moodle(username,password)
obj.Messages()