import serial


class UsbRelayBoard:
    def __init__(self, port, read_response=False, timeout=3):
        # Configurar el puerto serie
        self.port = serial.Serial(
            port=port,  # Cambia '/dev/ttyUSB0' al puerto serie que estés utilizando
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=timeout
        )
        self.read_response = read_response

    def turn_on(self, relay):
        self.turn_on_off(relay, 1)

    def turn_off(self, relay):
        self.turn_on_off(relay, 0)

    def turn_on_off(self, relay, value):
        """
        Function to activate/deactivate relays
        :param relay: Relay number (1..4)
        :param value: Value (0-Off, 1-On)
        :return: None
        """
        if relay < 1 or relay > 4:
            raise Exception ("Relay number not valid: " + str(relay))
        if value < 0 or value > 1:
            raise Exception("Value not valid: " + str(relay))

        data_to_send = bytes([0xFF, relay, value])
        self.send_data(data_to_send)

    def read_status(self, relay):
        """
        Read status of relay. NOT WORKING ON Board KMtronic V1.0 (it doesn't respond)
        :param relay: Relay number to read status (1..4)
        :return: None
        """
        self.old_read_response = self.read_response
        self.read_response = True

        data_to_send = bytes([0xFF, relay, 3])

        self.send_data(data_to_send)
        self.read_response = self.old_read_response

    def send_data(self, data):
        """
        Sends data bytes to configured port
        :param data: bytes to send
        :return: None
        """
        try:
            if not self.port.is_open:
                self.port.open()

            # Send data
            self.port.write(data)
            print(f"Bytes sent: {data.hex()}")

            if self.read_response:
                # Read response
                response = self.port.read(3)
                print(f"Response received: {response.hex()}")

        except Exception as e:
            print(f"Error when sending data: {e}")
        finally:
            self.port.close()

