import serial
import threading

# Replace 'COM4' with the correct port for your GRBL device
port = "COM4"
baud_rate = 115200

def read_from_serial(ser):
    """
    Continuously reads data from the serial port and prints it.
    """
    while True:
        try:
            if ser.in_waiting > 0:  # Check if there is data to read
                data = ser.readline().decode('utf-8').strip()
                print(f"GRBL: {data}")
        except Exception as e:
            print(f"Error reading from serial: {e}")
            break

def main():
    try:
        # Open the serial connection
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            print(f"Connected to {port} at {baud_rate} baud.")

            # Start a thread to continuously read from the serial port
            read_thread = threading.Thread(target=read_from_serial, args=(ser,))
            read_thread.daemon = True  # Ensure thread exits when the main program does
            read_thread.start()

            # Loop to send user input to the serial port
            while True:
                user_input = input("You: ")  # Input from user
                if user_input.lower() == "exit":
                    print("Exiting...")
                    break
                ser.write(f"{user_input}\n".encode('utf-8'))  # Send to GRBL

    except serial.SerialException as e:
        print(f"Could not open serial port: {e}")
    except KeyboardInterrupt:
        print("\nExiting on user interrupt.")

if __name__ == "__main__":
    main()
