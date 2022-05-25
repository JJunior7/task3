from codecs import ignore_errors
from pydoc import cli
import paho.mqtt.client as mqtt
import time




def on_log(client,userdata,level,buf):
    print("log"+buf)

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("connected Ok")
    else:
        print("bad connection blah blah blah")

def on_disconnect(client,userdata,flags,rc=0):
    print("disconnected bye"+str(rc))

def on_message(client,userdata,msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8"))
    print("message recieved",m_decode)

broker="broker.emqx.io"
port=1883

client=mqtt.Client("python1")

client.on_connect=on_connect
client.on_disconnect=on_disconnect 
client.on_log=on_log
client.on_message=on_message


print("connecting to broker",broker,port)


# client.connect(broker)
# client.loop_start()
# client.subscribe("door/door1")
# client.publish("door/door1",response.text)


