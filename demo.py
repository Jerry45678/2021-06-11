from tkinter import *

def setBtnText(num):
    global count
    count+=1
    if count % 2 != 0:
        sign = "O"
    else:
        sign = "X"

    if num == 0 and btn0.cget('text')==" ":
        btn0.config(text=sign)
    elif num == 1 and btn1.cget('text')==" ":
        btn1.config(text=sign)
    elif num == 2 and btn2.cget('text')==" ":
        btn2.config(text=sign)
    elif num == 3 and btn3.cget('text')==" ":
        btn3.config(text=sign)
    elif num == 4 and btn4.cget('text')==" ":
        btn4.config(text=sign)
    elif num == 5 and btn5.cget('text')==" ":
        btn5.config(text=sign)
    elif num == 6 and btn6.cget('text')==" ":
        btn6.config(text=sign)
    elif num == 7 and btn7.cget('text')==" ":
        btn7.config(text=sign)
    elif num == 8 and btn8.cget('text')==" ":
        btn8.config(text=sign)

    if btn0.cget('text') == btn1.cget('text') and btn0.cget('text') == btn2.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1 win")
        elif btn0.cget('text') == "X":
            print("Player2 win")
    if btn3.cget('text') == btn4.cget('text') and btn3.cget('text') == btn5.cget('text'):
        if btn3.cget('text') == "O":
            print("Player1 win")
        elif btn3.cget('text') == "X":
            print("Player2 win")
    if btn6.cget('text') == btn7.cget('text') and btn6.cget('text') == btn8.cget('text'):
        if btn6.cget('text') == "O":
            print("Player1 win")
        elif btn6.cget('text') == "X":
            print("Player2 win")
    if btn0.cget('text') == btn3.cget('text') and btn0.cget('text') == btn6.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1 win")
        elif btn0.cget('text') == "X":
            print("Player2 win")
    if btn1.cget('text') == btn4.cget('text') and btn1.cget('text') == btn7.cget('text'):
        if btn1.cget('text') == "O":
            print("Player1 win")
        elif btn1.cget('text') == "X":
            print("Player2 win")
    if btn2.cget('text') == btn5.cget('text') and btn2.cget('text') == btn8.cget('text'):
        if btn2.cget('text') == "O":
            print("Player1 win")
        elif btn2.cget('text') == "X":
            print("Player2 win")
    if btn0.cget('text') == btn4.cget('text') and btn0.cget('text') == btn8.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1 win")
        elif btn0.cget('text') == "X":
            print("Player2 win")
    if btn2.cget('text') == btn4.cget('text') and btn2.cget('text') == btn6.cget('text'):
        if btn2.cget('text') == "O":
            print("Player1 win")
        elif btn2.cget('text') == "X":
            print("Player2 win")

count = 0

window = Tk()
window.title("Button test")
window.geometry("600x600+460+200")
window.config(bg="White")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

btn0 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(0))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(window, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(8))
btn8.grid(row=2, column=2, sticky=NSEW)

window.mainloop()