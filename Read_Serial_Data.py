import serial  # Import Serial Library

arduinoSerialData = serial.Serial('COM3', 9600)  # Create Serial port object called arduinoSerialData

while (1):
    if (arduinoSerialData.inWaiting() > 0): # Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline().decode() # Reads the distance as a byte string and decode
        print(myData)           # Print the measurement to confirm things are working