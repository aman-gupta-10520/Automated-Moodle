import moodle
import sys
import argparse
'''
cmt_args=sys.argv
print("Running",cmt_args[0])
username=cmt_args[1]
password=cmt_args[2]
teacher=cmt_args[3]
obj=moodle.Moodle(username,password)
obj.Grades(teacher)'''

parser = argparse.ArgumentParser(prog='Grades',
                                 usage='''
                                Usage:
                                Pass username,password and return table of grades 


                                ''',
                                 description='''
                                -----------------------------------------------
                                Description:
                                This tool will show grades
                                -----------------------------------------------
                                ''',
                                 epilog="Copyrights @ Aman Gupta",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 add_help=True
                                 )

parser.add_argument("username", type=str, help="Enter Username. for example: 0901CS171021", metavar="Username")
parser.add_argument("password", type=str, help="Enter Password. for example: Rahul@122", metavar="Password")
parser.add_argument("teacher", type=str, help="Enter Teacher Name. for example:Vishvas", metavar="Teacher")

arg = parser.parse_args()
obj = moodle.Moodle(arg.username, arg.password)
obj.Grades(arg.teacher)