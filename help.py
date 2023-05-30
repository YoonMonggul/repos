from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1024x768")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

def start():
    win.destroy()

    import game1

canvas = Canvas(win, width = 2560, height = 1440)

BGA = PhotoImage(file = "image3.png")
canvas.create_image(1280, 720, image = BGA)

label1 = Label(win, text = "게임 하는 법")

label2 = Label(win, text = "먼저 두 개의 논문이 제시됩니다.")
label3 = Label(win, text = "두 논문 중 다른 부분을 잘 기억해주세요.")
label4 = Label(win, text = "30초가 지나면 다음 화면으로 넘어가고")
label5 = Label(win, text = "바로 문제가 출제되니 빠르고 정확하게 기억하세요!")

button1 = Button(win, overrelief = "solid", width = 10, repeatdelay=1000, repeatinterval=100)
button1.config(text = "시작하기")
button1.config(command = start)

canvas.pack()

label1.place(x = 420, y = 100)
label2.place(x = 270, y = 200)
label3.place(x = 230, y = 300)
label4.place(x = 240, y = 400)
label5.place(x = 150, y = 500)

button1.place(x = 400, y = 600)

win.mainloop()
