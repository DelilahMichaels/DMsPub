# python 3.8

import random
import time

from paho.mqtt import client as mqtt_client


# broker = 'broker.emqx.io'
broker = "b1eaeb99.ala.us-east-1.emqxsl.com"
port = 8084
topic = "jp/python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = '**********'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("RC is: " + str(rc))
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.username_pw_set("jpost", "password")
    # client.tls_set(ca_certs='./emqxsl-ca.crt')
    
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while msg_count < 5:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        print("\n\n" + "Resutls are: " + str(result))
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    # publish(client)
    time.sleep(5)
    client.disconnect()



if __name__ == '__main__':
    run()