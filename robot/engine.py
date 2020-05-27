import RPi.GPIO as GPIO          
import time
import sys
import signal
import os


def exiting(sig_num,frame):   
        GPIO.cleanup()  
        sys.exit()

signal.signal(signal.SIGTERM, exiting)

# assigning variables

call_fn = sys.argv[1]

mtrA_inp1 = 11
mtrA_inp2 = 13

mtrB_inp1 = 15
mtrB_inp2 = 16

enA = 33
enB = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(mtrA_inp1,GPIO.OUT)
GPIO.setup(mtrA_inp2,GPIO.OUT)
GPIO.setup(mtrB_inp1,GPIO.OUT)
GPIO.setup(mtrB_inp2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
mtrA=GPIO.PWM(enA,1000)
mtrB=GPIO.PWM(enB,1000)




def move():
        speed = sys.argv[2]
        direction = sys.argv[3]
        duration = int(sys.argv[4])
        if(duration==0):duration=100
        if(speed=='low'):speed=25
        elif(speed=='medium'):speed=50
        elif(speed=='high'):speed=100
        else: speed=0
        if(direction=='front'):
                mtrA.start(speed)
                mtrB.start(speed)
                GPIO.output(mtrA_inp1,GPIO.LOW)
                GPIO.output(mtrA_inp2,GPIO.HIGH)
                GPIO.output(mtrB_inp1,GPIO.LOW)
                GPIO.output(mtrB_inp2,GPIO.HIGH)
                
                time.sleep(duration)
        elif(direction=='back'):
                mtrA.start(speed)
                mtrB.start(speed)
                GPIO.output(mtrA_inp1,GPIO.HIGH)
                GPIO.output(mtrA_inp2,GPIO.LOW)
                GPIO.output(mtrB_inp1,GPIO.HIGH)
                GPIO.output(mtrB_inp2,GPIO.LOW)
                
                time.sleep(duration)


 

def turn():
        speed = sys.argv[2]
        rotate = sys.argv[3]
        duration = int(sys.argv[4])
        if(duration==0):duration=100
        if(speed=='low'):speed=20
        elif(speed=='medium'):speed=50
        elif(speed=='high'):speed=100
        else: speed=0
        if(rotate=='left'):
                if(speed==20):
                        GPIO.output(mtrA_inp1,GPIO.LOW)
                        GPIO.output(mtrA_inp2,GPIO.LOW)
                        GPIO.output(mtrB_inp1,GPIO.LOW)
                        GPIO.output(mtrB_inp2,GPIO.HIGH)
                        
                        mtrB.start(speed)
                        time.sleep(duration)
                else:        
                        GPIO.output(mtrA_inp1,GPIO.HIGH)
                        GPIO.output(mtrA_inp2,GPIO.LOW)
                        GPIO.output(mtrB_inp1,GPIO.LOW)
                        GPIO.output(mtrB_inp2,GPIO.HIGH)
                        mtrA.start(speed)
                        mtrB.start(speed)

                        time.sleep(duration)
        if(rotate=='right'):
                if(speed==20):
                        GPIO.output(mtrB_inp1,GPIO.LOW)
                        GPIO.output(mtrB_inp2,GPIO.LOW)
                        GPIO.output(mtrA_inp1,GPIO.LOW)
                        GPIO.output(mtrA_inp2,GPIO.HIGH)

                        mtrA.start(speed)                       
                        time.sleep(duration) 
                else:
                        GPIO.output(mtrB_inp1,GPIO.HIGH)
                        GPIO.output(mtrB_inp2,GPIO.LOW)
                        GPIO.output(mtrA_inp1,GPIO.LOW)
                        GPIO.output(mtrA_inp2,GPIO.HIGH)
                        mtrA.start(speed)
                        mtrB.start(speed)
                        time.sleep(duration)        


    
    

        


eval(call_fn+'()')
        








