from tkinter import *

win = Tk()
win.title("틀린논문찾기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

canvas = Canvas(win, width = 2560, height = 1440)

BGA = PhotoImage(file = "image3.png")
canvas.create_image(1280, 720, image = BGA)

lab = Label(win)
lab.config(text = "틀린논문찾기")

def start():
    win.destroy()

    import help

button1 = Button(win)
button1.config(command = start)
button1.config(text = "시작버튼")
button1.config(width = 10)

image = PhotoImage(file = "start.png")

canvas.create_image(520, 300, image = image)

canvas.pack()
lab.place(x = 420, y = 100)
button1.place(x = 410, y = 500)
win.mainloop()