# Command used to remove a directory in the current working directory
import os

def command(shell, args):
    if args[1] == "*":
        for dir in os.listdir(shell.path):
            if os.path.isdir(os.path.join(shell.path, dir)):
                os.rmdir(os.path.join(shell.path, dir))
    else:
        os.rmdir(os.path.join(shell.path, args[1]))

def help():
    return ("rmdir", "Removes a directory: rmdir [DIRECTORY NAME]. Use * to delete all directories in the current directory")