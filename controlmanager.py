import os
import paho.mqtt.client as mqtt
import sys
from datetime import datetime
import requests
import json

topic = "#"
server = "34.193.131.206" #EC2 address

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.payload)
    if(msg.payload == "emer"):
        os.system("python3 /home/ubuntu/Control_Magager/Texting.py") #Texting.py dir 
    elif(msg.payload == "weather") :
        os.system("python3 /home/ubuntu/Control_Magager/weather.py") #weather.py dir

client =mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.subscribe("#")
client.loop_forever()