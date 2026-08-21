from machine import Pin, I2C
import sh1106
import time
import network
import secrets
import urequests

#internet connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

while not wifi.isconnected():
    time.sleep(0.5)
    print("Attempting connection...")

print("Connected to " + secrets.WIFI_SSID)
print(wifi.ifconfig())

#request test
year = time.localtime()[0]
now = time.gmtime()

date = "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z".format(now[0], now[1], now[2], now[3], now[4], now[5])

url = "https://api.openf1.org/v1/sessions?year=" + str(year) + "&date_start%3E=" + str(date)

response = urequests.get(url)
sessions = response.json()
response.close()

next_session = sessions[0]

start = next_session["date_start"]
end = next_session["date_end"]

session_data = {
    "date": start[8:10] + "/" + start[5:7],
    "time_start": str(int(start[11:13]) + 2) + ":" + start[14:16],
    "time_end": str(int(end[11:13]) + 2) + ":" + end[14:16]
}

print(next_session["location"])
print(next_session["session_name"])
print(session_data["date"])
print(session_data["time_start"])
print(session_data["time_end"])


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
syear = str(year)[2:]

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
        oled.text(next_session["location"], 0, 10)
        oled.text(next_session["session_name"], 0, 20) 
        oled.text("On " + session_data["date"] + "/" + syear, 0, 30)
        oled.text("At " + session_data["time_start"] + "-" + session_data["time_end"], 0, 40)
        oled.text("1/2", 100, 50)
        oled.show()
        
    else:
        oled.fill(0)
        pin1.value(0)
        pin2.value(0)
        pin3.value(0)
        oled.text("Last winner:", 0, 0)
        oled.text("Oscar Piastri", 0, 10)  
        oled.text("Last session:", 0, 20)
        oled.text("Hungary Race", 0, 30)
        oled.text("Winner: NOR 1", 0, 40)
        oled.text("2/2", 100, 50)
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

