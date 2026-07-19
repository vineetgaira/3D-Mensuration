import math

def properties_cube(prop_choice, choice, a): 
     if prop_choice=="volume":
         return a*a*a
     if prop_choice=="area":
         if choice=="TSA":
             return 6*a*a
         else:
             return 4*a*a

def properties_cuboid(prop_choice,choice, l, w, h):    
    if prop_choice=="volume":
         return l*w*h
    if prop_choice=="area":
        if choice=="TSA":
            return 2(l*w + w*h + l*h)
        else:
            return 2*h(l + w)

def properties_cylinder(prop_choice, choice, r, h):

    if prop_choice=="volume":
        return math.pi*r*r*h
    if prop_choice=="area":
        if choice=="TSA":
            return 2*math.pi*r(r+h)
        else:
            return 2*math.pi*r*h

def properties_cone(prop_choice,choice, r, l):
    if prop_choice=="volume":
        return (math.pi*r*r*l)/3
    if prop_choice=="area":
        if choice=="TSA":
            return math.pi*r(r+l)
        else:
            return math.pi*r*l

def properties_sphere(prop_choice,choice, r):
    if prop_choice=="volume":
        return (4*math.pi*r*r*r)/3
    if prop_choice=="area":
        if choice=="TSA":
            return 4*math.pi*r*r
        else:
            return 4*math.pi*r*r

def properties_hemisphere(prop_choice, choice, r):
    if prop_choice=="volume":
        return (2*math.pi*r*r*r)/3
    if prop_choice=="area":
        if choice=="TSA":
            return 3*math.pi*r*r
        else:
            return 2*math.pi*r*r
        
def properties_pyramid(prop_choice, choice, a, s):
    if prop_choice=="volume":
        return (a*s)/3
    if prop_choice=="area":
        if choice=="TSA":
            return a*a+ 2*a*s
        else:
            return 2*a*s

