# Lists all ENV variables and their values

def command(shell, args):
    for k, v in shell.enviroment_variables.items():
        print(f"${k} = {v}")

def help():
    return "Lists all active enviroment variables"