import colorama
from colorama import Fore
colorama.init(autoreset=True)
from src.display import welcome, select_shape, select_properties, select_area_type,show_shape
from src.user_input import get_user_choie, collect_inputs
from src.utils import clear_screen
from src.calculation import calculate_volume,calculate_area
from src.constants import SHAPES, AREA, PROPERTY


def start_programme():
    welcome()
    while True:
        select_shape()
        shape=get_user_choie(SHAPES, "Enter your choice: ")
        show_shape(shape)
        values=collect_inputs(shape)
        select_properties()
        prop_choice=get_user_choie(PROPERTY, "Enter your choice: ")
        if prop_choice=="area":
            select_area_type()
            area_type=get_user_choie(AREA, "Enter your choice: ")
            area=calculate_area(shape,area_type,values)
            if area_type=="TSA":
                print(Fore.GREEN+f"Total Surface Area: {area:.4f}")
            else:
                print(Fore.GREEN+f"Curved/Lateral Surface Area: {area:.4f}")
        else:
            volume=calculate_volume(shape,values)
            print(Fore.GREEN+f"Volume: {volume:.3f}")
        


