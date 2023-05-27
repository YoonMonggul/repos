from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1200x800")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)

def start():
    win.destroy()

    import game2

lab = Label(win, text = "총 3개의 틀린 점이 있습니다. 잘 찾아보세요!")
lab2 = Label(win, text = "잘 기억하세요! 그 다음 정답 버튼을 눌러주세요.")

button = Button(win, overrelief = "solid", width = 10, repeatdelay=1000, repeatinterval=100)
button.config(text = "정답")
button.config(command = start)

image = PhotoImage(file = "image.png")
label = Label(win, width = 1200, height = 600, image = image)


lab.pack()
lab2.pack()
label.pack()
button.pack(side = "bottom", pady = 30)

win.mainloop()
