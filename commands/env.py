# Add a new enviroment variable to the terminal

def command(shell, args):
    string = args[1]
    name, value = string.split("=")
    shell.enviroment_variables[name] = value

def help():
    return "Sets an enviroment variable. Format: env NAME=VALUE"