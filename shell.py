import os
import getpass
import socket
import importlib
from colorama import init
from colorama import Fore

import subprocess
init()

class Shell:
    def __init__(self):
        self.path = os.getcwd()
        self.prompt = f"{Fore.YELLOW}{getpass.getuser()}@{socket.gethostname()}: {Fore.CYAN}{os.path.splitdrive(self.path)[1]}\\\033[39m "
        self.running = True
        self.commands = {}
        for file in os.listdir("commands/"):
                if file.endswith(".py") and not file == "__init__.py":
                    self.commands[file[0:-3]] = importlib.import_module(f"commands.{file[0:-3]}")
    
    def run(self):
        while self.running:
            command = input(self.prompt)
            args = command.split()
            if args[0] == "exit":
                self.running = False
            else:
                print(self.commands)
                for k, v in self.commands:
                    if args[0] == k:
                        v.command(self, args)
                
    def syscommand(self, command):
        subprocess.run(command, shell=True)

shell = Shell()
shell.run()