# https://bytebeam.io/blog/getting-started-with-mqtt-on-raspberry-pi-using-python/
#
import time
import random
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import logging
logger = logging.getLogger(__name__)
hostname = "port-1883-py4mqtt-jasmine-arabella.codeanyapp.com"
hostname = '167.88.61.92'
# port-xx-py4mqtt-jasmine-arabella.codeanyapp.com
broker_port = 1883
topic = "Cat Pics"

def on_connect():
    print("onnected")

def on_message():
    print("sent message")

client_id = f'My-work-mac-{random.randint(0, 1000)}'
client = mqtt.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id)
client.on_Connect = on_connect
client.on_message = on_message

client.connect(hostname, broker_port, 60)
logger.warning("The connection is: {}".format(client))

#generate a random number as message payload
message = str( client_id + " has cat number {}".format(random.randint(1, 234)))
client.publish(topic, message)
