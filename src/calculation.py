from src.constants import VOLUME_FORMULAS, AREA_FORMULAS

def calculate_volume(shape, values):
    return VOLUME_FORMULAS[shape](values)

def calculate_area(shape,area_type, values):
    return AREA_FORMULAS[shape][area_type](values)


