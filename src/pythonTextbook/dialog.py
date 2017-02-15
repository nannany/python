import tkinter.messagebox as mb

ans = mb.askyesno("question", "do you like ramen?")
if ans == True:
    mb.showinfo("agree", "me too")
else:
    mb.showinfo("really?", "unbelievable")
