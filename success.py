from tkinter import *

win = Tk()
win.title("순천향에서 살아남기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

def start():
    win.destroy()

    import main  #여기에 다음게임 넣어주세요 ^^


canvas = Canvas(win, width = 2560, height = 1440)

BGA = PhotoImage(file = "image3.png")
canvas.create_image(1280, 720, image = BGA)

lab = Label(win)
lab.config(text = "축하합니다!성공하셨습니다!")

label2 = Label(win, text = "다음 스테이지로 진행해주세요")


image = PhotoImage(file = "start.png")

canvas.create_image(510, 400, image = image)


button1 = Button(win, overrelief = "solid", width = 10, repeatdelay=1000, repeatinterval=100)
button1.config(text = "넘어가기")
button1.config(command = start)


canvas.pack()

button1.place(x = 400, y = 500)
lab.place(x = 300, y = 100)
label2.place(x = 280, y = 200)

win.mainloop()