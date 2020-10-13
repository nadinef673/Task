from tkinter import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("BMI Calculator")


    self.lblOutput = Label(self, text = "Please enter your weight :")
    self.lblOutput.grid()

    Label(self, text = "lbs").grid(row = 1, column = 1)
    self.txtlbs = Entry(self)
    self.txtlbs.grid(row = 1, column = 0)
    self.txtlbs.insert(0, "")

    self.lblOutput = Label(self, text = "Please enter your height in feet and inches")
    self.lblOutput.grid()

    Label(self, text = "Feet").grid(row = 3, column = 1)
    self.txtfeet = Entry(self)
    self.txtfeet.grid(row = 3, column = 0)
    self.txtfeet.insert(0, "")

    Label(self, text = "Inches").grid(row = 4, column = 1)
    self.txtinches = Entry(self)
    self.txtinches.grid(row = 4, column = 0)
    self.txtinches.insert(0, "")

    self.btnClickMe = Button(self, text = "Calculate your BMI", command = self.addoutput)
    self.btnClickMe.grid()
    self.mainloop()

def addoutput(self):

    Label(self, text = "Your BMI is:").grid(row = 12, column = 0)
    self.lbltotal = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lbltotal.grid(row = 13, column = 0, sticky = "we")

    Label(self, text = "Your health status is:").grid(row = 14, column = 0)
    self.lblhealth = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblhealth.grid(row = 15, column = 0, sticky = "we")

    #calculate the BMI
    height_1 = int(self.txtfeet.get())
    height_2 = int(self.txtinches.get())
    weight = int(self.txtlbs.get())
    height_3=height_1*12                                                                    #converts feet into inches
    height=height_2+height_3                                                                #Adds height to get total height
    weight_total= weight*703
    height_total=height*height
    total=weight_total/height_total
    self.lbltotal["text"] = "%.2f" % total

   # if total <= 18.5:
    #              print ('Underweight')
   # elif total >= 18.5 and total <= 24.9:
    #              print ('Healthy')
   #elif total >= 25 and total <= 29.9:
         #         print ('Overweight')
   #elif total >= 30:
             #  print ('Obese')

    #self.lblhealth["text"] = "%s" % health


def main():
  a = App()

if __name__ == "__main__":
  main()