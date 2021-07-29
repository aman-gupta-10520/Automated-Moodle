import moodle
import sys
cmt_args=sys.argv
print("Running",cmt_args[0])
'''
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
obj.Assignment(teacher_name,file,number,ext)'''
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
parser.add_argument("filename", type=str, help="Enter File Name. for example:assignment2", metavar="filename")

parser.add_argument("--number", "-n", type=int,
                    help="Optional: Enter number of course of attendance in teacher's module for example: 1", default=0,
                    required=False)
parser.add_argument("--extension", "-ext", type=str,
                    help="Optional: Enter number of course of attendance in teacher's module for example: 1", default=".pdf",
                    required=False)
arg = parser.parse_args()
obj = moodle.Moodle(arg.username, arg.password)
obj.Assignment(arg.teacher,arg.filename, arg.number, arg.extension)

