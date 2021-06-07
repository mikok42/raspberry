from gpiozero import LED
from time import sleep

ledGreen = LED(17)


while True:
    ledGreen.on()
    sleep(2)
    ledGreen.off()
   
