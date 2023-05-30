from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

def start():
    win.destroy()

    import main

canvas = Canvas(win, width = 2560, height = 1440)

BGA = PhotoImage(file = "image3.png")
canvas.create_image(1280, 720, image = BGA)

label1 = Label(win, text = "졸업에 실패하셨습니다!")
label2 = Label(win, text = "당신은 재수강입니다")

image1 = PhotoImage(file = "start.png")
label3 = Label(win, image = image1)

button1 = Button(win, overrelief = "solid", width = 10, repeatdelay=1000, repeatinterval=100)
button1.config(text = "다시하기")
button1.config(command = start)



canvas.pack()

button1.place(x = 400, y = 550)

label1.place(x = 340, y = 100)
label2.place(x = 360, y = 200)
label3.place(x = 440, y = 300)

win.mainloop()
