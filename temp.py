from tkinter import *


def convert():
    celTemp = float(celTempVar.get())
    fahTemp = float(fahTempVar.get())

    if celTempVar.get() != 0.0:
        celToFah = (celTemp * 9 / 5 + 32)
        print(celToFah)
        fahTempVar.set(round(celToFah, 2))

    elif fahTempVar.get() != 0.0:
        fahToCel = ((fahTemp - 32) * (5 / 9))
        print(fahToCel)
        celTempVar.set(round(fahToCel, 2))


def reset():
    top = Toplevel(padx=50, pady=50)
    top.grid()
    message = Label(top, text="Reset Complete")
    button = Button(top, text="OK", command=top.destroy)

    message.grid(row=0, padx=5, pady=5)
    button.grid(row=1, ipadx=10, ipady=10, padx=5, pady=5)

    fahTempVar.set(int(0))
    celTempVar.set(int(0))


def exit():
    root.destroy()


def move(event=' '):
    canvas.move(imageFinal, 10, 10)
    canvas.move(label, 10, 10)
    canvas.update()


root = Tk()
root.title("Temperature Converter")
root.geometry("2000x1500")
root.configure(background="purple")
mainframe = Frame(root)
mainframe.grid()
mainframe.configure(background="purple")

celTempVar = IntVar()
celTempVar.set(int(0))
fahTempVar = IntVar()
fahTempVar.set(int(0))

titleLabel = Label(mainframe, text="Celcius/Fahrenheit Temperature", font=("Arial", 20, "bold", "underline"),
                   justify=CENTER, background="purple")
titleLabel.grid(row=0, column=2, columnspan=5, pady=10, padx=20)

group_label1 = LabelFrame(mainframe, text="Celsius to Fahrenheit", font=("Arial", 15, "bold", "underline"), fg="red",
                          background="purple", width=10)
group_label1.grid(row=1, column=1, columnspan=4, padx=12, ipady=14, rowspan=4)

first_entry = Entry(group_label1, justify="center", width = 10, bd = 5, textvariable = celTempVar, state=DISABLED)
first_entry.grid()


group_label2 = LabelFrame(mainframe, text="Fahrenheit to Celsius", font=("Arial", 15, "bold", "underline"), fg="blue",
                          background="purple", width=10)
group_label2.grid(row=1, column=6, columnspan=4, padx=12, ipady=14, rowspan=4)

second_entry = Entry(group_label2, justify='center', width=10, bd=5, textvariable=fahTempVar, state=DISABLED)
second_entry.grid(row=2, column=7)



convertButton = Button(mainframe, text="Calculate conversion", font=("Arial", 12, "bold"), relief=RAISED, bd=5,
                       justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                       command=convert)
convertButton.grid(row=9, column=2, ipady=8, ipadx=6, pady=5, sticky=NW, padx=55)

resetButton = Button(mainframe, text="Clear", font=("Arial", 12, "bold"), relief=RAISED, bd=5, justify=CENTER,
                     highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                     command=reset)
resetButton.grid(row=9, column=5, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

exitButton = Button(mainframe, text="Exit Progam", font=("Arial", 12, "bold"), relief=RAISED, bd=5, justify=CENTER,
                    highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                    command=exit)
exitButton.grid(row=9, column=6, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

def act_cel():
    first_entry.configure(state=NORMAL)

B1 = Button(mainframe, text="Activate Celsius", command=act_cel)
B1.grid(row=5, column=2, ipady=8, ipadx=6, rowspan=4)

def act_fah():
    second_entry.configure(state=NORMAL)

B2 = Button(mainframe, text="Activate Fahrenheit", command=act_fah)
B2.grid(row=5, column=6, ipady=6, ipadx=4, rowspan=4)

root.mainloop()
