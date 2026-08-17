from colorama import Fore
import os 

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def show_error(prompt):
    print(prompt)