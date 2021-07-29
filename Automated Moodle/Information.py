import moodle
import sys
import argparse
cmt_args=sys.argv
print("Running",cmt_args[0])
parser = argparse.ArgumentParser(prog='Information',
                                 usage='''
                                Usage:
                                 takes No arguments
                                return Latest Posts

                                ''',
                                 description='''
                                -----------------------------------------------
                                Description:
                                This tool will display  information by TnP cell.
                                -----------------------------------------------
                                ''',
                                 epilog="Copyrights @ Aman Gupta",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 add_help=True
                                 )
arg = parser.parse_args()


moodle.Moodle("x","y").Information()
