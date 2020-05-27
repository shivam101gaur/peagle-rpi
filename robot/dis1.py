import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BOARD)

TRI = 22
ECH = 18


GPIO.setup(TRI,GPIO.OUT)
GPIO.setup(ECH,GPIO.IN)

GPIO.output(TRI, False)

time.sleep(2)



while True:
   GPIO.output(TRI, True)
   time.sleep(0.00001)
   GPIO.output(TRI, False)

   while GPIO.input(ECH)==0:
      pulse_star = time.time()
      

   while GPIO.input(ECH)==1:
      pulse_en = time.time()

   pulse_duratio = pulse_en - pulse_star

   distanc = pulse_duratio * 17150

   distanc = round(distanc+1.15, 2)
   if(distanc<=30):         
      print(distanc)
      sys.stdout.flush()
         
      
      
   time.sleep(0.5)


