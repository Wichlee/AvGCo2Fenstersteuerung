import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "test.mosquitto.org"

client = mqtt.Client("Co2_level")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("CO2LEVEL", randNumber)
    print("Just published " + str(randNumber) + " to topic CO2LEVEL")
    time.sleep(1)
    # print("alles kaputt Rolf")