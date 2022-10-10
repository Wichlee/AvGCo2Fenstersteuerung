import paho.mqtt.client as mqtt
import time

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883
WindowIsOpen = False


def on_message(message):
    co2_level = float(message.payload.decode("utf-8"))
    print("recieved message: ", co2_level)
    print("message topic: ", message.topic)

    if co2_level >= 1500.0:
        print("Opening Window")
        WindowIsOpen = True
    if co2_level < 1500.0:
        print("Closing Window")
        WindowIsOpen = False

client = mqtt.Client()
client.connect(mqttBrokerHostname, mqttBrokerPort)
print("Succesfully conntected to broker", mqttBrokerHostname, mqttBrokerPort)

client.loop_start()

client.subscribe("AvG/co2level")
client.on_message = on_message

time.sleep(30)
client.loop_stop()