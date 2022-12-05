import network
import secrets
from machine import Pin, Timer
import time

def Connect():
    
    #Turn Pico LED off to reset
    led = Pin("LED", Pin.OUT)
    led.off()
    
    #Configure wlan to connect to wifi network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)
        print(wlan.status())
        
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
        led.on()
    
