from machine import TouchPad, Pin,PWM
from MX1508 import *
from micropython import const
import uasyncio as asio
from BLEUART import *

debug=0
motorl = MX1508(19, 21)
motorr = MX1508(18, 17)
sp=1023
an=0
on=0
comand=''
pwm = PWM(Pin(33,Pin.OUT))
pwm.freq(50)
pwm.duty(0)


        
def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
def servo(pin, angle):
    pin.duty(map(angle, 0, 180, 20, 120))
def on_rx():
    global comand,on
    on=1
    comand=uart.read().decode()
    #print(comand)
    comand=comand[2:]

ble = bluetooth.BLE()
uart = BLEUART(ble)
uart.irq(handler=on_rx)    
                
    
async def do_it(int_ms):
    global an,on
    while 1:
        await asio.sleep_ms(int_ms)
        print(comand)
        if comand=='516':
            motorl.forward(sp)
            motorr.forward(sp)
        if comand=='615':
            motorr.reverse(sp)
            motorl.reverse(sp)
        if (comand=='507')or(comand=='606')or(comand=='705')or(comand=='804'):
            motorr.stop()
            motorl.stop()
        if comand=='813' and on:
            motorl.forward(sp)
            motorr.reverse(sp)
        if comand=='714' and on:
            motorr.forward(sp)
            motorl.reverse(sp)
	if comand=='11:':
	    an+=30
            on=0
            if an>180:
                an=180
	if comand=='219':
	    an-=30
            on=0
            if an<-180:
                an=-180
        servo(pwm, an)


# define loop
loop = asio.get_event_loop()

#create looped tasks
loop.create_task(do_it(5))
# loop run forever
loop.run_forever()

#uart.close()