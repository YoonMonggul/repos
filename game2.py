from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1100x800")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)
def correct():
    win.destroy()

    import game3

def fail():
    win.destroy()

    import fail

lab = Label(win, text = "다음 중 틀린 그림이었던 것은?")

image1 = PhotoImage(file = "Gehenna.png")
image2 = PhotoImage(file = "Trinity.png")
image3 = PhotoImage(file = "RedWinter.png")
image4 = PhotoImage(file = "Millennium.png")

label1 = Label(win, width = 150, height = 150, image = image1)
label2 = Label(win, width = 150, height = 150, image = image2)
label3 = Label(win, width = 150, height = 150, image = image3)
label4 = Label(win, width = 150, height = 150, image = image4)

button1 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button1.config(text = "선택")
button1.config(command = fail)

button2 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button2.config(text = "선택")
button2.config(command = fail)

button3 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button3.config(text = "선택")
button3.config(command = correct)

button4 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button4.config(text = "선택")
button4.config(command = fail)

lab.pack()
label1.place(x = 200 ,y = 250)
label2.place(x = 400 ,y = 250)
label3.place(x = 600 ,y = 250)
label4.place(x = 800 ,y = 250)

button1.place(x = 220 ,y = 450)
button2.place(x = 420 ,y = 450)
button3.place(x = 620 ,y = 450)
button4.place(x = 820 ,y = 450)

win.mainloop()
