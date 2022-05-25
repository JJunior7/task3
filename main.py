from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import paho.mqtt.client as mqtt

client=mqtt.Client("python1")

broker="broker.emqx.io"
port=1883

print("connecting to broker",broker,port)
client.connect(broker)

# client.loop_forever()
client.subscribe("door/door1")
HOST="192.168.1.153"
PORT=9999


class NeuralHTTP(BaseHTTPRequestHandler):



    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        print(post_data)
        client.publish("door/door1",post_data)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()


server= HTTPServer((HOST,PORT),NeuralHTTP)
print("server is running...")
server.serve_forever()
server.server_close()







        