from tkinter import *
import tkinter.font as font

import titleScreen

BG_COLOR = 'grey11'
BUTTON_COLOR = 'DarkOrange3'
ON_CLICK_COLOR = 'DarkOrange4'
TEXT_COLOR = BUTTON_COLOR
window = None


def char_button_click():
    global window

    titleScreen.display(window)


def display(w=None):
    global window
    if w is None:
        w = titleScreen.window_init()
    window = w
    FONT = font.Font(family='Trebuchet MS')

    window.grid_rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    frame_main = Frame(window, bg=BG_COLOR)
    frame_main.grid(sticky='news')

    label1 = Label(frame_main, text="Label 1", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
    label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

    name = StringVar()
    entry = Entry(frame_main, textvariable=name, bg='grey15')
    entry.grid(row=0, column=1)
    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas = Frame(frame_main)
    frame_canvas.grid(row=1, column=2, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)
    # Add a canvas in that frame
    canvas = Canvas(frame_canvas, bg="yellow")
    canvas.grid(row=0, column=0, sticky="news")

    # Link a scrollbar to the canvas
    vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

    # Create a frame to contain the buttons
    frame_buttons = Frame(canvas, bg="blue")
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
    Button(frame_main, text='back', command=char_button_click).grid(row=6, column=0, sticky=W)
    Checkbutton(frame_main, text="fire", variable=var1, bg=BG_COLOR, activeforeground=TEXT_COLOR, activebackground=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky=W)
    Checkbutton(frame_main, text="water", variable=var2, bg=BG_COLOR, activeforeground=TEXT_COLOR, activebackground=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, sticky=W)
    Checkbutton(frame_main, text="earth", variable=var3, bg=BG_COLOR, activeforeground=TEXT_COLOR, activebackground=BG_COLOR, fg=TEXT_COLOR).grid(row=4, column=0, sticky=W)
    Checkbutton(frame_main, text="air", variable=var4, bg=BG_COLOR, activeforeground=TEXT_COLOR, activebackground=BG_COLOR, fg=TEXT_COLOR).grid(row=5, column=0, sticky=W)

    control_variable = StringVar()
    OPTION_TUPLE = ("Sorcerer", "War priest", "Druid")
    optionmenu_widget = OptionMenu(frame_main, control_variable, *OPTION_TUPLE,
                                   ).grid(row=2, column=1)
    # Add 9-by-5 buttons to the frame
    rows = 9
    columns = 5
    buttons = [[Button() for j in range(columns)] for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            buttons[i][j] = Button(frame_buttons, text=("Spell {}{}".format(i, j)), bg=BG_COLOR, fg='khaki1',
                                   activebackground=BG_COLOR, activeforeground='khaki1')
            buttons[i][j].grid(row=i, column=j, sticky='news')

    # Update buttons frames idle tasks to let tkinter calculate buttons sizes
    frame_buttons.update_idletasks()



    # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
    first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
    first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
    frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                        height=first5rows_height)

    # Set the canvas scrolling region
    canvas.config(scrollregion=canvas.bbox("all"))

    # Launch the GUI
    window.mainloop()
    # char_spells_button = Radiobutton(window,
    #                                  text='abc',
    #                                  font=FONT,
    #                                  indicatoron=0,
    #                                  width=20,
    #                                  padx=20,
    #                                  variable=spell_filter,
    #                                  value=2,
    #                                  bg=BUTTON_COLOR,
    #                                  activebackground=ON_CLICK_COLOR,
    #                                  selectcolor=ON_CLICK_COLOR,
    #                                  ).grid(row=3, column=0)
