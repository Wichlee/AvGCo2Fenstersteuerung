import paho.mqtt.client as mqtt
from random import uniform
import time

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883

client = mqtt.Client()
client.connect(mqttBrokerHostname, mqttBrokerPort)
print("Succesfully conntected to broker", mqttBrokerHostname, mqttBrokerPort)

while True:
    randNumber = uniform(1000.0, 3500.0)
    client.publish("AvG/co2level", randNumber)
    print(str(randNumber) + " ppm published to topic CO2LEVEL")
    time.sleep(60)
