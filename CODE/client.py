import sys
import asyncio
from rtcbot import Websocket, RTCConnection, CVCamera
from aiortc import RTCConfiguration, RTCIceServer
cam = CVCamera()

conn = RTCConnection(rtcConfiguration=RTCConfiguration([
                    RTCIceServer(urls="stun:stun.l.google.com:19302"),
                    RTCIceServer(urls="turn:io.scilifelab.se:5349",
                        username="imjoy",credential="3a53d013d9996594d591")
                ]))

# conn = RTCConnection()
conn.video.putSubscription(cam)

@conn.subscribe
def onMessage(msg):  # Called when messages received from browser
    print("Button clicked:", msg.get("type"))
    conn.put_nowait({"response": "received: " + msg.get("type")})
    
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
is_running = False 
while(True):
    try:
        asyncio.get_event_loop().run_forever()
    finally:
        cam.close()
        conn.close()