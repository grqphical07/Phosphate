# Command used to create a directory in the current working directory
import os

def command(shell, args):
    os.mkdir(os.path.join(shell.path, args[1]))

def help():
    return ("mkdir", "Creates a new directory: mkdir [DIRECTORY NAME]")