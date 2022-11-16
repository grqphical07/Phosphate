# Command used to run scripts

def command(shell, args):
    file = args[1]
    with open(file, "r") as f:
        for line in f.readlines():
            shell.interpretcommand(line)

def help():
    return "Runs a given file as a script"