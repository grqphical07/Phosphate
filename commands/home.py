# Command to return user to hom
import os

def command(shell, args):
    shell.changeCWD(os.path.expanduser("~"))

def help():
    return ("home", "Sets the current directory to the users home directory (C:\\Users\\[USER] on Windows)")