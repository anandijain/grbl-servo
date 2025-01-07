import serial
import time
import sys

# Set up serial connection
port = "COM4"  # Replace with your GRBL serial port
baud_rate = 115200

def send_raise_command(speed=100):
    """
    Sends the M3S command with the specified speed to the CNC machine.
    
    Args:
        speed (int): The spindle speed to set (default is 100).
    """
    with serial.Serial(port, baud_rate, timeout=1) as cnc:
        # Wait for GRBL to initialize
        time.sleep(2)
        cnc.flush()
        
        # Send $X command to unlock
        cnc.write(f"$X\n".encode('utf-8'))
        time.sleep(0.1)  # Allow time for GRBL to process
        
        # Send M3S command
        command = f"M3S{speed}"
        print(f"Sending: {command}")
        cnc.write(f"{command}\n".encode('utf-8'))
        time.sleep(0.1)  # Allow time for GRBL to process
        response = cnc.readline().decode('utf-8').strip()
        print(f"Response: {response}")

if __name__ == "__main__":
    # Get speed from command-line argument or default to 100
    speed = 100
    if len(sys.argv) > 1:
        try:
            speed = int(sys.argv[1])
        except ValueError:
            print("Invalid speed value. Please provide an integer.")
            sys.exit(1)

    send_raise_command(speed)
