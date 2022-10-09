import time
import paho.mqtt.client as mqtt

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883
WindowIsOpen = False


def act(client, userdata, message):
    co2_level = float(message.payload.decode("utf-8"))
    print("recieved message: ", co2_level)
    print("message topic: ", message.topic)

    if co2_level >= 1500.0:
        print("Opening Window")
        WindowIsOpen = True
    if co2_level < 1500.0:
        print("Closing Window")
        WindowIsOpen = False

client = mqtt.Client("Window Controller")
client.connect(mqttBrokerHostname, mqttBrokerPort)

client.loop_start()

client.subscribe("CO2_Sensor")
client.on_message = act()

time.sleep(30)
client.loop_stop()