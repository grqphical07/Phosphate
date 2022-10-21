# Command for listing files in current directory
import subprocess

def command(shell, args):
    subprocess.run(f'dir "{shell.path}"', shell=True)

def help():
    return ("ls", "Used to list all files in a directory")