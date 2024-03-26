import subprocess

_shell = "start cmd /c python main.py"

subprocess.call(_shell, shell=True)