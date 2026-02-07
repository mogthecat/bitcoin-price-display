import machine
from machine import Pin, SPI
import network
import time
import urequests

# Change to the appropriate LCD library if using a differnt screen
import ssd1306 

NETWORK_NAME = "" #2.4GHz Wifi Networks only
PASSWORD = ""

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_NAME, PASSWORD)
    
    while not wlan.isconnected():
        time.sleep(1)
        
    print("Connected! IP:", wlan.ifconfig()[0])
    
    
def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT" # Can be changed to a different API Server
    
    try:
        res = urequests.get(url)
        data = res.json()               # Converts json into dictionary
        price = float(data['price'])    # Obtains the value from the price key
        res.close()                     # Closes the session to save memory
        print(f"Successful request! Price: {price}")
        
        return f"${price:,.2f}"
    
    except:
        return "API Error"

def main():

    # Change these pin numbers if wired differently
    spi = machine.SPI(1, baudrate=8000000, sck=Pin(10), mosi=Pin(11))
    # Order: (width, height, spi, dc, res, cs)
    # Change screen size and pin numbers if screen and wiring are different
    oled = ssd1306.SSD1306_SPI(128, 32, spi, Pin(8), Pin(12), Pin(9))
    
    connect_wifi()
    
    while True:
            
        oled.fill(0)
        print("Fetching price..")
        oled.text(f"Fetching price..", 4, 20, 1)
        oled.show()
        
        price = get_price()
        
        oled.fill(0)
        print(f"BTC = {price}")
        oled.text(f"BTC = {price}", 4, 20, 1)
        oled.show()
        
        time.sleep(5)
            
        
if __name__ == "__main__":
    main()
