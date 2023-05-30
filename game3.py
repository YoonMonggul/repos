from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1000x800")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)
def correct():
    win.destroy()

    import game4

def fail():
    win.destroy()

    import fail

canvas = Canvas(win, width = 2560, height = 1440)

BGA = PhotoImage(file = "image3.png")
canvas.create_image(1280, 720, image = BGA)

lab = Label(win, text = "다음 중 틀린 그림이었던 것은?")

image1 = PhotoImage(file = "brown.png")
image2 = PhotoImage(file = "yellow.png")
image3 = PhotoImage(file = "white.png")

canvas.create_image(200, 400, image = image1)
canvas.create_image(500, 400, image = image2)
canvas.create_image(800, 400, image = image3)

button1 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button1.config(text = "선택")
button1.config(command = fail)

button2 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button2.config(text = "선택")
button2.config(command = fail)

button3 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button3.config(text = "선택")
button3.config(command = correct)

canvas.pack()

lab.place(x = 300, y = 100)



button1.place(x = 150 ,y = 500)
button2.place(x = 450 ,y = 500)
button3.place(x = 750 ,y = 500)

win.mainloop()
