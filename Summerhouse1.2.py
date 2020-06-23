#!/usr/bin/env

__author__ = "Zino Henderickx"
__version__ = "1.2"

# LIBRARIES
from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import multiprocessing
import time
import timeit
from gpiozero import PWMLED

IP = PiGPIOFactory('192.168.0.207')


# LED's
AMOUNT_LEDS = 4
LED1 = LED(26, pin_factory=IP)
LED2 = LED(19, pin_factory=IP)
LED3 = LED(6, pin_factory=IP)
LED4 = LED(11, pin_factory=IP)

# BUTTONS
AMOUNT_BUTTONS = 4
BUTTON1 = Button(14, pin_factory=IP)
BUTTON2 = Button(16, pin_factory=IP)
BUTTON3 = Button(12, pin_factory=IP)
BUTTON4 = Button(23, pin_factory=IP)


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


def button_2():
    while True:
        if BUTTON2.value == 1 and LED3.value == 0:
            LED3.on()
            LED4.on()
            time.sleep(0.25)
        if BUTTON2.value == 1 and LED3.value == 1:
            LED3.off()
            LED4.off()
            time.sleep(0.25)


def button_3():
    while True:
        if BUTTON3.value == 1 and LED1.value == 0:
            LED1.on()
            LED2.on()
            LED3.on()
            LED4.on()
            time.sleep(0.25)
        if BUTTON3.value == 1 and LED1.value == 1:
            LED1.off()
            LED2.off()
            LED3.off()
            LED4.off()
            time.sleep(0.25)


if __name__ == "__main__":
    x1 = multiprocessing.Process(target=button_1)
    x2 = multiprocessing.Process(target=button_2)
    x3 = multiprocessing.Process(target=button_3)
    x1.start()
    x2.start()
    x3.start()