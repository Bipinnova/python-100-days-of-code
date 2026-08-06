from tkinter import *
import pandas
import random
from gtts import gTTS
import pygame
import os

BACKGROUND_COLOR = "#B1DDC6"
pygame.mixer.init()
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/hindi_english.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def speak(text, language):
    """
    language:
    hi -> Hindi
    en -> English
    """
    try:
        filename = "temp_voice.mp3"

        # Stop current speech if already playing
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        if os.path.exists(filename):
            try:
                os.remove(filename)
            except PermissionError:
                pass

        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    except Exception as e:
        print("Speech Error:", e)
        



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
    # Speak Hindi
    speak(current_card["Hindi"], "hi")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    speaker_button.config(command=lambda: speak(current_card["Hindi"], "hi"))


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

    # Speak English
    speak(current_card["English"], "en")
    speaker_button.config(command=lambda: speak(current_card["English"], "en"))


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

speaker_img = PhotoImage(file="images/speaker.png")

speaker_button = Button(
    window,
    image=speaker_img,
    borderwidth=0,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=lambda: speak(current_card["Hindi"], "hi")
)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

speaker_button.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()



