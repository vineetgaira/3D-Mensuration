import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from src.ascii_art import welcome_menu, selection_menu, properties_menu

def welcome():
    print(Fore.LIGHTBLUE_EX+welcome_menu)
    
    
def select_shape():
      
  print(Fore.LIGHTBLUE_EX+selection_menu)


def select_properties():
   
   print(Fore.LIGHTBLUE_EX+properties_menu)

