# import colorgram

# colors = colorgram.extract('hirst_img.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)


tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

color_list = [
    (46, 92, 144),
    (170, 13, 26),
    (34, 44, 62),
    (141, 80, 44),
    (228, 154, 7),
    (161, 57, 88),
    (211, 162, 101),
    (37, 144, 46),
    (68, 34, 47),
    (235, 219, 63),
    (225, 223, 4),
    (48, 45, 93),
    (22, 51, 47),
    (50, 40, 36),
    (88, 195, 171),
    (117, 162, 171),
    (247, 90, 16),
    (18, 96, 49),
    (211, 56, 76),
    (155, 23, 19),
    (187, 143, 156),
    (60, 167, 91),
    (46, 149, 196),
    (226, 177, 167),
    (163, 209, 182),
    (227, 171, 180),
]

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
