from tkinter import *

win = Tk()
win.title("순천향에서 살아남기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

lab = Label(win)
lab.config(text = "순천향에서 살아남기")

def start():
    win.destroy()

    import game1

btn = Button(win)
btn.config(command = start)
btn.config(text = "시작버튼")
btn.config(width = 10)

image = PhotoImage(file = "start.png")

Label = Label(win, width = 400, height = 500, image = image)
Label.pack()
lab.pack()
btn.pack()
win.mainloop()