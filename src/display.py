import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from src.ascii_art import welcome_menu, selection_menu, properties_menu, area_type, SHAPE_DICT

def welcome():
    print(Fore.LIGHTBLUE_EX+welcome_menu)
    
def select_shape():
      
  print(Fore.LIGHTCYAN_EX+selection_menu)

def show_shape(shape):

   print(Fore.LIGHTRED_EX+SHAPE_DICT[shape])

def select_properties():
   
   print(Fore.LIGHTYELLOW_EX+properties_menu)

def select_area_type():
   print(Fore.LIGHTGREEN_EX+area_type)

