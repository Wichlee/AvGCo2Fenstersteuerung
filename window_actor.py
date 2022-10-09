import paho.mqtt.client as mqtt

mqttBrokerHostname = "localhost"
mqttBrokerPort = 1883
topic = "CO2LEVEL"
WindowIsOpen = False


def on_message(client, userdata, message):
    print("recieved message: ", str(message.payload.decode("utf-8")))
    if message >= 1500:
        print("Opening Window")
        WindowIsOpen = True
    if message < 1500:
        print("Closing Window")
        WindowIsOpen = False

client = mqtt.Client("Window Controller")
client.connect((mqttBrokerHostname, mqttBrokerPort))

client.loop_start()

client.subscribe("CO2_Sensor")
client.on_message = on_message()

client.loop_stop()