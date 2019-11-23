from tkinter import *
import tkinter.font as font
BG_COLOR = 'grey11'
BUTTON_COLOR = 'DarkOrange3'
ON_CLICK_COLOR = 'DarkOrange4'

def display():
    window = Tk()
    FONT = font.Font(family='Trebuchet MS')

    window.geometry("500x500")
    window.title("PF spells organizer")
    window.configure(bg=BG_COLOR)
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)

    v = IntVar()

    level_button = Spinbox(window,
                           from_=1.0,
                           to=20.0,
                           width=5,
                           )
    level_button.pack()

    all_spells_button = Radiobutton(window,
                                    text='lorem ipsum whatever',
                                    font=FONT,
                                    indicatoron=0,
                                    width=20,
                                    padx=20,
                                    variable=v,
                                    value=1,
                                    bg=BUTTON_COLOR,
                                    activebackground=ON_CLICK_COLOR,
                                    selectcolor=ON_CLICK_COLOR,
                                    ).pack(anchor=W)
    char_spells_button = Radiobutton(window,
                                     text='abc',
                                     font=FONT,
                                     indicatoron=0,
                                     width=20,
                                     padx=20,
                                     variable=v,
                                     value=2,
                                     bg=BUTTON_COLOR,
                                     activebackground=ON_CLICK_COLOR,
                                     selectcolor=ON_CLICK_COLOR,
                                     ).pack(anchor=W)

    window.mainloop()