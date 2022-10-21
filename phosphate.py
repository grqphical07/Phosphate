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
        self.running = True
        self.isCommand = False
    
    # Main runtime function
    def run(self):
        print(f"Phosphate Version 1.00.0 (October 10th, 2022) Running on '{sys.platform}'")
        while self.running:
            # Take input and split into arguments
            command = input(self.prompt)
            args = command.split()
            if args[0] == "exit":
                self.running = False
            elif args[0] == "help":
                self.help()
            else:
                
                # Loop through every file in the commands folder and if its valid run it's command function
                for file in os.listdir("commands/"):
                    if args[0] == file[0:-3] and not file == "__init__.py" and file.endswith(".py"):
                        importlib.import_module(f"commands.{args[0]}").command(self, args)
                        self.isCommand = True
                        break
                    else:
                        self.isCommand = False
                
                # If it didnt run above execute it as a system command
                if not self.isCommand:
                    self.syscommand(command)

                
    def syscommand(self, command):
        subprocess.run(command, shell=True)
    
    def changeCWD(self, newCWD):
        self.path = os.path.abspath(newCWD)
        self.prompt = f"{Fore.YELLOW}{getpass.getuser()}@{socket.gethostname()}: {Fore.CYAN}{os.path.splitdrive(self.path)[1]}\\\033[39m "
    def help(self):
        for file in os.listdir("commands/"):
                if not file == "__init__.py" and file.endswith(".py"):
                    command, message = importlib.import_module(f"commands.{file[0:-3]}").help()
                    print(f"{command}: {message}")

shell = Shell()
shell.run()