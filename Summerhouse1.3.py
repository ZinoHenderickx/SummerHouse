#!/usr/bin/env

__author__ = "Zino Henderickx"
__version__ = "1.3"

# LIBRARIES
from gpiozero import LED        # Bilbiotheek voor de LED te laten werken.
from gpiozero import Button     # Bilbiotheek voor de schakelaars ("buttons") te laten werken.
from gpiozero.pins.pigpio import PiGPIOFactory      # Bibliotheek om de Pi op afstand te laten bedienen.
import multiprocessing      # Bilbiotheek voor multiprocessing, meerdere toepassingen tegelijk te laten gebruiken.
import time     # Bibliotheek om een debounce of pauzes te laten werken.
from gpiozero import PWMLED     # Bibliotheek om een dimbaar licht te laten werken.

IP = PiGPIOFactory('192.168.0.207')     # Maakt verbinding met het IP adres van de Pi.


# LED's
AMOUNT_LEDS = 4     # Hoeveelhei LED's aanwezig.
LED1 = LED(26, pin_factory=IP)      # Benaming LED
LED2 = LED(19, pin_factory=IP)
LED3 = LED(6, pin_factory=IP)
LED4 = LED(11, pin_factory=IP)

# Constant

DEBOUNCE = 0.25     # Debounce om de reactietijd tussen het indrukken v/d knop en functie te verlengen.
SHORT_TIME = 5      # Tijd tussen een functie.
LONG_TIME = 30      # Tijd tussen een functie.


# BUTTONS

AMOUNT_BUTTONS = 4      # Hoeveelheid drukknoppen aanwezig.
BUTTON1 = Button(14, pin_factory=IP)        # Benaming drukknop.
BUTTON2 = Button(16, pin_factory=IP)
BUTTON3 = Button(12, pin_factory=IP)
BUTTON4 = Button(23, pin_factory=IP)


def turn_led_on():      # Definitie om alle leds HIGH te zetten.
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()


def turn_led_off():     # Definitie om alle leds LOW te zetten.
    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()


def let_led_blink():        # Definitie om alle leds te doen blinken.
    LED1.blink()
    LED2.blink()
    LED3.blink()
    LED4.blink()


def button_1():     # Definitie van de drukknop.
    while True:
        if BUTTON1.value == 1 and LED1.value == 0:      # Als button HIGH is en LED LOW voer de volgende functie uit.
            turn_led_on()       # Schakel alle leds in (functie hierboven vermeld).
            time.sleep(0.25)        # Zodat er genoeg tijd tussen zit tussen de reactie en de functie.
        if BUTTON1.value == 1 and LED1.value == 1:
            turn_led_off()
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
            turn_led_on()
            PWMLED(12, True, 0.50, 100)     # De functie heb ik nog niet werkende gekregen spijtig genoeg.
            time.sleep(0.25)
        if BUTTON3.value == 1 and LED1.value == 1:
            turn_led_off()
            time.sleep(0.25)


def button_4():
    while True:
        if BUTTON4.value == 1 and LED1.value == 1:      # Als Button 4 HIGH en LED1 HIGH = .
            time.sleep(30)       # 30 Seconden wachten...
            turn_led_off()      # Doe de led uit.
        if BUTTON4.value == 1 and LED2.value == 1:
            time.sleep(30)
            turn_led_off()
        if BUTTON4.value == 1 and LED3.value == 1:
            time.sleep(30)
            turn_led_off()
        if BUTTON4.value == 1 and LED4.value == 1:
            time.sleep(30)
            turn_led_off()
        if BUTTON4.value == 1 and LED1.value == 0:      # Als Button 4 HIGH en LED1 LOW = .
            turn_led_on()       # Schakel alle leds aan.
            time.sleep(30)      # Wacht 30 seconden.
            let_led_blink()     # Laat de leds blinken.
            time.sleep(5)       # 5 seconden laten blinken.
            turn_led_off()      # Alle leds uitschakelen.


if __name__ == "__main__":      # Main, d.w.z. functie dat alles doet werken in 1 opsomming.
    x1 = multiprocessing.Process(target=button_1)       # Naam van de functie met daarin de definitie van een knop.
    x2 = multiprocessing.Process(target=button_2)
    x3 = multiprocessing.Process(target=button_3)
    x4 = multiprocessing.Process(target=button_4)
    x1.start()      # Laat de functie starten.
    x2.start()
    x3.start()
    x4.start()