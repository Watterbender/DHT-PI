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

#while True:
try:
    temperatura1 = DHT1.temperature
    print("Temperatura={0:0.1f}ºC".format(temperatura1))

except RuntimeError as err:
    print(err.args[0])
    #time.sleep(2.0)
    #continue

except Exception as err:
    print("Velika napaka")
    DHT1.exit()
    raise err

#time.sleep(3.0)