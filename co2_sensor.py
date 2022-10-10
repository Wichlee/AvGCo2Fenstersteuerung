import paho.mqtt.client as mqtt
from random import uniform
import time

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883
client_id = "co2_sensor"

client = mqtt.Client(client_id)
client.connect(mqttBrokerHostname, mqttBrokerPort)
print("Client", client_id, "succesfully conntected to broker", mqttBrokerHostname, mqttBrokerPort)

while True:
    randNumber = int(uniform(1000, 3500))
    client.publish("AvG/co2level", randNumber)
    print(str(randNumber) + " ppm published to topic AvG/co2level")
    time.sleep(60)
