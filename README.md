# UC2 goes Cloud ☁️ 

**2nd Photonics Days Makathon:** *Digital concept for university internships in physics and optics*


## 📅 General Schedule

| Date | Time | Task |
| ------------- |:-------------:| -----:|
|  21.09. | 09.30 – 22.00 | Makeathon |
|  22.09. | 09.30 – 11.30  | Pitches |


## What is UC2?

UC2 [You-See-Too] is a joint research project of the Leibniz Institute for Photonic Technology (IPHT) Jena and the Lichtwerkstatt Jena. The aim is to abstract the function of each complex optical device and to guarantee reusability by dividing it into functional subgroups. The assembly of these modules to an optical setup, e.g. a light microscope, is done intuitively without much previous knowledge according to the modular principle. The system is based on commercially available components such as the Raspberry Pi (+camera), smartphones, low-cost optics and innovative 3D- printed cubes, which are mounted on a magnetic base plate. Each cube can contain a specific function. By combining different functions, complex systems are created, which can range from a simple lens to a sensitive holographic microscope. The product therefore does not end at the moment of its production, but lives on through the creativity of the user. 

One 3D printed cube is mounted on a magnetic baseplate:
<p align="center">
<img src="https://github.com/bionanoimaging/UC2-GIT/raw/master/IMAGES/UC2_Explosion_v2.png" width="150">
</p>

You can customize a cube with inserts and combine them to very complicated optical setups:
<p align="center">
<img src="https://github.com/bionanoimaging/UC2-GIT/raw/master/IMAGES/UC2_openstandard.png
" width="650">
</p>


## UC2 Principle 

- The "4f'-Optics" concept allows lenses to be linked like functional blocks
- A simple microscope is created by snapping two lenses together at a certain distance from each other 
- The 3D-printed UC2 system enables a stable mounting by means of a magnetic mechanism
- Adding additional components (such as lasers) can lead to complex setups like the light-sheet microscope (figure).
- The frame (cube, base plate) forms the skeleton of the toolbox
- The mechanical insert is developed by the user and determines the function of the cube 


The "4f'-optics" or Fourier optical principle basically means, that focal lengths of ajacent lenses follow one another and form image and Fourier planes:
<img src="https://github.com/bionanoimaging/UC2-GIT/raw/master/IMAGES/UC2_simplemicroscope.png" width="650">
</p>


## Problem

Presence events at many universities are currently "corona-conditioned", although university operations must continue. For many students, this means that in addition to the classic lectures and seminars, internships and final theses are also part of the successful completion of their studies. Experiments via videos help to understand, but the experiences actually only follow from the interaction. The same applies to biologists* who now have clearly limited access to the laboratory. Experiments that require microscopes are thus made much more difficult. 


## General UC2 Structure

