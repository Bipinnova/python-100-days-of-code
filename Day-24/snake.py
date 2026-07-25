from turtle import Turtle

from settings import (
    STARTING_POSITIONS,
    MOVE_DISTANCE,
    UP,
    DOWN,
    LEFT,
    RIGHT,
)


class Snake:
    """
    Handles everything related to the snake.
    """

    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    # -------------------------
    # Snake Creation
    # -------------------------

    def create_snake(self):
        """Create the initial snake."""
        self.segments.clear()

        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.segments[0]

    def add_segment(self, position):
        """Add one body segment."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        segment.goto(position)

        self.segments.append(segment)

    # -------------------------
    # Movement
    # -------------------------

    def move(self):
        """Move the snake forward."""

        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    # -------------------------
    # Growth
    # -------------------------

    def extend(self):
        """Increase snake length."""

        self.add_segment(self.segments[-1].position())

    # -------------------------
    # Direction Controls
    # -------------------------

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # -------------------------
    # Reset
    # -------------------------

    def reset(self):
        """
        Remove old snake and create a new one.
        """

        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()

        self.create_snake()