from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

label1 = Label(win, text = "졸업에 실패하셨습니다!")
label2 = Label(win, text = "당신은 재수강입니다")

image1 = PhotoImage(file = "start.png")
label3 = Label(win, image = image1)


label1.place(x = 340, y = 100)
label2.place(x = 360, y = 200)
label3.place(x = 450, y = 400)

win.mainloop()
