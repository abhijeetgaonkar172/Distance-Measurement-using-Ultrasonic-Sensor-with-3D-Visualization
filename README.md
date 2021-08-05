# Distance-Measurement-using-Ultrasonic-Sensor-with-3D-Visualization
## Introduction
In this project I have used Ultrasonic Sensor (HC-SR04) for distance measurement and further I have used Python, where I made a 3D Model of my system using Vpython library wherein we can create navigable real-time 3D animations. We can see the 3D Visualization of our System in python using the Pyserial library which collects the serial data from COM port directly to python.   

## Ultrasonic Sensor (HC-SR04)

![Introduction-to-HC-SR04](https://user-images.githubusercontent.com/51810591/128392990-da66b4d0-2ef0-481b-862f-7dfc8de7ad1b.jpg)

As shown above the HC-SR04 Ultrasonic (US) sensor is a 4-pin module, whose pin names are Vcc, Trigger, Echo and Ground respectively. This sensor is a very popular sensor used in many applications where measuring distance or sensing objects are required. The module has two eyes like projects in the front which forms the ultrasonic transmitter and Receiver.

### Sound Frequency Ranges:

![Sound frequencies](https://user-images.githubusercontent.com/51810591/128393114-c093be5f-27e2-494b-ae3a-b48cbbadacdf.png)

### Working:
The Ultrasonic transmitter transmits an ultrasonic wave, this wave travels in air and when it gets objected by any material it gets reflected back toward the sensor this reflected wave is observed by the Ultrasonic receiver module as shown in the picture below.

![Working](https://user-images.githubusercontent.com/51810591/128393173-bd281570-b835-41ce-9d7a-c0a76abad779.jpg)

Now, to calculate the distance using the above formulae, we should know the Speed and time. Since we are using the Ultrasonic wave, we know the universal speed of US wave at room conditions which is 330m/s. The circuitry inbuilt on the module will calculate the time taken for the US wave to come back and turns on the echo pin high for that same amount of time, this way we can also know the time taken. Now simply calculate the distance using a microcontroller or microprocessor.

![Timing diagram](https://user-images.githubusercontent.com/51810591/128393207-d580257d-de5b-4829-b6bc-4ddd06cf6ef9.jpg)

First, we need to trigger the sensor with a 10 us trigger pulse then our sensor will generate a sonic burst of 8 pulses at 40kHz this pulses will gets objected by an obstacle they reflect back toward our receiver end, if a pulse is received then it will be in a range of 150us – 25ms.
Note: Echo pulse is approximately 38ms if no object is detected (38ms because this is the time out period of echo pin in module HC-SR04 if no object detected)
The time taken by pulse to leave and return back is calculated by echo pin.

### pulseIn() function

Reads a pulse either HIGH or LOW. If value is HIGH, pulseIn() waits for the pin to go from LOW to HIGH, starts timing, then waits for the pin to go LOW and stops timing.
Returns length of pulse in microseconds and 0 if no complete pulse was received within the timeout.
Pulse: 10 microseconds – 3mins length.
Echo Pin will give us time travelled by the pulse (T)

Let’s take time (width of received pulse) = 500 us

Speed of Sound = 340 m/s = 0.034 cm/us

Distance = Time * Speed = (500 * 0.034)/2

Distance = 8.5 cm 

## Serial Data in Python using Pyserial Library

We want to read the sensor data i.e., distance of the object from the COM port directly into python. So, for this purpose we will use Pyserial library which helps us access the serial port.

### Pyserial Library
This module covers the access for the serial port.
https://pypi.org/project/pyserial/ 
Some important functions used:
#### readline() function: Reads serial information till EOL Character by deafault it is \n escape character.
The data which comes from NodeMCU serially is a byte string we need to decode it to Unicode string
For e.g:
b’70\n’ 
b (Prefixed), 70 (Data point), carriage return, newline character

#### decode() function: Process of converting bytes to Unicode(i.e., Decoding). Removes byte prefix and carriage & newline characters. 

## 3D Animation in Python using Vpython Library 
### Vpython Library
https://vpython.org/ 
VPython makes it unusually easy to write programs that generate navigable real-time 3D animations. It is based on the Python programming language which is widely used in introductory programming courses thanks to its clean design, and it is also widely used in science and business.
You can launch a VPython program from applications such as IDLE, Spyder, or a terminal if the version of Python is 3.5.3 or greater.
This short program will display a white box on a black background:
    from vpython import *
    box()
    Rotate the camera view: drag with the right mouse button (or Ctrl-drag left button).
    Zoom: drag with left and right mouse buttons (or Alt/Option-drag or scroll wheel).
    Pan: Shift-drag.
In the VPython 7 environment, VPython programs run on a local server, using standard Python, and output is sent to a browser, where the GlowScript graphics library is used to display the 3D animation. In the GlowScript environment, VPython programs are compiled in the browser itself by the RapydScript Python-to-JavaScript compiler, and the program is run in the browser.
 
The GlowScript libraries are based on WebGL and use GPU (Graphics Processing Unit) hardware. 
GlowScript is an easy-to-use, powerful environment for creating 3D animations and publishing them on the web. Here at glowscript.org, you can write and run GlowScript programs right in your browser, store them in the cloud for free, and easily share them with others.

WebGL (Web Graphics Library) is the new standard for 3D graphics on the Web, It is designed for the purpose of rendering 2D graphics and interactive 3D graphics.
First, we need to create our 3D model using vpython library. I have created a 3D model which is shown below. It consists of an ultrasonic sensor (i.e., made up of one box+ 2 cylinders), measuring rod (i.e., a cylinder) and obstacle (target box). Also added a text label of “Target Distance is” at top along with a data field which will update in real time as our port receives data from nodeMCU.

![3DVisual](https://user-images.githubusercontent.com/51810591/128393398-49bed14c-a06a-4a9c-a7d2-2ddf7e79c27a.PNG)

Some mathematical formulations, calculations done in the program are based on this figure.
 
![3D_Visualisation_Diagram](https://user-images.githubusercontent.com/51810591/128393420-665711ad-5ebd-41ea-8b4b-d54d0f15ec76.png)

Please refer the above figure, it clears all the mathematical formulations, calculations and logic developed in the python program for 3D Visualization.

## Hardware Required
1)NodeMCU ESP8266
2)Ultrasonic Sensor(HC-SR04)
3)Jumper Wires

## Hardware Connection

![Ultrasonic_Sensor_Diagram](https://user-images.githubusercontent.com/51810591/128393778-73b95333-ec53-4fc0-99a2-010aad2e5125.png)
