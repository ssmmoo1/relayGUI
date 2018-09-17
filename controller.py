#!/usr/bin/python3
import tkinter as tk
from time import sleep
from threading import Thread
from PIL import ImageTk, Image
#import RPi.GPIO as GPIO

#################################################################################
backgroundColor = "lightblue2"
buttonColor = "slategray"
textColor = "black"

fontSize = "22"

button1Text = "Shoe Rack"
button2Text = "Garmet Drawer"

button3Text = "Keith's Upper Closet"
button4Text = "Keith's Lower Closet"

button5Text = "Erika's Upper Closet"
button6Text = "Erika's Lower Closet"

button1ImageFile = "allShoes.png"
button2ImageFile = "dress.jpg"

button3ImageFile = "shirt.png"
button4ImageFile = "shorts.png"

button5ImageFile = "blouse.jpg"
button6ImageFile = "skirt.png"

actuatorActiveTime = 6
#################################################################################











pins = {1: 7, 2: 11, 3: 12, 4: 13, 5: 15, 6: 16, 7: 18, 8: 22, 9: 29, 10: 31, 11: 32, 12: 33}

#GPIO.setmode(GPIO.BOARD)

#for pin in pins:
    #GPIO.setup(pins[pin], GPIO.OUT)
    #GPIO.output(pins[pin], GPIO.HIGH)

root = tk.Tk()
root.title("Controller")
root.config(background=backgroundColor)

#root.attributes("-fullscreen", True)  Uncomment when turning in program
#root.bind('<Escape>',quit)
root.geometry("800x480")


button1Img = ImageTk.PhotoImage(Image.open("images/" + button1ImageFile))
button2Img = ImageTk.PhotoImage(Image.open("images/" +button2ImageFile))
button3Img = ImageTk.PhotoImage(Image.open("images/" +button3ImageFile))
button4Img = ImageTk.PhotoImage(Image.open("images/" +button4ImageFile))
button5Img = ImageTk.PhotoImage(Image.open("images/" +button5ImageFile))
button6Img = ImageTk.PhotoImage(Image.open("images/" +button6ImageFile))



class Relay():

    def __init__(self, relayNumber, xPos, yPos, label, long=False):
        global root
        global pins

        words= label.split()
        self.name = "\n".join(words)



        self.id = relayNumber
        self.x = xPos
        self.y = yPos
        self.state = False

        self.pin1 = pins[relayNumber]
        self.pin2 = pins[relayNumber + 1]

        self.span = 1
        if(long == True):
            self.span=2

        self.button = tk.Button(master=root, command=self.startProcess, bd=10, bg = buttonColor, text = self.name, font="Helvetica, " + fontSize , compound = tk.CENTER, activebackground=buttonColor, fg=textColor)
        self.button.grid(row=xPos, column=yPos,rowspan=self.span,padx=10, pady= 10)
        self.button.grid_propagate(0)


        self.inProgress = False
        self.stop = False


    def startReset(self):
        print("Resetting Stage I")
        t1 = Thread(target=self.reset)
        t1.start()

    def reset(self):
        print("Resetting Stage II")

        print("Setting " + str(self.pin1) + " to high")
        #GPIO.output(self.pin1, GPIO.HIGH)

        print("Setting " + str(self.pin2) + " to low")
        #GPIO.output(self.pin2, GPIO.LOW)

        print("Waiting six seconds")
        sleep(6)
        #GPIO.output(self.pin2, GPIO.HIGH





    def startProcess(self):
        if (self.inProgress == False):
            if (self.state == False):
                print("Opening stage I")

            else:
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

            print("Waiting " + str(actuatorActiveTime) + " seconds")

            sleepCounter = 0

            while (sleepCounter < (actuatorActiveTime * 100) and self.stop == False):
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

            print("Waiting " + str(actuatorActiveTime) + " seconds")

            sleepCounter = 0

            while (sleepCounter < (actuatorActiveTime * 100) and self.stop == False):
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


d1 = Relay(1, 0, 0, button1Text, long=True)
d2 = Relay(3, 0, 1, button2Text, long = True)

longHeight = 350
d1.button.config(height=longHeight, width= 100, image = button1Img, compound = tk.CENTER)
d2.button.config(height=longHeight, width=150, image = button2Img)




d3 = Relay(5, 0, 2, button3Text)
d4 = Relay(7, 1, 2, button4Text)
d5 = Relay(9, 0, 3, button5Text)
d6 = Relay(11,1, 3, button6Text)



smallHeight= 150
smallWidth = 185
d3.button.config(height=smallHeight, width=smallWidth, image=button3Img)
d4.button.config(height=smallHeight, width=smallWidth, image = button4Img)
d5.button.config(height=smallHeight, width=smallWidth, image = button5Img)
d6.button.config(height=smallHeight, width=smallWidth, image = button6Img)


def allClose():
    d1.startReset()
    d2.startReset()
    d3.startReset()
    d4.startReset()
    d5.startReset()
    d6.startReset()


allControl = tk.Button(master=root, command = allClose, bd=10, height = 1, width = 53, text="Close All", font="Helvetica, 18", bg=buttonColor, activebackground=buttonColor, fg=textColor)
allControl.grid(row= 3, column =0, columnspan= 4)



root.mainloop()
