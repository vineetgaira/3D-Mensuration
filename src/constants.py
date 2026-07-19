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

SHAPE_INPUTS = {
    "cube":       [("side", "Enter side length: ")],
    "cuboid":     [("length", "Enter length: "), ("width", "Enter width: "), ("height", "Enter height: ")],
    "cylinder":   [("radius", "Enter radius: "), ("height", "Enter height: ")],
    "cone":       [("radius", "Enter radius: "), ("height", "Enter height: ")],
    "sphere":     [("radius", "Enter radius: ")],
    "hemisphere": [("radius", "Enter radius: ")],
    "pyramid":    [("base_area", "Enter base area: "), ("height", "Enter height: "), ("perimeter", "Enter perimeter of base:")],
}

import math


VOLUME_FORMULAS = {
    "cube":       lambda v: v["side"] ** 3,
    "cuboid":     lambda v: v["length"] * v["width"] * v["height"],
    "cylinder":   lambda v: math.pi * v["radius"] ** 2 * v["height"],
    "cone":       lambda v: (1/3) * math.pi * v["radius"] ** 2 * v["height"],
    "sphere":     lambda v: (4/3) * math.pi * v["radius"] ** 3,
    "hemisphere": lambda v: (2/3) * math.pi * v["radius"] ** 3,
    "pyramid":    lambda v: (1/3) * v["base_area"] * v["height"],
}


AREA_FORMULAS = {
    "cube": {
        "TSA": lambda v: 6 * v["side"] ** 2,
        "CSA": lambda v: 4* v["side"]**2,
    },
    "cuboid": {
        "TSA": lambda v: 2 * (v["length"]*v["width"] + v["width"]*v["height"] + v["height"]*v["length"]),
        "CSA": lambda v: 2 * (v["height"]*v["width"] + v["height"]*v["length"])
    },
    "cylinder": {
        "CSA": lambda v: 2 * math.pi * v["radius"] * v["height"],
        "TSA": lambda v: 2 * math.pi * v["radius"] * (v["radius"] + v["height"]),
    },
    "cone": {
        "CSA": lambda v: math.pi * v["radius"] * v["slant_height"],
        "TSA": lambda v: math.pi * v["radius"] * (v["radius"] + v["slant_height"]),
    },
    "sphere": {
        "CSA": lambda v: 4 * math.pi * v["radius"] ** 2,
        "TSA": lambda v: 4 * math.pi * v["radius"] ** 2,   
    },
    "hemisphere": {
        "CSA": lambda v: 2 * math.pi * v["radius"] ** 2,
        "TSA": lambda v: 3 * math.pi * v["radius"] ** 2,
    },
    "pyramid": {
        "TSA": lambda v: v["base_area"] + (1/2) * v["perimeter"] * v["height"] ,
        "CSA": lambda v: (1/2) * v["perimeter"] * v["height"] 
    }
}