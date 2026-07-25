import time
from turtle import Screen

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    WINDOW_TITLE,
    INITIAL_SPEED,
    SPEED_INCREMENT,
    MINIMUM_SPEED,
)

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from sound import (
    play_background,
    play_eat,
    play_game_over,
    stop_background
)


# ===========================================
# Screen
# ===========================================

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(WINDOW_TITLE)
screen.tracer(0)

# ===========================================
# Game Objects
# ===========================================

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# ===========================================
# Controls
# ===========================================

screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# ===========================================
# Game Speed
# ===========================================

game_speed = INITIAL_SPEED

# ===========================================
# Main Loop
# ===========================================
play_background()
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(game_speed)

    snake.move()

    # ==========================
    # Food Collision
    # ==========================

    if snake.head.distance(food) < 15:

        food.new_food()

        snake.extend()

        play_eat()        
        scoreboard.increase_score()

        game_speed = max(
            MINIMUM_SPEED,
            game_speed - SPEED_INCREMENT
        )

    # ==========================
    # Wall Collision
    # ==========================

    x = snake.head.xcor()
    y = snake.head.ycor()

    if (
        x > SCREEN_WIDTH / 2 - 20
        or x < -SCREEN_WIDTH / 2 + 20
        or y > SCREEN_HEIGHT / 2 - 20
        or y < -SCREEN_HEIGHT / 2 + 20
    ):

        stop_background()
        play_game_over()
        scoreboard.game_over()
        break

    # ==========================
    # Tail Collision
    # ==========================

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:

            stop_background()
            play_game_over()
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()