- 📝 [UC2 - Paper/Preprint](https://www.biorxiv.org/content/10.1101/2020.03.02.973073v1) 

- 👨‍💻 [UC2 - Software Repository](https://github.com/bionanoimaging/UC2-Software-GIT/)

-  🧰 [UC2 - Hardware Repository](https://github.com/bionanoimaging/UC2-GIT/)

- 📃 [UC2 - Website ](https://youseetoo.org)





👩🏼⚒🦠🧬📃

## Challenge

With UC2 we want to provide the missing access to both optical experiments and microscopes from remote. In doing so, we are aiming for the "lab-in-the-cloud", where components such as cameras, stages or lamps can be operated by external devices (e.g. laptops). A minicomputer (Raspberry Pi) enables digital image acquisition, additional components such as the Arduino microcontroller or ESP32 ensure the control of motors for focusing and lighting. 

The challenge is to create a web interface in the sense of "IoT" (Internet-of-things), where students can log in and program, control and monitor the devices from home. Common protocols such as MQTT and Web-RTC for controlling and reading the images are to be tested. The finished microscope will be located at the Leibniz IPHT during the "Challenge" and can be remotely programmed via SSH.

**How it could look like:**

<p align="center">
<img src="./IMAGES/FIG1.png" width="700">
</p>

ℹ️  More information for the incubator microscope can be found [**here**](https://github.com/bionanoimaging/UC2-GIT/tree/master/APPLICATIONS/APP_Incubator_Microscope). Information 


## Solution 

Since the devices from the UC2 project already have a network and IoT capable interface, only one connection between the devices and the users at home is needed. In the best case this should be done via a browser platform where students can log in and work on the tasks remotely. 
The goal is to create a website that displays the video stream from a Raspberry Pi camera and provides buttons for hardware functions such as light on/off. The commands for the hardware are to be sent from the Raspberry Pi to the MQTT devices located on the same network.


## Milestones 

The task mentioned above sounds like a lot of work. Where to start? In the following we try to break down the final goal to access the small microscope to external users through a website into little pieces.

### ℹ️ Some information in advance

***📤 Datalimit:*** The microscope is connected to a portable Wifi hotspot which has a datalimit of **10GB** for the **10h** makathon!

***✉️ Contact:*** You can reach us by filling an issue in this github repository, via the Discord channel or via mail: **[info@youseetoo.org](info@youseetoo.org)**.

***⛏ Software:***

- SSH: Access the Raspberry Pi remotely through [WinSCP](https://winscp.net/eng/docs/lang:de) + [Putty](https://www.putty.org/)
- ImJoy: Create a plugin which connects Python, Javascript and streaming applications using [ImJoy](https://imjoy.io/) for tutorials look [here](https://imjoy.readthedocs.io/en/latest/tutorials/)
- Chrome: Debugging HTML/Javascript becomes handy with chromes on-board debugging tools 



# 
VPN + SSH + HTTPS
Setup VPN-connection (openvpn client) + login via SSH
Read & understand python script/call structure with MQTT via <GITLINK>
Move motor, turn on/off light and take an image
Stream video (at lowest quality possible)
https://appuals.com/how-to-perform-video-streaming-using-raspberry-pi/
MJPEG and HTTPS vs h264 with webRTCTest https://medium.com/home-wireless/headless-streaming-video-with-the-raspberry-pi-zero-w-and-raspberry-pi-camera-38bef1968e1
Create a homepage and run on RASPI -> VUE.js which calls a node.js interface and redirects commands
Implement camera-stream into homepage and buttons to interact with remote device
webRTC + STUN
read into imjoy.io
Setup webRTC on RasPi
Install an imjoy.io instance on your PC (within browser) and write an interface to connect to Raspi
Best 
René

- Challenges (milestones)

## Steps

### 0. Connect to the Raspi 

The Raspberry Pi located at the Leibniz IPHT Jena is connected to a Wifi Router which itself is connected to the internet through a UMTS USB Stick. 
The global IP address is XX.XX.XX.XX.

General steps to connect to the Raspi: 



## 1. Control Motors remotely 
- motors, LED

## 2. Create simple web-based GUI 
- Button for LED on/off

## 3. Create WebRTC camera  live- stream 
- 


## Final: Implement everything into ImJoy 

https://gist.github.com/oeway/279c412350d53de07db8760141667b31



```
<docs lang="markdown">
[TODO: write documentation for this plugin.]
</docs>

<config lang="json">
{
  "name": "UC2-Streamer",
  "type": "window",
  "tags": [],
  "ui": "",
  "version": "0.1.1",
  "cover": "",
  "description": "[TODO: describe this plugin with one sentence.]",
  "icon": "extension",
  "inputs": null,
  "outputs": null,
  "api_version": "0.1.8",
  "env": "",
  "permissions": [],
  "requirements": [
    "https://horrible-fly-95.telebit.io/libs/request.min.js",
     "https://horrible-fly-95.telebit.io/libs/adapter.min.js",
    "https://horrible-fly-95.telebit.io/webrtcstreamer.js"],
  "dependencies": [],
  "defaults": {"w": 20, "h": 10, "fullscreen": true}
}
</config>

<script lang="javascript">

class ImJoyPlugin {
  async setup() {
    api.log('initialized')
  }

  async run(ctx) {
    var webrtcConfig = {
      url: "https://horrible-fly-95.telebit.io" ,
      options: "rtptransport=tcp&timeout=60",
      layoutextraoptions: "&width=320&height=0",
      defaultvideostream: "Bunny"
    }

    var url = { video:"mmal service 16.1" };  
    var options = webrtcConfig.options;
    if (typeof URLSearchParams != 'undefined') {
      var params = new URLSearchParams(location.search);
      if (params.has("video") || params.has("audio")) {
        url = { video:params.get("video"), audio:params.get("audio") };
      }
      if (params.has("options")) {
        options = params.get("options");
      }
    }
    const webRtcServer = new WebRtcStreamer("video", webrtcConfig.url);
    document.getElementById("title").innerHTML=url.video; 
    webRtcServer.connect(url.video,url.audio,options);
    request("GET" , webrtcConfig.url + "/api/version").done( function (response) { 
      document.getElementById("footer").innerHTML = "<p><a href='https://github.com/mpromonet/webrtc-streamer'>WebRTC-Streamer</a> " + JSON.parse(response.body).split(" ")[0] + "</p>";			
    });			

  }
}

api.export(new ImJoyPlugin())
</script>

<window lang="html">
  <div>
    <h2 id="title"></h2>
    <video id="video" muted></video>
    <footer id="footer"></footer>
  </div>
</window>

<style lang="css">
#video {
  width: 100%;
}
</style>
```