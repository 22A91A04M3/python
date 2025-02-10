from tkinter import *
window = Tk()
def do_something():
    s = e.get()
    e.delete(0, len(s))
    
e = Entry(window, font="Calibri 40", fg='pink')
e.pack()
e.grid(row=0, column=0, columnspan=30)

b2 = Button(window, text="7", font="Times 24", padx=80, pady=20, command=do_something)
b2.grid(row=1, column=1)

b3 = Button(window, text="8", font="Times 24", padx=80, pady=20)
b3.grid(row=1, column=2)

b4 = Button(window, text="9", font="Times 24", padx=80, pady=20)
b4.grid(row=1, column=3)

b5 = Button(window, text="4", font="Times 24", padx=80, pady=20)
b5.grid(row=2, column=1)

b6 = Button(window, text="5", font="Times 24", padx=80, pady=20)
b6.grid(row=2, column=2)

b7 = Button(window, text="6", font="Times 24", padx=80, pady=20)
b7.grid(row=2, column=3)

b8 = Button(window, text="1", font="Times 24", padx=80, pady=20)
b8.grid(row=3, column=1)

b9 = Button(window, text="2", font="Times 24", padx=80, pady=20)
b9.grid(row=3, column=2)

b10 = Button(window, text="3", font="Times 24", padx=80, pady=20)
b10.grid(row=3, column=3)

a1 = Button(window, text="0", font="Times 24", padx=80, pady=20)
a1.grid(row=4, column=1)

a2 = Button(window, text="Clear", font="Times 24", padx=160, pady=20, command=do_something)
a2.grid(row=4, column=2, columnspan=2)

a3 = Button(window, text="+", font="Times 24", padx=80, pady=20)
a3.grid(row=5, column=1)

a4 = Button(window, text="=", font="Times 24", padx=180, pady=20)
a4.grid(row=5, column=2, columnspan=2)

a5 = Button(window, text="-", font="Times 24", padx=80, pady=20)
a5.grid(row=6, column=1)

a6 = Button(window, text="x", font="Times 24", padx=80, pady=20)
a6.grid(row=6, column=2)

a7 = Button(window, text="/", font="Times 24", padx=80, pady=20)
a7.grid(row=6, column=3)

window.title("calc")
window.mainloop()
