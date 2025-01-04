import serial
import time

# Set up serial connection
port = "COM4"  # Replace with your GRBL serial port
baud_rate = 115200
gcode_file = "square.gcode"  # Replace with your G-code file path

# Open serial connection
with serial.Serial(port, baud_rate, timeout=1) as cnc:
    # Wait for GRBL to initialize
    time.sleep(2)
    cnc.flush()
    cnc.write(f"$H\n".encode('utf-8'))
    # time.sleep(5)
    cnc.write(f"$X\n".encode('utf-8'))
    # Open the G-code file
    with open(gcode_file, 'r') as file:
        for line in file:
            # Strip comments and whitespace
            command = line.strip()
            if command:
                print(f"Sending: {command}")
                cnc.write(f"{command}\n".encode('utf-8'))
                time.sleep(0.1)  # Wait for GRBL to process
                # Read response
                response = cnc.readline().decode('utf-8').strip()
                print(f"Response: {response}")
