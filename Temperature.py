from tkinter import *
from winsound import *
import os
import ttk

##Initialize
root = Tk()
root.geometry('{}x{}'.format(938, 600))
canvas = Canvas(root, width = 938, height = 505, bg = 'white')
canvas.pack()
label = ttk.Label(root, text ="Hello my name is Scorp welcome to this drums app")
label.pack()
label.config(foreground ='black')
label.config(font = ('arial',15, 'bold'))
##PhotoImage(file ="g1.gif")
logo =PhotoImage(file ="drums1.gif")
imageFinal = canvas.create_image(480, 260, image = logo)


##logo =PhotoImage(file ="drums.gif")
##imageFinal = canvas.create_image(530, 80, image = logo)


def move():
    canvas.move(imageFinal, 10, 10 )
    canvas.move(label, 10, 10)
    canvas.update()

def play1():
    os.system('hi_hat.wav')

##define buttons
button = Button(text = 'move', height = 2, width = 4, command = move)
button.place(x=556, y=550)
button1 = Button(text = 'Hi-Hat', height = 2, width = 10, command = play1)
button1.place(x=20, y=240)
root.mainloop()
