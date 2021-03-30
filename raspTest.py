from gpiozero import LED
from time import sleep

ledGreen = LED(8)
ledOrange = LED(18)

while True:
    ledGreen.on()
    sleep(1)
    ledGreen.off()
    ledOrange.on()
    sleep(1)
    ledOrange.off()
