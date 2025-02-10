from tkinter import *
window = Tk()
def do_something():
    s = e.get()
    e.delete(0, len(s))
    x = Label(window, text=f"Hello {s}", font="Times 30")
    x.pack()
#Label--> Display something on the window
lb = Label(window, text="Hello All", font="Arial 30", fg='pink',bg='blue');
lb.pack()
#EntryField-->Used to make user enter something
e = Entry(window, font="Calibri 40", fg='blue')
e.pack()
#Button --> Used to do something upon click
b = Button(window, text="click me!", font="calibri 30", command=do_something)
b.pack()
window.title("FirstGUI")
window.mainloop()
