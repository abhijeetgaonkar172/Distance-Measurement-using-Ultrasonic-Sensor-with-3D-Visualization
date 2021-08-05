import serial           # Import Serial Library
from vpython import *    # Import all the vPython library

scene.title = "Ultrasonic_Distance_3D_Visuals" # Create your scene and give it a title.
scene.width = 1560  # We can set the dimension of your visual box. 1560X720 pixels works well on my screen
scene.height = 720
scene.center = vec(-2,-2,0)
scene.range = 8   # Set range of your scene to be 8 inches

arduinoSerialData = serial.Serial('COM3', 9600)  # Create Serial port object called arduinoSerialData

#create label to display distance
lengthLabel = label(pos=vec(-3, 4, 0), text='Target Distance is: ', box = 0, height=50)

#create measuringRod 3D object
measuringRod = cylinder(radius=0.1, length=6, color=color.yellow, pos=vec(-11.4, -1, 0))

#create target 3D object
target=box(length=0.2, width=3, height=3, color=color.green, pos=vec(0,-1,0))

#create ultrasonic sensor back 3D object
ultra_back =box(pos=vec(-11.9,-1,0), length=0.05, width=2, height=1, color=color.blue)

#create 2 cylinders(reciever transmitter ends of sensor)
reciever = cylinder(radius=0.4, length=0.5, color=color.gray(0.8), pos=vec(-11.9, -1, -0.5))
transmitter = cylinder(radius=0.4, length=0.5, color=color.gray(0.8), pos=vec(-11.9, -1, 0.5))

while (1 == 1): # Create a loop that continues to read and display the data
    if (arduinoSerialData.inWaiting() > 0): # Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline().decode()  # Reads the distance as a string and decode
        print(myData)       # Print the measurement to confirm things are working
        distance = float(myData)  # convert reading to a floating point number
        measuringRod.length = distance # Change the length of your measuring rod to your last measurement
        target.pos = vec(-11.4 + distance, -1, 0)  # change the position of target
        myLabel = 'Target Distance is: ' + myData  # Create label by appending string myData to string
        lengthLabel.text = myLabel  # display updated myLabel on your graphic