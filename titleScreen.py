from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import os

BG_COLOR = 'grey11'
BUTTON_COLOR = 'DarkOrange3'
ON_CLICK_COLOR = 'DarkOrange4'
WIDTH, HEIGHT = 550, 550
BUTTON_Y = 400


def window_init():
    window = Tk()

    window.geometry("600x550")
    window.title("PF spells organizer")
    window.configure(bg=BG_COLOR)

    return window


def create_char_button(window, FONT, character, row, column):
    char_button = Button(window,
                         text='Sorcerer lvl.8',
                         font=FONT,
                         width=20,
                         padx=10,
                         bg=BUTTON_COLOR,
                         activebackground=ON_CLICK_COLOR,
                         highlightthickness=0
                         ).place(x=0, y=120 + row * 40, )
    edit_button = Button(window,
                         text='+',
                         font=FONT,
                         width=5,
                         padx=0,
                         bg=BUTTON_COLOR,
                         activebackground=ON_CLICK_COLOR,
                         highlightthickness=0
                         ).place(x=300, y=120 + row * 40, )
    # window.grid_columnconfigure(column + 1, )


def display():
    # window initialization
    window = window_init()
    FONT = font.Font(family='Trebuchet MS')

    img = ImageTk.PhotoImage(Image.open("title_image.png"))

    title = Label(window,
                  image=img,
                  bg=BG_COLOR, )
    title.place(x=50, y=10)
    # Add a canvas in that frame

    char_filter = IntVar()

    create_char_button(window, FONT, None, 1, 0)

    create_button = Button(window,
                           text='Create new character',
                           font=FONT,
                           width=20,
                           padx=10,
                           bg=BUTTON_COLOR,
                           activebackground=ON_CLICK_COLOR,
                           ).place(x=0, y=120 + 3 * 40, )
    window.mainloop()
