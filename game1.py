from tkinter import *
import time
count = 0
time = 0

win = Tk()

def countstart():
    global count
    global time
    count += 1
    time += 1
    labtimer["text"] = str(count) + "초"
    if time > 30:
        return start()
    win.after(1000, countstart)

win.title("틀린논문찾기")
win.geometry("1500x800")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

def start():
    win.destroy()

    import game2

canvas = Canvas(win, width = 2560, height = 1440)

image1 = PhotoImage(file = "image3.png")
canvas.create_image(1280, 720, image = image1)


quiz1 = PhotoImage(file = "quiz1.png")
label2 = Label(win, width = 600, height = 600, image = quiz1)

quiz2 = PhotoImage(file = "quiz2.png")
label3 = Label(win, width = 600, height = 600, image = quiz2)

labtimer = Label(win, width = 5, height = 2, text = "0초")

win.after(1000, countstart)


canvas.pack()
labtimer.place(x = 700, y = 350)
label2.place(x = 50, y = 100)
label3.place(x = 850, y = 100)

win.mainloop()
