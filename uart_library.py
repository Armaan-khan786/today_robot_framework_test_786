import serial
import time

class UartLibrary:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, sender_port='COM6', receiver_port='COM7', baud=115200):
        self.sender_port = sender_port
        self.receiver_port = receiver_port
        self.baud = baud
        self.receiver = None

    # Robot sees this as keyword "Open Ports"
    def open_ports(self):
        """Open the receiver COM port"""
        self.receiver = serial.Serial(self.receiver_port, self.baud, timeout=1)
        time.sleep(2)

    # Robot sees this as keyword "Close Ports"
    def close_ports(self):
        """Close the receiver COM port"""
        if self.receiver and self.receiver.is_open:
            self.receiver.close()

    # Robot sees this as keyword "Read All 100 Messages"
    def read_all_100_messages(self):
        """Read and validate 100 firmware messages from ESP32"""
        expected_messages = [
            "FLASH_ESP32","BLINK_LED_ON","BLINK_LED_OFF","POWER_ON_ESP","POWER_OFF_ESP",
            # ... continue all 100 messages
            "START_SEQUENCE","END_SEQUENCE"
        ]

        received = []
        start_time = time.time()
        ignore_prefix = ("ets", "rst", "boot", "configsip", "clk_drv", "load", "entry")

        while len(received) < 100:
            if self.receiver.in_waiting:
                line = self.receiver.readline().decode(errors='ignore').strip()
                if line and not line.lower().startswith(ignore_prefix):
                    print(f"VALIDATING: {line}")
                    received.append(line)
            if time.time() - start_time > 60:
                raise Exception(f"Timeout waiting for 100 messages. Only received {len(received)}")

        # Compare each message
        for i, msg in enumerate(expected_messages):
            if received[i] != msg:
                raise Exception(f"Message {i+1} mismatch: expected '{msg}' got '{received[i]}'")
