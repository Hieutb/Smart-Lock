import time
from PyQt5.QtCore import QThread
import RPi.GPIO as GPIO

class UnlockThread(QThread):
    def run(self):
        CONTROL_PIN = 12
        TIME_UNLOCK = 3
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(CONTROL_PIN, GPIO.OUT)

        GPIO.output(CONTROL_PIN, GPIO.HIGH)
        time.sleep(TIME_UNLOCK)
        GPIO.output(CONTROL_PIN, GPIO.LOW)

        GPIO.cleanup()
