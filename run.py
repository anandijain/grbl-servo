import serial
import time
import sys

# Set up serial connection
port = "COM4"  # Replace with your GRBL serial port
baud_rate = 115200

def run_code(cnc, code_lines, delay=1):
    """
    Sends G-code commands to the CNC machine line by line.
    
    Args:
        cnc: Serial connection object.
        code_lines: List of G-code commands as strings.
        delay: Time delay between sending each command.
    """
    for line in code_lines:
        command = line.strip()
        if command:
            print(f"Sending: {command}")
            cnc.write(f"{command}\n".encode('utf-8'))
            time.sleep(delay)  # Wait for GRBL to process
            # Read response
            response = cnc.readline().decode('utf-8').strip()
            print(f"Response: {response}")

def run_file(cnc, file_path, delay=0.1):
    """
    Reads a G-code file and sends it to the CNC machine line by line.
    
    Args:
        cnc: Serial connection object.
        file_path: Path to the G-code file.
        delay: Time delay between sending each command.
    """
    with open(file_path, 'r') as file:
        for line in file:
            run_code(cnc, [line], delay)

if __name__ == "__main__":
    # Check for filename argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <gcode_file>")
        sys.exit(1)

    gcode_file = sys.argv[1]

    # Open serial connection
    with serial.Serial(port, baud_rate, timeout=1) as cnc:
        # Wait for GRBL to initialize
        time.sleep(2)
        cnc.flush()
        
        # Startup sequence
        startup_commands = [
            "$X",       # Unlock GRBL
            "M3S110",   # Set spindle speed
            "$H",       # Home the machine
            "??"        # Request machine status
        ]
        run_code(cnc, startup_commands, delay=1)  # Run startup sequence with a 1-second delay

        # Run the G-code file
        run_file(cnc, gcode_file, delay=0.5)
