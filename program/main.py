from colorama import *
import pyfiglet
import os
import platform
import sys
import time
import webbrowser
os.system('clear')
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script."
    "\nPlease try again, this time using 'su -', and entering your root password"
    '\nExiting the Program')

init()
asci_banner = pyfiglet.figlet_format('Nix Engine')
print(asci_banner)

print(Fore.RED + '=======================================')
print(Fore.YELLOW + 'Detected System Information')
print(Fore.GREEN + f"OS : {platform.system()}")
print(Fore.GREEN + f'Release : {platform.version()}')
print(Fore.GREEN + f'Python Version : {platform.python_version()}')
print(Fore.RED + '=======================================')

input('\nPress enter to start Menu')

# Program Menu





# Conditions
while True:
    os.system('clear')
    print(asci_banner)
    print(Fore.YELLOW + '[+] Installer Menu-------------->\n')
    print(Fore.CYAN + ' [1] Install Visual Studio Code [Type 1]')
    print(Fore.CYAN + ' [2] Install Pycharm (Community Edition)[Type 2]')
    print(Fore.CYAN + ' [3] Install Sublime Text [Type 3]')
    print(Fore.CYAN + ' [4] Install Atom [Type 4]')
    print(Fore.CYAN + ' [5] Install Python IDLE for Python3 [Type 5]')
    print(Fore.CYAN + ' [6] Install Python IDLE for Python2 [Type 6]\n')
    user_input = input('Type here>>')


    if '1' in user_input:
        print(Fore.CYAN + 'Starting Installation Process for VS Code')
        time.sleep(2)
        os.system('wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg')
        os.system('sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/')
        os.system("sudo sh -c echo deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" + '> /etc/apt/sources.list.d/vscode.list')
        os.system('sudo apt install apt-transport-https')
        os.system('sudo apt update')
        os.system('sudo apt install code')
        print(Fore.GREEN + 'Process Complete!')
        time.sleep(2)
 

    elif '2' in user_input:
        os.system('sudo apt update')
        os.system('sudo apt upgrade')
        os.system('sudo apt install snapd')
        os.system('sudo apt install core')
        os.system('sudo snap install pycharm-community --classic')
        time.sleep(2)


    elif '3' in user_input:
        os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
        os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
        os.system('sudo apt update')
        os.system('apt install sublime-text')
        time.sleep(2)


    elif '4' in user_input:
        os.system('wget https://atom.io/download/deb -O atom.deb')
        os.system('sudo dpkg -i atom.deb')
        time.sleep(2)
 

    elif '5' in user_input:
        os.system('sudo apt-get install idle3')
        time.sleep(2)


    elif '6' in user_input:
        os.system('sudo apt install idle')
        time.sleep(2)

    elif 'quit' in user_input:
        print(Fore.RED + 'Program Exitted, sorry to see you go :(')
        time.sleep(1)
        sys.exit()

    elif 'exit' in user_input:
        print(Fore.RED + 'Program Exitted, sorry to see you go :(')
        time.sleep(1)
        sys.exit()

    else:
        print('Unavailable Command!')
        time.sleep(2)

    
           









'''
user = os.getuid()
if user != 0:
    os.system('gksudo ls')
    os.system('clear')
os.system('sudo command_requiring_root')
'''
