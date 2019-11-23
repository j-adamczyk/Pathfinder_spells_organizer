from tkinter import *

if __name__ == '__main__':
    window = Tk()
    window.geometry("500x500")
    window.title("PF spells organizer")

    v = IntVar()

    Label(window,
             text="""Choose a 
    programming language:""",
             justify=LEFT,
             padx=20).pack()
    Radiobutton(window,
                  text='ALL',
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable = v,
                  value = 1,
                  ).pack(anchor=W)
    Radiobutton(window,
                  text='MINE',
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable = v,
                  value = 2,
                ).pack(anchor=W)

    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)
    window.mainloop()
