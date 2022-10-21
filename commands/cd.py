# Command for changing directories
import os

def command(shell, args):
    path = ""

    for i in args:
        if args.index(i) == 0:
            continue
        elif args[1] == "..":
            path = os.path.dirname(shell.path)
        else:  
            path += f"{i}"
            if not i == args[-1]:
                path += " "

    if os.path.exists(path):
        shell.changeCWD(path)
    else:
        print(f"Path '{path}' does not exist")

def help():
    return ("cd", "Used to navigate directories in the file system")