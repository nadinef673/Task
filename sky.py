from tkinter import*

root = Tk()
root.title("Temperature Converter")
step = LabelFrame(root, text="C")
root.geometry("750x700")
root.configure(background="red")
dinges=Frame(root)
dinges.configure(background="red")
dinges.grid()


def convert():
celTemp = celTempVar.get()
fahTemp = fahTempVar.get()



if celTempVar.get() != 0.0:
celToFah = (celTemp * 9/5 + 32)
print (celToFah)
fahTempVar.set(celToFah)

elif fahTempVar.get() != 0.0:
fahToCel = ((fahTemp - 32) * (5/9))
print (fahToCel)
celTempVar.set(fahToCel)



def clear():
top = Toplevel(padx=50, pady=50)
top.grid()
message = Label(top, text = "cleared")
button = Button(top, text="OK", command=top.destroy)

message.grid(row = 0, padx = 5, pady = 5)
button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

fahTempVar.set(int(0))
celTempVar.set(int(0))

celTempVar = IntVar()
celTempVar.set(int(0))
fahTempVar = IntVar()
fahTempVar.set(int(0))


titleLabel = Label (dinges, text = "Celcius/Fahrenheit Temperature", font = ("Arial", 20, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)

celLabel = Label (dinges, text = "Celcius: ", font = ("Arial", 16), fg = "purple")
celLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

celEntry = Entry (dinges, width = 10, bd = 5, textvariable = celTempVar, state=DISABLED)
celEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

fahLabel = Label (dinges, text = "Fahrenheit: ", font = ("Arial", 16), fg = "purple")
fahLabel.grid(row = 3, column = 2, pady = 10, sticky = NW)

fahEntry = Entry (dinges, width = 10, bd = 5, textvariable = fahTempVar, state=DISABLED)
fahEntry.grid(row = 3, column = 8, pady = 10, sticky = NW, padx = 125 )



convertButton =Button (dinges, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
convertButton.grid(row = 5, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)


clearButton = Button (dinges, text = "Clear", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = clear)
clearButton.grid(row = 5, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)

quitButton = Button(dinges, text = "Quit", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = quit)
quitButton.grid(row = 5, column = 3,ipady = 8, ipadx = 12, pady = 5, sticky = NW)

def act_cel():
    celEntry.configure(state=NORMAL)

B1=Button(dinges, text="activate celcius" , command=act_cel)
B1.grid(row=12, column=10, pady=10)

def act_fah():
    fahEntry.configure(state=NORMAL)

B2=Button(dinges, text="activate fahrenheit", command=act_fah)
B2.grid(row=12, column=11, pady=10)



root.mainloop()