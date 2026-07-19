<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                     WELCOME TO 3D MENSURATION                            ║
║                     ────────────────────────                             ║
║                  volumes • surface areas • solids                        ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════╝

   CUBE                CUBOID              CYLINDER            CONE
   +------+            +----------+          _.-''-._            /\
  /      /|           /          /|       .-'  ░░░░   '-.       /  \
 +------+ |          +----------+ |      |  ░▓▓▓▓▓▓░░    |     / ░░ \
 |  ▓▓  | +          |    ▓▓▓   | +      |  ░▓▓▓▓▓▓░░    |    /▓▓▓▓▓▓\
 |      |/           |          |/        \  ░░░░░░    /    /████████\
 +------+             +----------+           '-.._..-'      \________/
```

### A Python CLI tool for calculating the Volume and Surface Area of 3D solids

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Colorama](https://img.shields.io/badge/Colorama-Terminal%20Styling-FFD43B?style=for-the-badge)](https://pypi.org/project/colorama/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Practice Project](https://img.shields.io/badge/Type-Learning%20Project-blueviolet?style=for-the-badge)](#)

</div>

---

## 📖 About

**3D Mensuration** is a command-line calculator that walks a user through selecting a **3D shape**, choosing whether they want its **Area** or **Volume**, and — for shapes that have one — picking between **Total Surface Area (TSA)** and **Curved/Lateral Surface Area (CSA)**. It then collects the required measurements and returns the calculated result.

This project was built as a **learning exercise** to practice:
- Structuring a CLI application around **data-driven design** (dictionaries mapping shapes → formulas) instead of repetitive per-shape functions
- Writing **reusable, generic input-validation functions**
- Applying **`lambda` functions** for compact, table-driven formula lookups
- Designing a clean, modular menu-navigation flow

> ⚠️ This is a self-directed practice project, not a production tool. Contributions, feedback, and suggestions are welcome as part of the learning process!

---

## 🎬 Preview

```
$ python main.py

╔══════════════════════════════════════════════════════════════════════════╗
║                     WELCOME TO 3D MENSURATION                            ║
╚══════════════════════════════════════════════════════════════════════════╝

Select a shape:
  1. Cube
  2. Cuboid
  3. Cylinder
  4. Cone
  5. Sphere
  6. Hemisphere
  7. Pyramid
Enter your choice: 3

Select area or volume:
  1. Area
  2. Volume
Enter your choice: 1

Select area type:
  1. TSA
  2. CSA
Enter your choice: 2

Enter radius: 7
Enter height: 10

CSA: 439.82
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧊 **7 Solids Supported** | Cube, Cuboid, Cylinder, Cone, Sphere, Hemisphere, Pyramid |
| 📐 **Area & Volume** | Calculates both, with TSA/CSA distinction where geometrically valid |
| 🧠 **Shape-Aware Menus** | Only shows CSA as an option for shapes that actually have a curved surface |
| 🔁 **Reusable Input Engine** | One generic `get_user_choice()` and `get_positive_float()` power every menu and prompt |
| 🗂️ **Data-Driven Formulas** | Formulas stored in dictionaries of `lambda` functions, not hardcoded per-shape logic |
| ✅ **Input Validation** | Rejects non-numeric and non-positive values with clear retry prompts |
| 🎨 **Styled Terminal Output** | ASCII art banners and `colorama`-powered coloring |

---

## 🧮 Supported Shapes & Formulas

| Shape | Volume | TSA | CSA |
|---|---|---|---|
| **Cube** | a³ | 6a² | — |
| **Cuboid** | l·w·h | 2(lw + wh + hl) | — |
| **Cylinder** | πr²h | 2πr(r + h) | 2πrh |
| **Cone** | ⅓πr²h | πr(r + l) | πrl |
| **Sphere** | (4/3)πr³ | 4πr² | 4πr² |
| **Hemisphere** | (2/3)πr³ | 3πr² | 2πr² |
| **Pyramid** | ⅓ × base area × h | base area + lateral area | — |

> Cube, Cuboid, and Pyramid have no CSA — they're made entirely of flat faces, so only TSA is meaningful.

---

## 🗂️ Project Structure

```
3D-Mensuration/
│
├── main.py                # Entry point — runs the menu loop
│
├── src/
│   ├── banner.py           # ASCII art banners & welcome screen
│   ├── registry.py         # SHAPES, PROPERTY, AREA, SHAPE_REGISTRY dicts
│   ├── formulas.py         # VOLUME_FORMULAS & AREA_FORMULAS (lambda-based)
│   ├── input_handler.py    # get_user_choice(), get_positive_float(), collect_inputs()
│   └── calculator.py       # calculate_volume(), calculate_area()
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```
   ┌─────────────┐     ┌──────────────┐     ┌───────────────┐
   │ Select Shape│ ──▶ │ Area / Volume│ ──▶ │  TSA / CSA     │
   └─────────────┘     └──────────────┘     │ (if applicable)│
                                             └───────┬────────┘
                                                     ▼
                                          ┌────────────────────┐
                                          │  Collect Dimensions │
                                          └──────────┬──────────┘
                                                     ▼
                                          ┌────────────────────┐
                                          │  Lookup & Calculate │
                                          │ (dict + lambda)     │
                                          └──────────┬──────────┘
                                                     ▼
                                          ┌────────────────────┐
                                          │   Display Result    │
                                          └────────────────────┘
```

### Core Design: Data Over Duplication

Rather than writing a separate function per shape, the project centers on **dictionaries that map shape names directly to formulas and input prompts**:

```python
VOLUME_FORMULAS = {
    "cube":     lambda v: v["side"] ** 3,
    "cylinder": lambda v: math.pi * v["radius"] ** 2 * v["height"],
    ...
}
```

Adding a new shape means adding one dictionary entry — not writing a new function from scratch.

---

## 🔍 Function Breakdown

| Function | Purpose |
|---|---|
| `get_user_choice(options, prompt)` | Generic numbered-menu handler; validates input against any dict of options |
| `get_positive_float(prompt)` | Validates numeric, positive dimension input |
| `collect_inputs(shape, mode)` | Gathers only the measurements needed for the selected shape + calculation type |
| `calculate_volume(shape, values)` | Looks up and runs the correct volume formula |
| `calculate_area(shape, area_type, values)` | Looks up and runs the correct TSA/CSA formula |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/vineetgaira/3D-Mensuration.git
cd 3D-Mensuration

# Install dependencies
pip install -r requirements.txt

# Run the program
python main.py
```

---

## 🎯 Learning Goals

- [x] Replace repetitive per-shape functions with a single generic input handler
- [x] Use `lambda` functions inside dictionaries for compact formula lookups
- [x] Build shape-aware menus (e.g. hide CSA for shapes without a curved surface)
- [ ] Add unit conversion support (cm ↔ m ↔ inches)
- [ ] Add a history log of past calculations
- [ ] Write unit tests for each formula

---

## 🧑‍💻 Author

**Vineet Gaira**
GitHub: [@vineetgaira](https://github.com/vineetgaira)

---

<div align="center">

*"Measure twice, code once."* 📐

</div>
