import os
import sys
import time

os.system('clear')
if os.geteuid() != 0:
    exit("You need to have root privileges to run the setup"
    "\nPlease try again, this time using 'su -', and entering your root password"
    '\nExiting the Program')

os.system('pip3 install colorama')
os.system('pip3 install pyfiglet')

print("All requirements have been installed successfully, you can now exit this program and run the 'main.py' script.")
time.sleep(100)
