import os
import getpass
import socket
import sys
import importlib
from colorama import init
from colorama import Fore
import subprocess


# Initalize colorama
init()

# Main shell class
class Shell:
    def __init__(self):
        self.path = os.getcwd()
        self.prompt = f"{Fore.YELLOW}{getpass.getuser()}@{socket.gethostname()}: {Fore.CYAN}{os.path.splitdrive(self.path)[1]}\\\033[39m "
        self.path_variables = {}
        if not os.path.exists(".PATH"):
            with open(".PATH", "w") as f:
                f.write("")
        with open(".PATH", "r") as f:
            for line in f.readlines():
                name, path = line.split("=")
                self.path_variables[name] = path
        self.running = True
        self.isCommand = False

        self.enviroment_variables = {}
    
    # Main runtime function
    def run(self):
        print(f"Phosphate Version 1.00.0 (October 10th, 2022) Running on '{sys.platform}'")
        while self.running:
            # Take input and split into arguments
            command = input(self.prompt)
            if command == "exit":
                sys.exit()
            if command == "help":
                self.help()
            self.interpretcommand(command)

                
    def syscommand(self, command):
        try:
            value = subprocess.run(command, shell=True, check=True, capture_output=True)
            print(value)
        except:
            print(f"Command '{command}' was not found. Use 'help' to view all commands")
    
    def changeCWD(self, newCWD):
        self.path = os.path.abspath(newCWD)
        self.prompt = f"{Fore.YELLOW}{getpass.getuser()}@{socket.gethostname()}: {Fore.CYAN}{os.path.splitdrive(self.path)[1]}\\\033[39m "
        
    def help(self):
        for file in os.listdir("commands/"):
                if not file == "__init__.py" and file.endswith(".py"):
                    command, message = importlib.import_module(f"commands.{file[0:-3]}").help()
                    print(f"{command}: {message}")
    def interpretcommand(self, command):
        self.args = command.split()
        isPathVar = False
        # first check if its a path variable then run it
        for k, v in self.path_variables.items():
            if self.args[0] == k:
                self.args.pop(0)
                self.args.insert(0, v)
                subprocess.run(self.args, capture_output=True)
                isPathVar = True
                break
        # Check for any enviroment variables used
        for i, arg in enumerate(self.args):
            for k, v in self.enviroment_variables.items():
                if arg.find(f"${k}") != -1:
                    newstr = arg.replace(f"${k}", v)
                    self.args[i] = newstr
                    

        # Loop through every file in the commands folder and if its valid run it's command function
        for file in os.listdir("commands/"):
            if self.args[0] == file[0:-3] and not file == "__init__.py" and file.endswith(".py"):
                importlib.import_module(f"commands.{self.args[0]}").command(self, self.args)
                self.isCommand = True
                break
            else:
                self.isCommand = False
                
        # If it didnt run above execute it as a system command
        if not self.isCommand:
            self.syscommand(command)

shell = Shell()
shell.run()