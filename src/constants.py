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
    "pyramid":    [("base_area", "Enter base area: "), ("height", "Enter height: ")],
}