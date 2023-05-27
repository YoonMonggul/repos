from tkinter import *

win = Tk()

win.title("틀린논문찾기")
win.geometry("1200x800")
win.option_add("*Font", "맑은고딕 25")
win.resizable(False, False)
def correct():
    win.destroy()

    import success

def fail():
    win.destroy()

    import fail

lab = Label(win, text = "다음 중 틀린 그림이었던 것은?")

image1 = PhotoImage(file = "MomoFriends.png")
image2 = PhotoImage(file = "peroro.png")
image3 = PhotoImage(file = "pink.png")
image4 = PhotoImage(file = "wavecat.png")

label1 = Label(win, width = 300, height = 300, image = image1)
label2 = Label(win, width = 300, height = 300, image = image2)
label3 = Label(win, width = 300, height = 300, image = image3)
label4 = Label(win, width = 300, height = 300, image = image4)

button1 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button1.config(text = "선택")
button1.config(command = correct)

button2 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button2.config(text = "선택")
button2.config(command = fail)

button3 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button3.config(text = "선택")
button3.config(command = fail)

button4 = Button(win, overrelief = "solid", width = 5, repeatdelay=1000, repeatinterval=100)
button4.config(text = "선택")
button4.config(command = fail)

lab.pack()
label1.place(x = 50 ,y = 250)
label2.place(x = 350 ,y = 250)
label3.place(x = 650 ,y = 250)
label4.place(x = 900 ,y = 250)

button1.place(x = 150 ,y = 600)
button2.place(x = 430 ,y = 600)
button3.place(x = 770 ,y = 600)
button4.place(x = 1000 ,y = 600)

win.mainloop()
