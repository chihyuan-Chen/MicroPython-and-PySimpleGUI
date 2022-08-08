# main.py -- put your code here!

from machine import Pin

from pyb import UART

u = UART(2,9600)




tm = pyb.Timer(4,freq=1000)

pwm1 = tm.channel(2,mode = pyb.Timer.PWM,pin = pyb.Pin('PD13'))
pwm2 = tm.channel(4,mode = pyb.Timer.PWM,pin = pyb.Pin('PD15'))
pwm3 = tm.channel(1,mode = pyb.Timer.PWM,pin = pyb.Pin('PD12'))
pwm4 = tm.channel(3,mode = pyb.Timer.PWM,pin = pyb.Pin('PD14'))


while True:
    x = u.any()
    if x != 0:
        t = u.read()
        if t == b'r':
            pwm1.pulse_width_percent(0)
            pwm2.pulse_width_percent(0)
            pwm3.pulse_width_percent(99)
            pwm4.pulse_width_percent(0)
            pyb.delay(100)
            
            pwm1.pulse_width_percent(0)
            pwm2.pulse_width_percent(0)
            pwm3.pulse_width_percent(0)
            pwm4.pulse_width_percent(0)
            
            pyb.delay(150)
        if t == b'l':
            pwm1.pulse_width_percent(99)
            pwm2.pulse_width_percent(0)
            pwm3.pulse_width_percent(0)
            pwm4.pulse_width_percent(0)
            pyb.delay(100)
            
            pwm1.pulse_width_percent(0)
            pwm2.pulse_width_percent(0)
            pwm3.pulse_width_percent(0)
            pwm4.pulse_width_percent(0)
            pyb.delay(150)
        if t == b'f':
            pwm1.pulse_width_percent(99)
            pwm2.pulse_width_percent(0)
            pwm3.pulse_width_percent(99)
            pwm4.pulse_width_percent(0)
            pyb.delay(100)
            
            pwm1.pulse_width_percent(0)
            pwm2.pulse_width_percent(0)
            pwm3.pulse_width_percent(0)
            pwm4.pulse_width_percent(0)
            pyb.delay(150)
            
            