# %% imports
from MQTTDevice import MQTTDevice
import paho.mqtt.client as mqtt
from random import randint
from time import time, sleep

import sys
import asyncio
from rtcbot import Websocket, RTCConnection, PiCamera
from aiortc import RTCConfiguration, RTCIceServer

cam = PiCamera()

conn = RTCConnection(rtcConfiguration=RTCConfiguration([
                    RTCIceServer(urls="stun:stun.l.google.com:19302"),
                    RTCIceServer(urls="turn:io.scilifelab.se:5349",
                        username="imjoy",credential="3a53d013d9996594d591")
                ]))


# set parameters
setup_name          = "S001"
device_ID           = "RAS01"
device_MQTT_name    = "RASPI_" + str(randint(0, 100000))
mqtt_broker_ip      = "localhost"
mqtt_client_name    = "raspi1" # not necessary
mqtt_client_pass    = "1ipsar" # not necessary
mqtt_port           = 1883
mqtt_keepalive      = 60
mqtt_uselogin       = False


# conn = RTCConnection()
conn.video.putSubscription(cam)

class MQTTtest():
    '''
    Simple class to contain necessary code elements
    '''

    def __init__(self,setup_name,device_ID,device_MQTT_name,mqtt_broker_ip,mqtt_client_name,mqtt_client_pass,mqtt_port,mqtt_keepalive,mqtt_uselogin):

        # get parameters and store in instance
        self.setup_name         = setup_name
        self.device_ID          = device_ID
        self.device_MQTT_name   = device_MQTT_name
        self.mqtt_broker_ip     = mqtt_broker_ip
        self.mqtt_client        = None
        self.mqtt_client_name    = mqtt_client_name
        self.mqtt_client_pass    = mqtt_client_pass
        self.mqtt_port          = mqtt_port
        self.mqtt_keepalive     = mqtt_keepalive
        self.mqtt_uselogin      = mqtt_uselogin
        self.devices            = {}

        # connect to MQTT server
        self.mqtt_connect_to_server()

    def mqtt_register_devices(self, device_name, device_ID):
        '''
        Adds devices to pointers.

        Note: no ERROR-catches!
        '''
        self.devices[device_name] = MQTTDevice(setup=self.setup_name, device=device_ID,mqtt_client=self.mqtt_client)

    def mqtt_connect_to_server(self):
        mqtt.Client.connected_flag = False  # create flag in class
        mqtt.Client.bad_connection_flag = False  # new flag
        mqtt.Client.disconnect_flag = False
        mqtt.Client.turnoff_flag = False

         # define broker
        self.mqtt_client = mqtt.Client(self.device_MQTT_name)  # creates a new client
        if self.mqtt_uselogin:
            self.mqtt_client.username_pw_set(self.mqtt_client_name, self.mqtt_client_pass)

        # attach functions to client
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_disconnect = self.on_disconnect

        # start loop to process received messages
        self.mqtt_client.loop_start()

        try:
            print("mqtt_client: connecting to broker ".format(self.mqtt_broker_ip))
            self.mqtt_client.connect(host=self.mqtt_broker_ip, port=self.mqtt_port, keepalive=self.mqtt_keepalive)


            while not self.mqtt_client.connected_flag and not self.mqtt_client.bad_connection_flag:
                print("mqtt_client: Waiting for established connection.")
                sleep(1)

            if self.mqtt_client.bad_connection_flag:
                self.mqtt_client.loop_stop()
                print(
                    "WARNING -> mqtt_client: had bad-connection. Not trying to connect any further.")

        except Exception as err:  # e.g. arises when port errors exist etc
            print("mqtt_client: Connection failed")
            print(err)


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:  # connection established
            client.connected_flag = True
            #logger.info("Connected with result code = {}".format(rc))
            print("Connected with result code = {}".format(rc))
        else:
            #logger.warning("Connection error")
            print("Connection error")
            client.bad_connection_flag = True

    def on_message(self, client, userdata, message):
        if message == "off":
            client.turnoff_flag = True
        print("Time on receive={}\nReceived={}\nTopic={}\nQOS={}\nRetain Flag={}".format(time().str,message.payload.decode("utf-8"), message.topic, message.qos, message.retain))


    def on_disconnect(self, client, userdata, rc):

        print("disconnecting reason: {}".format(rc))
        client.connected_flag = False
        client.disconnect_flag = True

    def commanddef(self):
        '''
        prints a list of available commands
        '''
        self.command_dict = {'i': 'individual pixel', 'o': 'off', 'r': 'rectangular', 'x': 'exit'}
        print('The following commands are avialable:\n================================')
        for m in self.command_dict:
            print("{}: {}".format(m,self.command_dict[m]))

    def loop(self,use_device):
        print('What shall be done?')
        self.commanddef()
        while True:
            cmd = input()

            if cmd == 'i':
                self.devices[use_device].send("CLEAR")
                self.devices[use_device].send("PXL", 35, 40, 127, 200)
            elif cmd in ['o','x']:
                self.devices[use_device].send("CLEAR")
                self.devices[use_device].send("CLEAR")
                if cmd == 'x':
                    break
            elif cmd == 'r':
                self.devices[use_device].send("NA+3")
                self.devices[use_device].send("RECT+0+0+8+8+1", 120, 120, 120)
            else:
                print('Nothing to do here...')

        print('Have fun :)')


# Register devices# init class and auto-connect to server
uc2 = MQTTtest(setup_name=setup_name,device_ID=device_ID,device_MQTT_name=device_MQTT_name,mqtt_broker_ip=mqtt_broker_ip,mqtt_client_name=mqtt_client_name,mqtt_client_pass=mqtt_client_pass,mqtt_port=mqtt_port,mqtt_keepalive=mqtt_keepalive,mqtt_uselogin=mqtt_uselogin)

# add devices for testing -> LED
uc2.mqtt_register_devices(device_name='LED',device_ID='LAR01')
uc2.devices['LED'].send("CLEAR")



@conn.subscribe
def onMessage(msg):  # Called when messages received from browser
    print("Button clicked:", msg.get("type"))
    conn.put_nowait({"response": "received: " + msg.get("type")})
    uc2.devices['LED'].send(msg.get("type"))

async def connect():
    channel = sys.argv[1] if len(sys.argv)>1 else "default"
    print("Starting WebRTC, channel="+channel)
    ws = Websocket("https://rtc.imjoy.io/ws/" + channel)
    print("Waiting for remote connection")
    remoteDescription = await ws.get()
    print("Sending local description")
    robotDescription = await conn.getLocalDescription(remoteDescription)
    ws.put_nowait(robotDescription)
    print("Started WebRTC")
    await ws.close()
    print("WebRTC connected")

asyncio.ensure_future(connect())
try:
    asyncio.get_event_loop().run_forever()
finally:
    cam.close()
    conn.close()
