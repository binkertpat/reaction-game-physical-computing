import RPi.GPIO as GPIO
import time            
import random 

roteled = 6;
ledspielereins = 7
ledspielerzwei = 5

spielereins = 2
spielerzwei = 4

sieg = False

def setup():
  GPIO.setwarnings(False)
  GPIO.setmode(roteled, GPIO.OUT)
  GPIO.setmode(ledspielereins, GPIO.OUT)
  GPIO.setmode(ledspielerzwei, GPIO.OUT)
  GPIO.setup(spielereins, GPIO.IN)
  GPIO.setup(spielerzwei, GPIO.IN)

  GPIO.output(roteled, GPIO.HIGH)
  sleep(random.randint(1,8))                    
  GPIO.output(roteled, GPIO.LOW)  


def spielereinssieg():
  GPIO.output(ledspielereins, GPIO.HIGH)
  print("Sieg für Spieler 1!")   
  sieg = True


def spielerzweisieg():
  GPIO.output(ledspielerzwei, GPIO.HIGH)
  print("Sieg für Spieler 2!")   
  sieg = True


def beidesieg():
  GPIO.output(ledspielereins, GPIO.HIGH)
  GPIO.output(ledspielerzwei, GPIO.HIGH)
  sieg = True


def loop():
 while True:
     sleep(0.01)
     schaltereins = GPIO.input(spielereins)
     schalterzwei = GPIO.input(spielerzwei)
     if(sieg == False):
        if (schaltereins == GPIO.LOW):
            spielereinssieg()
        if (schalterzwei == GPIO.LOW ):
            spielerzweisieg()
        if (schaltereins == GPIO.LOW and schalterzwei == GPIO.LOW):
            beidesieg()
  
setup()
loop()
