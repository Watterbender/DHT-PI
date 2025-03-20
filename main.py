import os
import time
import board
import adafruit_dht

from dotenv import load_dotenv

load_dotenv()

#DHT1 = os.getenv('DHT1')
#DHT2 = os.getenv('DHT2')

DHT1 = adafruit_dht.DHT11(board.D5)
DHT2 = adafruit_dht.DHT11(board.D6)

class Sensors:
    def __init__(self, ime, pot):
        self.ime = ime
        self.pot = pot

def temperatura(sensor):
    try:
        temperatura1 = sensor.pot.temperature
        print(f"{sensor.ime}: Temperatura = {temperatura1:0.1f}ºC")

    except RuntimeError as err:
        print(f"{sensor.ime}: {err.args[0]}")

    except Exception as err:
        print(f"{sensor.ime}: Velika napaka")
        sensor.pot.exit()
        raise err


#Majmune source env/bin/activate


sensors = [Sensors("petka", DHT1), Sensors("sestka", DHT2)]

for s in sensors:
    temperatura(s)



#time.sleep(3.0)