from src.display import welcome, select_shape, select_properties, select_area_type
from src.user_input import get_user_choie, collect_inputs
from src.utils import clear_screen
from src.calculation import properties_cube, properties_cuboid, properties_cylinder, properties_cone, properties_sphere, properties_hemisphere, properties_pyramid
from src.constants import SHAPES, AREA, PROPERTY

def start_programme():
    welcome()
    while True:
        select_shape()
        shape=get_user_choie(SHAPES, "Enter your choice: ")
        