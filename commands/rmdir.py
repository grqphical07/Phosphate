# Command used to remove a directory in the current working directory
import os

def command(shell, args):
    os.rmdir(os.path.join(shell.path, args[1]))

def help():
    return ("rmdir", "Removes a directory: rmdir [DIRECTORY NAME]")