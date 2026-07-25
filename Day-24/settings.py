# ==============================
# Game Window Settings
# ==============================

SCREEN_WIDTH = 680
SCREEN_HEIGHT = 680
BACKGROUND_COLOR = "#111111"
WINDOW_TITLE = "Professional Snake Game"

# ==============================
# Snake Settings
# ==============================

MOVE_DISTANCE = 20

STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0),
]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# ==============================
# Speed Settings
# ==============================

INITIAL_SPEED = 0.12
SPEED_INCREMENT = 0.005
MINIMUM_SPEED = 0.05

# ==============================
# Food Settings
# ==============================

FOOD_SIZE = 0.6

FOOD_COLORS = [
    "#ff4d4d",
    "#00ff99",
    "#00ccff",
    "#ffcc00",
    "#ff66ff",
    "#66ffff",
    "#ffffff",
    "#ff884d",
]

# ==============================
# Score Settings
# ==============================

LEVEL_UP_EVERY = 5

# ==============================
# UI Fonts
# ==============================

TITLE_FONT = ("Courier", 34, "bold")
SCORE_FONT = ("Courier", 18, "bold")
MESSAGE_FONT = ("Courier", 18, "normal")

# ==============================
# High Score File
# ==============================

HIGH_SCORE_FILE = "data.txt"