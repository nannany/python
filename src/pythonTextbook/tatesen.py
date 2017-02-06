from tkinter import *

w = Canvas(Tk(), width=900, height=400)
w.pack()

for i in range(100):
    x = i * 9
    if i % 2 == 0:
        c = "#ff0000"
    else:
        c = "#0000ff"
    w.create_line(x, 0, x, 400, fill=c)

mainloop()
