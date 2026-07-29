WINDOW_TITLE = "Unit Converter"

BACKGROUND = "#2C3E50"
TEXT_COLOR = "white"

FONT_TITLE = ("Arial", 18, "bold")
FONT_NORMAL = ("Arial", 12)

CONVERSIONS = {
    ("Miles", "Kilometers"): lambda x: x * 1.60934,
    ("Kilometers", "Miles"): lambda x: x / 1.60934,

    ("Celsius", "Fahrenheit"): lambda x: (x * 9 / 5) + 32,
    ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5 / 9,

    ("Kilograms", "Pounds"): lambda x: x * 2.20462,
    ("Pounds", "Kilograms"): lambda x: x / 2.20462,

    ("Centimeters", "Inches"): lambda x: x / 2.54,
    ("Inches", "Centimeters"): lambda x: x * 2.54,
}