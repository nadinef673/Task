from tkinter import *

def convert():
    celTemp = float(celTempVar.get())
    fahTemp = float(fahTempVar.get())



    if celTempVar.get() != 0.0:
        celToFah = (celTemp *  9/5 + 32)
        print(celToFah)
        fahTempVar.set(celToFah)

    elif fahTempVar.get() != 0.0:
        fahToCel = ((fahTemp - 32) * (5/9))
        print(fahToCel)
        celTempVar.set(fahToCel)



def reset():
    top = Toplevel(padx=50, pady=50)
    top.grid()
    message = Label(top, text = "Reset Complete")
    button = Button(top, text="OK", command=top.destroy)

    message.grid(row = 0, padx = 5, pady = 5)
    button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

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

titleLabel = Label(mainframe, text="Celcius/Fahrenheit Temperature", font=("Arial", 20, "bold", "underline"), justify=CENTER, background="purple")
titleLabel.grid(row=0, column=0, columnspan=5, pady=10, padx=20)

celLabel = Label(mainframe, text="Celcius: ", font=("Arial", 16, "bold", "underline"), fg="red", background="purple")
celLabel.grid(row=2, column=1, columnspan=7, pady=10, sticky=NW)

fahLabel = Label(mainframe, text="Fahrenheit: ", font=("Arial", 16, "bold", "underline"), fg="blue", background="purple")
fahLabel.grid(row=2, column=4, columnspan=7, pady=10, sticky=NW)

celEntry = Entry(mainframe, width=10, bd=5, textvariable=celTempVar)
celEntry.grid(row=3, column=1, columnspan=7, pady=10, sticky=NW, padx=125)

fahEntry = Entry(mainframe, width=10, bd=5, textvariable=fahTempVar)
fahEntry.grid(row=3, column=8, columnspan=7, pady=10, sticky=NW, padx=125)

convertButton = Button(mainframe, text="Convert", font=("Arial", 8, "bold"), relief=RAISED, bd=5, justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                       command=convert)
convertButton.grid(row=15, column=1, ipady=8, ipadx=6, pady=5, sticky=NW, padx=55)

resetButton = Button(mainframe, text="Reset", font=("Arial", 8, "bold"), relief=RAISED, bd=5, justify=CENTER,
                     highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                     command=reset)
resetButton.grid(row=15, column=2, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

exitButton = Button(mainframe, text="Exit", font=("Arial", 8, "bold"), relief= RAISED, bd=5, justify=CENTER,
                    highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                    command=exit)
exitButton.grid(row=15, column=3, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)








root.mainloop()






