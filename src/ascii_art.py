cube=r"""
CUBE
        +----------+
       /          /|
      /          / |
     /          /  |
    +----------+   |
    |          |   |
    |    ▓▓▓   |   +
    |   ▓▓▓▓   |  /
    |    ▓▓    | /
    |          |/
    +----------+

    6 equal square faces
    12 edges, 8 vertices
    All face angles are 90°
    Volume = a³ | Surface Area = 6a²
"""

cuboid=r"""
CUBOID
        +----------------+
       /                /|
      /                / |
     /                /  |
    +----------------+   |
    |                |   |
    |     ▓▓▓▓▓      |   +
    |    ▓▓▓▓▓▓      |  /
    |                | /
    |                |/
    +----------------+

    6 rectangular faces (opposite pairs equal)
    12 edges, 8 vertices
    Also called a rectangular prism
    Volume = l·w·h | Surface Area = 2(lw+wh+hl)
"""

cylinder=r"""

CYLINDER
        _.-''''''-._
     .-'  ░░░░░░░░  '-.
    /   ░░░░░░░░░░░░   \
   |   ░░░░░░░░░░░░░░   |
   |                    |
   |     ▓▓▓▓▓▓▓▓       |
   |    ▓▓▓▓▓▓▓▓▓▓      |
   |                    |
    \                  /
     '-.            .-'
        '-.._____.-'

    2 parallel circular bases + 1 curved lateral surface
    No vertices, 2 circular edges
    Volume = πr²h
    Surface Area = 2πr² + 2πrh

"""

cone=r"""

CONE
              /\
             /  \
            /    \
           / ░░░░ \
          /  ░░░░  \
         /   ░░░░   \
        /  ▓▓▓▓▓▓▓▓  \
       / ▓▓▓▓▓▓▓▓▓▓▓▓ \
      /_________________\
      \_________________/
       '-.._________..-'

    1 circular base + 1 curved surface tapering to an apex
    1 vertex, 1 circular edge
    Volume = (1/3)πr²h
    Surface Area = πr² + πrl (l = slant height)

"""

sphere=r"""

SPHERE
           _.-'''''-._
        .-'   ░░░░░    '-.
      .'   ░░▓▓▓▓▓▓░░     '.
     /   ░▓▓▓████▓▓▓░       \
    |   ░▓▓██████▓▓░         |
    |   ░▓▓▓████▓▓▓░         |
     \   ░░▓▓▓▓▓▓░░         /
      '.    ░░░░░        .'
        '-._         _.-'
            '''''''''

    Perfectly round; every surface point equidistant from center
    No edges, no vertices, no flat faces
    Volume = (4/3)πr³ | Surface Area = 4πr²
    Shading shows light source (upper-left) for the illusion of curvature
"""

hemisphere=r"""
HEMISPHERE
           _.-'''''-._
        .-'   ░░░░░    '-.
      .'   ░░▓▓▓▓▓▓░░     '.
     /   ░▓▓▓████▓▓▓░       \
    |___░▓▓██████▓▓░________|
    |________________________|
     \______________________/

    Half of a sphere, cut through the center
    1 flat circular face + 1 curved surface
    Volume = (2/3)πr³
    Surface Area = 3πr² (2πr² curved + πr² flat)


"""
pyramid=r"""

PYRAMID
                /\
               /  \
              / ░░ \
             /  ░░   \
            / ▓▓▓▓    \
           /  ▓▓▓▓▓    \
          / ████████    \
         /  ██████████   \
        /___________ _____\
       /_______________ ___\

    1 polygonal base + triangular faces meeting at an apex
    Square base: 5 faces, 8 edges, 5 vertices
    Volume = (1/3) × base area × height
    Surface Area = base area + sum of triangular faces


"""

SHAPE_DICT={
  "cube" : cube,
  "cuboid" : cuboid,
  "cylinder" : cylinder,
  "cone" : cone,
  "sphere": sphere,
  "hemisphere": hemisphere,
  "pyramid": pyramid
}

