import paho.mqtt.client as mqtt
import time

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883
WindowIsOpen = False
client_id = "window_actor"


def on_message(message):
    co2_level = message.payload
    print("recieved message: ", co2_level)
    print("message topic: ", message.topic)

    if co2_level >= 1500.0:
        print("Opening Window")
        WindowIsOpen = True
    if co2_level < 1500.0:
        print("Closing Window")
        WindowIsOpen = False

client = mqtt.Client(client_id)
client.connect(mqttBrokerHostname, mqttBrokerPort)
print("Client", client_id, "succesfully conntected to broker", mqttBrokerHostname, mqttBrokerPort)

client.loop_start()

client.subscribe("AvG/co2level")
client.on_message = on_message

time.sleep(120)
client.loop_stop()