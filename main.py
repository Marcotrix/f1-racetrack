from machine import Pin, I2C
import sh1106
import time

#oled bullshit
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
oled = sh1106.SH1106_I2C(128, 64, i2c, addr=0x3C)

#pins
pin1 = Pin(2, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
pin3 = Pin(16, Pin.OUT)
pin4 = Pin(26, Pin.IN, Pin.PULL_UP)

#other variables
change = 0
racemode = 0

#display and leds setup
oled.rotate(1)
pin1.value(0)
pin2.value(0)
pin3.value(0)

while racemode == 0:
    #button press logic
    if pin4.value() == 0:
        change += 1
        if change > 1:
            change = 0
        time.sleep_ms(300)
        
    if change == 0:
        oled.fill(0)
        pin1.value(0)
        pin2.value(0)
        pin3.value(0)
        oled.text("Next Session:", 0, 0)
        oled.text("Zandvoort FP1", 0, 10)  
        oled.text("On 21/08/26", 0, 20)
        oled.text("At 12:30-13:30", 0, 30)
        oled.text("For other info", 0, 40)
        oled.text("press the button", 0, 50)
        oled.show()
        
    else:
        oled.fill(0)
        pin1.value(0)
        pin2.value(0)
        pin3.value(0)
        oled.text("Last winner:", 0, 0)
        oled.text("Oscar Piastri", 0, 10)  
        oled.text("Last session:", 0, 30)
        oled.text("Hungary Race", 0, 40)
        oled.text("Winner: NOR 1", 0, 50)
        oled.show()




while racemode == 1:
    #button press logic
    if pin4.value() == 0:
        change += 1
        if change > 2:
            change = 0
        time.sleep_ms(300)
        
    if change == 0:
        oled.fill(0)
        pin1.value(1)
        pin2.value(0)
        pin3.value(0)
        oled.text("Lap 11/60", 0, 0)
        oled.text("Green Flag", 0, 10)
        oled.text("Last FIA", 0, 30)
        oled.text("Decision:", 0, 40)
        oled.text("5s ANT", 0, 50)
        oled.text("Top 5:", 80, 0)
        oled.text("VER", 90, 10)
        oled.text("ANT 5", 86 , 20)
        oled.text("SAI", 90, 30)
        oled.text("HAD", 90, 40)
        oled.text("ALB", 90, 50)
        oled.show()

    elif change == 1:
        oled.fill(0)
        pin1.value(0)
        pin2.value(1)
        pin3.value(0)
        oled.text("Lap 11/60", 0, 0)
        oled.text("Yellow T11", 0, 10)
        oled.text("Last FIA", 0, 30)
        oled.text("Decision:", 0, 40)
        oled.text("5s ANT", 0, 50)
        oled.text("Top 5:", 80, 0)
        oled.text("VER", 90, 10)
        oled.text("ANT 5", 86 , 20)
        oled.text("SAI", 90, 30)
        oled.text("HAD", 90, 40)
        oled.text("ALB", 90, 50)
        oled.show()

    else:
        oled.fill(0)
        pin1.value(0)
        pin2.value(0)
        pin3.value(1)
        oled.text("Lap 11/60", 0, 0)
        oled.text("Red flag", 0, 10)
        oled.text("Last FIA", 0, 30)
        oled.text("Decision:", 0, 40)
        oled.text("Session Stopped", 0, 50)
        oled.text("Top 4:", 80, 0)
        oled.text("VER", 90, 10)
        oled.text("ANT 5", 86 , 20)
        oled.text("SAI", 90, 30)
        oled.text("HAD", 90, 40)
        oled.show()
