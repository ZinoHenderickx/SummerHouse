#!/usr/bin/env

__author__ = "Zino Henderickx"
__version__ = "1.0"

# LIBRARIES
from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import multiprocessing
import time
import timeit

IP = PiGPIOFactory('192.168.0.207')

# LED's
AMOUNT_LEDS = 4
LED1 = LED(17, pin_factory=IP)
LED2 = LED(4, pin_factory=IP)
LED3 = LED(3, pin_factory=IP)
LED4 = LED(2, pin_factory=IP)
LED = [LED1, LED2, LED3, LED4]

# BUTTONS
AMOUNT_BUTTONS = 4
BUTTON1 = Button(21, pin_factory=IP)
BUTTON2 = Button(20, pin_factory=IP)
BUTTON3 = Button(16, pin_factory=IP)
BUTTON4 = Button(12, pin_factory=IP)


def button_1():
    while True:
        if BUTTON1.value == 1 and LED1.value == 0:
            LED1.on()
            LED2.on()
            LED3.on()
            LED4.on()
            time.sleep(0.25)
        if BUTTON1.value == 1 and LED1.value == 1:
            LED1.off()
            LED2.off()
            LED3.off()
            LED4.off()
            time.sleep(0.25)


def main():
    button_1()


if __name__ == "__main__":
    main()