#!/usr/bin/python3

import os
import sys
import shutil
help ='''
    Welcome to NUTILS
    --help or -h -----        ------(Help for the commands)
    clear        -----        ------(clears the terminal)
    copy <file1> <file2>      ------(clears the terminal)
    rmdir <dirname>           ------(remove a directory)
    '''
print(help)
while(1):
    key_input = input("     Command: ")
    if(key_input == 'pwd'):
        currentDir = os.getcwd()
        print(currentDir)
    if(key_input == '-h'):
        print(help)
    if(key_input == 'exit'):
        print("     Bye! take care\n")
        sys.exit(1)
    if(key_input == 'clear'):
        os.system('clear')
    if(key_input == 'copy'):
        file1 = input('File 1: ')
        file2 = input('File 2: ')
        shutil.copyfile(file1,file2)
    if(key_input == 'copy'):
        file1 = input('File 1: ')
        file2 = input('File 2: ')
        shutil.copy(file1,file2)
