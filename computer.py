from tkinter import *

opset = 0
v3 = 0

def ChangeText(num):
    if int(lab["text"]) != 0:
        lab["text"] = lab["text"] + num
    else:
        lab["text"] = num

def Del():
    lab["text"] = 0

def opSet(onValue):
    global opset
    global v1
    v1 = int(lab["text"])
    btnequal.config(state="active")
    opset = int(onValue)
    lab["text"] = 0

def equal():
    global v1
    global v3
    global opset
    v2 = int(lab["text"])
    if opset == 1:
        v3 = v1 + v2
    elif opset == 2:
        v3 = v1 - v2
    elif opset == 3:
        v3 = v1 * v2
    elif opset == 4:
        v3 = v1 // v2
    lab["text"] = v3
    btnequal.config(state="disabled")

window = Tk()
window.title("Button test")
window.geometry("300x400+460+200")
window.config(bg="White")
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

lab = Label(window, text="0", justify=RIGHT, anchor=E, font="Helvetica 40 bold",background="Thistle")
lab.grid(row=0, column=0, columnspan=4, sticky=EW)

btn7 = Button(window, text="7",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('7'))
btn7.grid(row=1, column=0, sticky=NSEW)
btn8 = Button(window, text="8",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('8'))
btn8.grid(row=1, column=1, sticky=NSEW)
btn9 = Button(window, text="9",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('9'))
btn9.grid(row=1, column=2, sticky=NSEW)

btn4 = Button(window, text="4",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('4'))
btn4.grid(row=2, column=0, sticky=NSEW)
btn5 = Button(window, text="5",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('5'))
btn5.grid(row=2, column=1, sticky=NSEW)
btn6 = Button(window, text="6",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('6'))
btn6.grid(row=2, column=2, sticky=NSEW)

btn1 = Button(window, text="1",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('1'))
btn1.grid(row=3, column=0, sticky=NSEW)
btn2 = Button(window, text="2",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('2'))
btn2.grid(row=3, column=1, sticky=NSEW)
btn3 = Button(window, text="3",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('3'))
btn3.grid(row=3, column=2, sticky=NSEW)

btn0 = Button(window, text="0",font=("Helvetica", 30, "bold"), command=lambda:ChangeText('0'))
btn0.grid(row=4, column=0, sticky=NSEW)
btnequal = Button(window, text="=",font=("Helvetica", 30, "bold"),state="disabled", command=equal)
btnequal.grid(row=4, column=2, sticky=NSEW)
btnDel = Button(window, text="C",font=("Helvetica", 30, "bold"), command=Del)
btnDel.grid(row=4, column=1, sticky=NSEW)

btnadd = Button(window, text="+",font=("Helvetica", 30, "bold"), command=lambda:opSet('1'))
btnadd.grid(row=1, column=3, sticky=NSEW)
btnsub = Button(window, text="-",font=("Helvetica", 30, "bold"), command=lambda:opSet('2'))
btnsub.grid(row=2, column=3, sticky=NSEW)
btnmul = Button(window, text="x",font=("Helvetica", 30, "bold"), command=lambda:opSet('3'))
btnmul.grid(row=3, column=3, sticky=NSEW)
btndiv = Button(window, text="÷",font=("Helvetica", 30, "bold"), command=lambda:opSet('4'))
btndiv.grid(row=4, column=3, sticky=NSEW)

window.mainloop()