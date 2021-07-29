import moodle
import sys
import argparse
'''
cmt_args=sys.argv
print("Running",cmt_args[0])
username=cmt_args[1]
password=cmt_args[2]
teacher_name=cmt_args[3]
if(len(cmt_args)==5):
    number=cmt_args[4]
else:
    number=1
obj=moodle.Moodle(username,password)
obj.Attendance(teacher_name,number)'''
parser = argparse.ArgumentParser(prog='Attendance',
                                 usage='''
                                Usage:
                                Pass username,password and teacher_name to submit the attendance
                                and one optional argument 


                                ''',
                                 description='''
                                -----------------------------------------------
                                Description:
                                This tool will submit the attendance
                                -----------------------------------------------
                                ''',
                                 epilog="Copyrights @ Aman Gupta",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 add_help=True
                                 )

parser.add_argument("username", type=str, help="Enter Username. for example: 0901CS171021", metavar="Username")
parser.add_argument("password", type=str, help="Enter Password. for example: Rahul@122", metavar="Password")
parser.add_argument("teacher", type=str, help="Enter Teacher Name. for example:Vishvas", metavar="Teacher")
parser.add_argument("--number", "-n", type=int,
                    help="Optional: Enter number of course of attendance in teacher's module for example: 1", default=1,
                    required=False)
arg = parser.parse_args()
obj = moodle.Moodle(arg.username, arg.password)
obj.Attendance(arg.teacher, arg.number)


