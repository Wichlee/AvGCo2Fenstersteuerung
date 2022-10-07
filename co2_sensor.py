import paho.mqtt.client as mqtt
from random import uniform
import time

mqttBrokerUri = "localhost"
mqttBrokerPort = 1883

client = mqtt.Client("CO2_Sensor")
client.connect(mqttBrokerUri, mqttBrokerPort)

while True:
    randNumber = uniform(1000.0, 3500.0)
    client.publish("CO2LEVEL", randNumber)
    print(str(randNumber) + "ppm published to topic CO2LEVEL")
    time.sleep(60)
