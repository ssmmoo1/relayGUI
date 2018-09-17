from fauxmo.plugins import FauxmoPlugin
import RPi.GPIO as GPIO
from time import sleep
from threading import Thread


class relayControlPlugin(FauxmoPlugin):

    def __init__(self, name: str, port: int, relayNum: int):
        GPIO.setmode(GPIO.BOARD)
        pins = {1: 7, 2: 11, 3: 12, 4: 13, 5: 15, 6: 16, 7: 18, 8: 22, 9: 29, 10: 31, 11: 32, 12: 33}

        self.pin1 = pins[relayNum]
        self.pin2 = pins[relayNum + 1]
        self.state = False

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.HIGH)
        super().__init__(name=name, port=port)

    def on(self) -> bool:
        t1 = Thread(target=self.onT)
        t1.start()
        self.state = True
        return True

    def off(self) -> bool:
        t1 = Thread(target=self.offT)
        t1.start()
        self.state = False
        return True

    def get_state(self):
        if self.state == False:
            return "off"
        else:
            return "on"

    def onT(self):
        GPIO.output(self.pin1, GPIO.LOW)
        sleep(6)
        GPIO.output(self.pin1, GPIO.HIGH)

    def offT(self):
        GPIO.output(self.pin2, GPIO.LOW)
        sleep(6)
        GPIO.output(self.pin2, GPIO.HIGH)




