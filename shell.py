import os
import getpass
import socket
from colorama import init
from colorama import Fore

import subprocess
init()

class Shell:
    def __init__(self):
        self.path = os.getcwd()
        self.prompt = f"{Fore.YELLOW}{getpass.getuser()}@{socket.gethostname()}: {Fore.CYAN}{os.path.splitdrive(self.path)[1]}\\\033[39m "
        self.running = True
        while self.running:
            command = input(self.prompt)
            if command == "exit":
                self.running = False
            else:
                self.syscommand(command)
    def syscommand(self, command):
        subprocess.run(command, shell=True)

shell = Shell()