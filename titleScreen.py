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

    window.geometry("550x550")
    window.title("PF spells organizer")
    window.configure(bg=BG_COLOR)
    return window

def create_char_button(window, FONT, character):
    char_button = Button(window,
                         text='Sorcerer lvl.8',
                         font=FONT,
                         width=30,
                         padx=15,
                         bg=BUTTON_COLOR,
                         activebackground=ON_CLICK_COLOR,
                         ).grid(row=1, column=0)


def display():
    #window initialization
    window = window_init()
    FONT = font.Font(family='Trebuchet MS')

    frame_main = Frame(window, bg=BG_COLOR)
    frame_main.grid(sticky='news')
    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas = Frame(frame_main)
    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)

    scrollbar = Scrollbar(window, orient="vertical")
    scrollbar.grid(row=1, column=1, sticky='ns')
    img = ImageTk.PhotoImage(Image.open("title_image.png"))
    title = Label(window,
                  image=img,
                  bg=BG_COLOR,)
    title.place(x=0, y=10)
    title.grid(column=0, row=0)
    # Add a canvas in that frame
    canvas = Canvas(window, bg=BG_COLOR,  width=WIDTH, height=100, relief=SUNKEN)
    canvas.grid(row=1, column=0, sticky="news", ipadx=0, ipady=BUTTON_Y)

    spell_filter = IntVar()

    create_char_button(canvas, FONT, None)

    edit_button = Button(canvas,
                                     text='+',
                                     font=FONT,
                                     width=5,
                                     padx=5,
                                     bg=BUTTON_COLOR,
                                     activebackground=ON_CLICK_COLOR,
                                     ).grid(row=1, column=1,)

    create_button = Button(canvas,
                                     text='Create new character',
                                     font=FONT,
                                     width=30,
                                     padx=15,
                                     bg=BUTTON_COLOR,
                                     activebackground=ON_CLICK_COLOR,
                                     ).grid(row=2, column=0,)
    window.mainloop()