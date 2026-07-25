import pygame           # type: ignore
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, "assets")


def play_background():
    pygame.mixer.music.load(os.path.join(ASSETS, "background.wav"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


def stop_background():
    pygame.mixer.music.stop()


def play_eat():
    pygame.mixer.Sound(
        os.path.join(ASSETS, "eat.wav")
    ).play()


def play_game_over():
    pygame.mixer.Sound(
        os.path.join(ASSETS, "gameover.wav")
    ).play()
