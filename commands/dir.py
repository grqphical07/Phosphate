import subprocess

def command(shell, args):
    subprocess.run(f"dir {shell.path}", shell=True)