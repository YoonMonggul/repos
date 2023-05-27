from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1200x800")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)
def correct():
    win.destroy()

    import game4

def fail():
    win.destroy()

    import fail

lab = Label(win, text = "다음 중 틀린 그림이었던 것은?")

image1 = PhotoImage(file = "brown.png")
image2 = PhotoImage(file = "yellow.png")
image3 = PhotoImage(file = "white.png")

label1 = Label(win, width = 150, height = 150, image = image1)
label2 = Label(win, width = 150, height = 150, image = image2)
label3 = Label(win, width = 150, height = 150, image = image3)

button1 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button1.config(text = "선택")
button1.config(command = fail)

button2 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button2.config(text = "선택")
button2.config(command = fail)

button3 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button3.config(text = "선택")
button3.config(command = correct)

lab.pack()
label1.place(x = 250 ,y = 250)
label2.place(x = 550 ,y = 250)
label3.place(x = 850 ,y = 250)

button1.place(x = 270 ,y = 450)
button2.place(x = 570 ,y = 450)
button3.place(x = 870 ,y = 450)

win.mainloop()
