import colorama 
from colorama import Fore
colorama.init(autoreset=True)
from src.ascii_art import welcome_menu, selection_menu, properties_menu, area_type, SHAPE_DICT

def welcome():
    print(Fore.LIGHTCYAN_EX+welcome_menu)
    
def select_shape():
      
  print(Fore.LIGHTCYAN_EX+selection_menu)

def show_shape(shape):

   print(Fore.LIGHTCYAN_EX+SHAPE_DICT[shape])

def select_properties():
   
   print(Fore.LIGHTCYAN_EX+properties_menu)

def select_area_type():
   print(Fore.LIGHTCYAN_EX+area_type)

