# Bitcoin Price Display

A simple API caller that requests the price of bitcoin from an API server and displays it on a screen. Programmed in MicroPython on a Raspberry Pi Pico 2 W.

## Equipment
- Raspberry Pi Pico 2 W
> [!NOTE]
> Any microcontroller with network access and MicroPython support should be acceptable.
- Waveshare 2.3" 128 x 32 OLED HAT display
> [!NOTE]
> This is a 7-pin display connected via 4-pin SPI, however I2C screens should also work with a few tweaks.
- Socket-to-pin wires
> [!TIP]
> 7 wires for the 7 pin connector on the OLED screen, this can also be achieved without a breadboard through direct connections to the microcontroller.
- Access to an API server, we used https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT in this code.
  
## Pin Layout

<img width="1758" height="562" alt="image" src="https://github.com/user-attachments/assets/6c602631-2e49-41c2-a8e9-a63fbcd4efa5" />
Raspberry Pi Pico 2 W Pinout Diagram - https://github.com/user-attachments/files/25141177/pico-2-w-pinout.pdf

> [!NOTE]
> 3.3V and 5V are both acceptable for this screen, please check the voltage of your own LCD display.

## Photographs

<img width="2440" height="1640" alt="image" src="https://github.com/user-attachments/assets/53c4f1d6-0281-4199-81e2-f5424a912a26" />
Picture 1: Full Project
<img width="2440" height="1762" alt="image" src="https://github.com/user-attachments/assets/5e112682-afe0-4120-a9cf-e1ad740431cc" />
Picture 2: Connections to Raspberry Pi Pico
<img width="2440" height="1722" alt="image" src="https://github.com/user-attachments/assets/94b139e8-c00d-4dcd-a401-293e54bbaa97" />
Picture 3: Connections to Waveshare 2.23" OLED Display
<img width="2438" height="1696" alt="image" src="https://github.com/user-attachments/assets/d515e72e-496b-4a51-afe2-66bf892be33b" />
Picture 4: The loading screen when making an API request
