import random
from turtle import Turtle

from settings import (
    FOOD_SIZE,
    FOOD_COLORS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class Food(Turtle):
    """
    Represents the food that the snake eats.
    """

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.speed("fastest")

        self.shapesize(
            stretch_wid=FOOD_SIZE,
            stretch_len=FOOD_SIZE
        )

        self.new_food()

    # ---------------------------------
    # Generate New Food
    # ---------------------------------

    def new_food(self):
        """
        Move food to a random location
        and assign a random colour.
        """

        margin = 40

        random_x = random.randrange(
            -SCREEN_WIDTH // 2 + margin,
            SCREEN_WIDTH // 2 - margin,
            20
        )

        random_y = random.randrange(
            -SCREEN_HEIGHT // 2 + margin,
            SCREEN_HEIGHT // 2 - margin,
            20
        )

        self.color(random.choice(FOOD_COLORS))

        self.goto(random_x, random_y)