# Command used to print a message to the shell

def command(shell, args):
    for word in args:
        if args.index(word) == 0:
            continue
        print(word, end="")
        print(" ", end="")
    print("")

def help():
    return ("echo", "Used to print a message to the terminal: echo [MESSAGE HERE (Spaces are included)]")