from tkinter import *

win = Tk()
win.title("순천향에서 살아남기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

lab = Label(win)
lab.config(text = "축하합니다!성공하셨습니다!")

label2 = Label(win, text = "다음 스테이지로 진행해주세요")


image = PhotoImage(file = "start.png")

Label = Label(win, width = 400, height = 500, image = image)

Label.pack()
lab.pack()
label2.pack()

win.mainloop()