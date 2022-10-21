# Command for clearing the screen
import subprocess

def command(shell, args):
    subprocess.run("cls", shell=True)

def help():
    return ("cls", "Clears the terminal screen")