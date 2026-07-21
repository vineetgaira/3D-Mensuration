import colorama
import time
from colorama import Fore
colorama.init(autoreset=True)
from src.display import welcome, select_shape, select_properties, select_area_type,show_shape
from src.user_input import get_user_choie, collect_inputs
from src.utils import clear_screen
from src.calculation import calculate_volume,calculate_area
from src.constants import SHAPES, AREA, PROPERTY


def start_programme():
    welcome()
    time.sleep(5)
    while True:
        clear_screen()
        select_shape()
        shape=get_user_choie(SHAPES, "Enter your choice: ")
        clear_screen()
        show_shape(shape)
        values=collect_inputs(shape)
        clear_screen()
        select_properties()
        prop_choice=get_user_choie(PROPERTY, "Enter your choice: ")
        
        if prop_choice=="area":
            clear_screen()
            select_area_type()
            area_type=get_user_choie(AREA, "Enter your choice: ")
            area=calculate_area(shape,area_type,values)
            if area_type=="TSA":
                print(Fore.LIGHTGREEN_EX+f"Total Surface Area: {area:.4f}")
            else:
                print(Fore.LIGHTGREEN_EX+f"Curved/Lateral Surface Area: {area:.4f}")
        else:
            volume=calculate_volume(shape,values)
            print(Fore.LIGHTGREEN_EX+f"Volume: {volume:.3f}")
        while True:
            user_exit=input(Fore.LIGHTCYAN_EX+"Do you want to continue? y/n :").lower().strip()
            if user_exit=="y":
                break
            elif user_exit=="n":
                print(Fore.GREEN+"Thanks for being here...")
                return
            else:
                print(Fore.RED+"Please etner a y/n.")
            
        


