import paho.mqtt.client as mqtt

mqttBrokerUri = "localhost"
mqttBrokerPort = 1883
topic = "CO2LEVEL"
WindowIsOpen = False


def on_message(client, userdata, message):
    print("recieved message: ", str(message.payload.decode("utf-8")))
    if message > 1500:
        print("Öffne Fenster")
        WindowIsOpen = True
    if message < 1500:
        print("Schließe Fenster")
        WindowIsOpen = False

client = mqtt.Client("Fenstersteuerung")
client.connect((mqttBrokerUri, mqttBrokerPort))

client.loop_start()

client.subscribe("CO2_Sensor")
client.on_message = on_message()

client.loop_stop()