# Similar to copy or xcopy
import re
import os

def command(shell, args):
    if os.path.isfile(args[1]):              
        src = ""
        with open(os.path.abspath(args[1]), "r") as f:
            src = f.read()
        with open(os.path.abspath(args[2]), "w") as f:
            f.write(src)

def help():
    return ("copy", "Takes the contents of one file and pastes them into another file. copy [SOURCE] [DESTINATION]")