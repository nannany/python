from tkinter import *


def count_text(event):
    s = main_text.get(1.0, END)
    info_label.config(text="{0}letters".format(len(s)))


root = Tk()
root.title("text counter")

main_text = Text(root)
main_text.bind("<Key>", count_text)
main_text.pack()

info_label = Label(root)
info_label.pack()

root.mainloop()
