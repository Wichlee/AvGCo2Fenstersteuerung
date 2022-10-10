import paho.mqtt.client as mqtt

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883
WindowIsOpen = False
client_id = "window_actor"


def on_message(client, userdata, message):

    print("recieved message: ", message.payload)
    print("message topic: ", message.topic)

    if message.payload >= 1500.0:
        print("Opening Window")
        WindowIsOpen = True

    if message.payload < 1500.0:
        print("Closing Window")
        WindowIsOpen = False

client = mqtt.Client(client_id)
client.on_message = on_message
client.connect(mqttBrokerHostname, mqttBrokerPort)
print("Client", client_id, "succesfully conntected to broker", mqttBrokerHostname, mqttBrokerPort)

client.loop_forever()

client.subscribe("AvG/co2level")

