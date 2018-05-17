#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6
#=======================================================================

# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "1. Fcosiety"
    print "2. SCDL"
    print "3. Irssi"
    print "4. Msfconsole"
    print "5. wifite, fluxion"
    print "6. wifi-driver(rtl8723)"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    print "Installing!\n"
    os.chdir('/root')
    os.system("git clone https://github.com/Manisso/fsociety.git")
    os.chdir('fsociety')
    os.system("chmod +x install.sh")
    os.system("./install.sh")
    print("Installed fsociety-TOOLS")
    print ("Type python fsociety.py")
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print "SCDL (music downloader) !\n"
    os.system("pkg install python")
    os.system("pkg install python-pip")
    os.system("pip install scdl")
    print "Type scdl -l (link with song)"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
# Menu 3
def menu3():
    print "Irssi (irc client CLI)"
    os.system("pkg update ")
    os.system("pkg install irssi")
    print "TYPE irssi"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 6
def menu6():
    print "Install driver (I am not recomend install driver in first because restart system in end of install)"
    os.system("git clone https://github.com/smlinux/rtl8723de.git -b 4.11-up")
    os.system("sudo dkms add ./rtl8723de")
    os.system("sudo dkms install rtl8723de/5.1.1.8_21285.20171026_COEX20170111-1414")
    os.system("sudo depmod -a")
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
# Menu 5

def menu5():
    os.system("git clone https://github.com/FluxionNetwork/fluxion.git ")
    os.chdir("fluxion")
    print "TYPE ./fluxion.sh"
    os.chdir("-")
    os.system("wget https://raw.github.com/derv82/wifite/master/wifite.py")
    os.system("chmod +x wifite.py")
    print "TYPE ./wifite.py"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
# Menu 4
def menu4():
    print "Install MSF"
    os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \ ")
    os.system("chmod 755 msfinstall && \ ")
    print "TYPE ./msfinstall"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return



# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '9': back,
    '0': exit,

}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