welcome_menu=r"""
          
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║                     WELCOME TO 3D MENSURATION                            ║
║                     ────────────────────────                             ║
║                  volumes • surface areas • solids                        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝

   CUBE                CUBOID              CYLINDER            CONE
   +------+            +----------+          _.-''-._            /\
  /      /|           /          /|       .-'  ░░░░   '-.       /  \
 +------+ |          +----------+ |      |  ░▓▓▓▓▓▓░░    |     / ░░ \
 |  ▓▓  | +          |    ▓▓▓   | +      |  ░▓▓▓▓▓▓░░    |    /▓▓▓▓▓▓\
 |      |/           |          |/        \  ░░░░░░    /    /████████\
 +------+             +----------+           '-.._..-'      \________/


   SPHERE             HEMISPHERE           PYRAMID
     _.-'''-._          _.-'''-._               /\
   .'  ░░▓▓▓░  '.      /  ░▓▓▓▓  \             /  \
  |  ░▓▓███▓▓░   |    |░▓▓█████▓▓░|           / ░░ \
  |  ░▓▓███▓▓░   |    |___________|          /▓▓▓▓▓▓\
   '.  ░░▓▓░░  .'     |___________|         /████████\
     '-.....-'                             /__________\
     
      >> Press ENTER to continue to selection menu
"""

selection_menu=r""" 
╔══════════════════════════════════════════════════════════════════════════╗
║  Select a shape from the menu below to explore its formulas & properties ║
╚══════════════════════════════════════════════════════════════════════════╝
  

  1. CUBE               2. CUBOID             3. CYLINDER       4. CONE
   +------+            +----------+          _.-''-._            /\
  /      /|           /          /|       .-'  ░░░░   '-.       /  \
 +------+ |          +----------+ |      |  ░▓▓▓▓▓▓░░    |     / ░░ \
 |  ▓▓  | +          |    ▓▓▓   | +      |  ░▓▓▓▓▓▓░░    |    /▓▓▓▓▓▓\
 |      |/           |          |/        \  ░░░░░░    /    /████████\
 +------+             +----------+           '-.._..-'      \________/


   5. SPHERE           6. HEMISPHERE         7. PYRAMID
     _.-'''-._          _.-'''-._               /\
   .'  ░░▓▓▓░  '.      /  ░▓▓▓▓  \             /  \
  |  ░▓▓███▓▓░   |    |░▓▓█████▓▓░|           / ░░ \
  |  ░▓▓███▓▓░   |    |___________|          /▓▓▓▓▓▓\
   '.  ░░▓▓░░  .'     |___________|         /████████\
     '-.....-'                             /__________\
        
  """

properties_menu=r"""

╔═════════════════════════════╗
║  Select a property to find  ║
╚═════════════════════════════╝

██╗      █████╗ ██████╗ ███████╗ █████╗ 
███║     ██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚██║     ███████║██████╔╝█████╗  ███████║
 ██║     ██╔══██║██╔══██╗██╔══╝  ██╔══██║
 ███║    ██║  ██║██║  ██║███████╗██║  ██║
 ╚══╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

 ██████╗  ██╗   ██╗ ██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗
╚════██╗ ██║   ██║██╔═══██╗██║     ██║   ██║████╗ ████║██╔════╝
 █████╔╝ ██║   ██║██║   ██║██║     ██║   ██║██╔████╔██║█████╗  
██╔═══╝  ╚██╗ ██╔╝██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══╝  
███████╗  ╚████╔╝ ╚██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║███████╗
╚══════╝   ╚═══╝   ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
"""

area_type=r"""

╔═══════════════════════════╗
║  Select the area to find  ║
╚═══════════════════════════╝


░▓▓▓▓▓▓▓▓▓▓▓▓▓░   ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
▓ 1. TOTAL SA ▓   ▓ 2. CURVED/LATERAL ▓
░▓▓▓▓▓▓▓▓▓▓▓▓▓░   ▓        SA         ▓
                  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
                  
                  """