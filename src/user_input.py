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

def user_select_shape():
    valid_choices={1,2,3,4,5,6,7}
    while True:
        try:
            choice=int(input("Enter your choice :"))
            if choice in valid_choices:
                return SHAPES[choice]
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid integer choice.")
    
def user_select_property():
    valid_choices={1,2}
    while True:
        try:
            property_choice=int(input("Enter your choice :"))
            if property_choice in valid_choices:
                return PROPERTY[property_choice]
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid integer choice.")

def user_select_area():
    valid_choices={1,2}
    while True:
        try:
            area_choice=int(input("Enter your choice :"))
            if area_choice in valid_choices:
                return AREA[area_choice]
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid integer choice.")


def get_dimensions(prompt):
    while True:
        try:
            value=float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive value.")
        except ValueError:
            print("Please enter a numeric value.")

def collect_inputs(shape):
    values = {}
    for var_name, prompt in SHAPE_INPUTS[shape]:
        values[var_name] = get_dimensions(prompt)
    return values