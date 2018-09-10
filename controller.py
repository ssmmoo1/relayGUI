#!/usr/bin/python3
import tkinter as tk
from time import sleep
from threading import Thread
from PIL import ImageTk, Image

#import RPi.GPIO as GPIO

pins = {1: 7, 2: 11, 3: 12, 4: 13, 5: 15, 6: 16, 7: 18, 8: 22, 9: 29, 10: 31, 11: 32, 12: 33}

#GPIO.setmode(GPIO.BOARD)

#for pin in pins:
    #GPIO.setup(pins[pin], GPIO.OUT)
    #GPIO.output(pins[pin], GPIO.HIGH)

root = tk.Tk()
root.title("Controller")

#root.attributes("-fullscreen", True)  Uncomment when turning in program
#root.bind('<Escape>',quit)
root.geometry("720x480")


#playImg = tk.PhotoImage(file="play.gif")
#pauseImg = tk.PhotoImage(file="pause.gif")
#shoeImg = ImageTk.PhotoImage(Image.open("shoe.jpg"))


class Relay():

    def __init__(self, relayNumber, xPos, yPos, label, long=False):  # Relay number is 1-16 used for http request
        global root
        global pins
        self.id = relayNumber
        self.x = xPos
        self.y = yPos
        self.name = label
        self.state = False

        self.pin1 = pins[relayNumber]
        self.pin2 = pins[relayNumber + 1]

        span = 1
        if(long == True):
            span=2

        #self.label = tk.Label(master=root, text=self.name)
        #self.label.grid(row=xPos - 1, column=yPos)

        self.button = tk.Button(master=root, command=self.startProcess, bd=10)
        #self.button.grid(row=xPos, column=yPos,rowspan=span, ipadx=100, ipady=100, padx=10, pady= 10, sticky= "WENS")
        self.button.grid_propagate(0)

        #self.txt1 = tk.Label(text = self.name)
        #self.txt1.grid(row=xPos, column=yPos, sticky="S")

        #self.txt2 = ""

        self.inProgress = False
        self.stop = False

    def startProcess(self):
        if (self.inProgress == False):
            if (self.state == False):
                #self.button.config(image=pauseImg)
                print("Opening stage I")

            else:
                #self.button.config(image=playImg)
                print("Closing stage I")

            ocThread = Thread(target=self.openClose)
            ocThread.start()

        else:
            print("Already opening or closing please wait")
            self.stop = True

    def openClose(self):

        self.inProgress = True

        if (self.state == False):

            print("opening stage II")

            #GPIO.output(self.pin2, GPIO.HIGH)
            print("Pin " + str(self.pin2) + " output HIGH")
            #GPIO.output(self.pin1, GPIO.LOW)
            print("Pin " + str(self.pin1) + " ouput low")

            print("Waiting ten seconds")

            sleepCounter = 0

            while (sleepCounter < 600 and self.stop == False):
                sleep(.01)
                sleepCounter += 1

            #GPIO.output(self.pin1, GPIO.HIGH)
            print("Pin " + str(self.pin1) + " output high")

            self.state = True
            self.stop = False

        else:
            print("opening stage II")

            #GPIO.output(self.pin1, GPIO.HIGH)
            print("Pin " + str(self.pin1) + " output HIGH")
            #GPIO.output(self.pin2, GPIO.LOW)
            print("Pin " + str(self.pin2) + " ouput low")

            print("Waiting ten seconds")

            sleepCounter = 0

            while (sleepCounter < 600 and self.stop == False):
                sleep(.01)
                sleepCounter += 1

            #GPIO.output(self.pin2, GPIO.HIGH)
            print("Pin " + str(self.pin2) + " output high")

            self.state = False
            self.stop = False

        self.inProgress = False
        return


ypad = 63
xpad = 68


d1 = Relay(1, 0, 0, "Shoe Rack", long=True)
d2 = Relay(3, 0, 1, "Garmet Drawer", long = True)


d1.button.grid(row=d1.x, column=d2.x,rowspan=2, ipadx=xpad, ipady=ypad,  padx=8, pady= 8, sticky= "WENS")
d2.button.grid(row=d2.x, column=d2.y,rowspan=2, ipadx=xpad, ipady=ypad,  padx=8, pady= 8, sticky= "WENS")





d3 = Relay(5, 0, 2, "Keith's upper closet")
d4 = Relay(7, 1, 2, "Keith's lower closet")
d5 = Relay(9, 0, 3, "Erika's upper closet")
d6 = Relay(11,1, 3, "Erika's lower closet")
d3.button.grid(row=d3.x, column=d3.y,rowspan=1, ipadx=xpad, ipady=ypad, padx=10, pady= 10, sticky= "WENS")
d4.button.grid(row=d4.x, column=d4.y,rowspan=1, ipadx=xpad, ipady=ypad, padx=10, pady= 10, sticky= "WENS")
d5.button.grid(row=d5.x, column=d5.y,rowspan=1, ipadx=xpad, ipady=ypad, padx=10, pady= 10, sticky= "WENS")
d6.button.grid(row=d6.x, column=d6.y,rowspan=1, ipadx=xpad, ipady=ypad, padx=10, pady= 10, sticky= "WENS")

def allOpenClose():
    d1.startProcess()
    d2.startProcess()
    d3.startProcess()
    d4.startProcess()
    d5.startProcess()
    d6.startProcess()


allControl = tk.Button(master=root, command = allOpenClose, bd=10)
allControl.grid(row= 3, column =0, columnspan= 4, ipadx=340, ipady=25)



root.mainloop()
