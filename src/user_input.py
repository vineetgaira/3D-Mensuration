import colorama
from colorama import Fore
colorama.init(autoreset=True)

from src.constants import SHAPE_INPUTS

SHAPES={
    1: "cube",
    2: "cuboid",
    3: "cylinder",
    4: "cone",
    5: "sphere",
    6: "hemisphere",
    7: "pyramid"
}

PROPERTY={
    1: "area",
    2: "volume"
}

AREA={
    1: "TSA",
    2: "CSA"
}

def get_user_choie(options: dict, prompt: str ):
    valid_choices=set(options.keys())
    while True:
        try:
            choice=int(input(Fore.BLUE+prompt))
            if choice in valid_choices:
                return options[choice]
            else:
                print(Fore.RED+"Please enter a valid choice.")
        except ValueError:
            print(Fore.RED+"Please enter a valid integer choice.")

def get_valid_dimensions(prompt):
    while True:
        try:
            value=float(input(Fore.BLUE+prompt))
            if value > 0:
                return value
            else:
                print(Fore.RED+"Please enter a positive value.")
        except ValueError:
            print(Fore.RED+"Please enter a numeric value.")

def collect_inputs(shape):
    values = {}
    for var_name, prompt in SHAPE_INPUTS[shape]:
        values[var_name] = get_valid_dimensions(prompt)
    return values