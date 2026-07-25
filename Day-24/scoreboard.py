from turtle import Turtle

from settings import (
    SCORE_FONT,
    TITLE_FONT,
    MESSAGE_FONT,
    HIGH_SCORE_FILE,
    LEVEL_UP_EVERY,
)


class Scoreboard(Turtle):
    """
    Displays score, high score, level,
    game messages and manages high score.
    """

    def __init__(self):
        super().__init__()

        self.score = 0
        self.level = 1

        self.color("white")
        self.penup()
        self.hideturtle()

        self.goto(0, 310)

        self.high_score = self.load_high_score()

        self.update()

    # ===================================
    # High Score
    # ===================================

    def load_high_score(self):
        """Read high score from file."""

        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        """Save high score."""

        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    # ===================================
    # Score Display
    # ===================================

    def update(self):
        """Refresh scoreboard."""

        self.clear()

        self.write(
            f"Score : {self.score}     "
            f"High Score : {self.high_score}     "
            f"Level : {self.level}",
            align="center",
            font=SCORE_FONT,
        )

    # ===================================
    # Score
    # ===================================

    def increase_score(self):

        self.score += 1

        self.level = (self.score // LEVEL_UP_EVERY) + 1

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.update()

    # ===================================
    # Reset
    # ===================================

    def reset(self):

        self.score = 0
        self.level = 1
        self.update()

    # ===================================
    # Messages
    # ===================================

    def show_start_screen(self):

        self.goto(0, 30)

        self.write(
            "PROFESSIONAL SNAKE GAME",
            align="center",
            font=TITLE_FONT,
        )

        self.goto(0, -20)

        self.write(
            "Press SPACE to Start",
            align="center",
            font=MESSAGE_FONT,
        )

    def show_pause(self):

        self.goto(0, 0)

        self.write(
            "GAME PAUSED",
            align="center",
            font=TITLE_FONT,
        )

        self.goto(0, -40)

        self.write(
            "Press P to Resume",
            align="center",
            font=MESSAGE_FONT,
        )

    def game_over(self):

        self.goto(0, 20)

        self.write(
            "GAME OVER",
            align="center",
            font=TITLE_FONT,
        )

        self.goto(0, -20)

        self.write(
            f"Final Score : {self.score}",
            align="center",
            font=MESSAGE_FONT,
        )