import time,RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

trig=13
echo=11

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

try:
    while True:
        GPIO.output(trig,0)
        time.sleep(2E-6)
        GPIO.output(trig,1)
        time.sleep(10E-6)
        GPIO.output(trig,0)
        while GPIO.input(echo)==0:
            pass
        echo_start=time.time()
        while GPIO.input(echo)==1:
            pass
        echo_stop=time.time()
        pingtraveltime=echo_stop-echo_start
        print(int(pingtraveltime*1E6))
        time.sleep(.2)
                
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO is good to go')