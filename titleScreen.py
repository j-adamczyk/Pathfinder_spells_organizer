from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import os

import characterScreen

BG_COLOR = 'grey11'
BUTTON_COLOR = 'DarkOrange3'
ON_CLICK_COLOR = 'DarkOrange4'
WIDTH, HEIGHT = 550, 550
BUTTON_Y = 400
window = None
widgets = []


def char_button_click():
    global widgets, window
    
    characterScreen.display(window)


def window_init():
    global window
    window = Tk()

    window.geometry("600x550")
    window.title("PF spells organizer")
    window.configure(bg=BG_COLOR)

    return window


def create_char_button(window, FONT, character, row, column, text):
    global widgets
    char_button = Button(window,
                         text=text,
                         font=FONT,
                         width=20,
                         padx=10,
                         bg=BUTTON_COLOR,
                         activebackground=ON_CLICK_COLOR,
                         highlightthickness=0,
                         command=char_button_click
    )
    char_button.place(x=50, y=120 + row * 50,)

    edit_button = Button(window,
                         text='+',
                         font=FONT,
                         width=5,
                         padx=0,
                         bg=BUTTON_COLOR,
                         activebackground=ON_CLICK_COLOR,
                         highlightthickness=0
                         )
    edit_button.place(x=300, y=120 + row * 50, )
    widgets += [char_button]
    widgets += [edit_button]


def display():
    global window, widgets
    # window initialization
    window = window_init()
    FONT = font.Font(family='Trebuchet MS')

    img = ImageTk.PhotoImage(Image.open("title_image.png"))

    title = Label(window,
                  image=img,
                  bg=BG_COLOR, )
    title.place(x=50, y=10)
    widgets += [title]
    # Add a canvas in that frame

    char_filter = IntVar()

    create_char_button(window, FONT, None, 1, 0, 'Sorcerer lvl.8')
    create_char_button(window, FONT, None, 2, 0, 'war priest halo')

    create_button = Button(window,
                           text='Create new character',
                           font=FONT,
                           width=26,
                           padx=10,
                           bg=BUTTON_COLOR,
                           activebackground=ON_CLICK_COLOR,
                           )
    create_button.place(x=50, y=400, )
    widgets += [create_button]
    window.mainloop()
