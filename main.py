import os
import time
import board
import adafruit_dht

from dotenv import load_dotenv

load_dotenv()

DHT1pin = os.getenv('DHT1') 
DHT1ime = os.getenv('DHT1ime')
DHT2pin = os.getenv('DHT2') 
DHT2ime = os.getenv('DHT2ime')

dht1_pin = getattr(board, DHT1pin)
dht2_pin = getattr(board, DHT2pin)


DHT1 = adafruit_dht.DHT11(board.D5)
DHT2 = adafruit_dht.DHT11(board.D6)

class Sensors:
    def __init__(self, ime, pot):
        self.ime = ime
        self.pot = pot

def temperatura(sensor):
    temperatura1 = sensor.pot.temperature
    print(f"{sensor.ime}: Temperatura = {temperatura1:0.1f}ºC")



#Majmune source env/bin/activate


sensors = [Sensors(DHT1ime, DHT1), Sensors(DHT2ime, DHT2)]

for s in sensors:
    temperatura(s)
    s.pot.exit()



#time.sleep(3.0)