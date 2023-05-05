import os
import subprocess

# Change the working directory to the directory where your python files reside.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Activate the virtual environment.
subprocess.Popen(['pipenv', 'shell'])

# Open the first program in a new window. Deactivated for now
subprocess.Popen(['cmd', '/c', 'start', 'python', 'twitchGPT.py'])

# Open the second program in a new window.
# subprocess.Popen(['cmd', '/c', 'start', 'python', 'twitchImage.py'])

# Open the third program in a new window.
subprocess.Popen(['cmd', '/c', 'start', 'python', 'twitchmp3.py'])
