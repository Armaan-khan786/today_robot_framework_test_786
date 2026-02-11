import serial
import time

class UartLibrary:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, receiver_port='COM7', baud=115200):
        self.receiver_port = receiver_port
        self.baud = baud
        self.receiver = None

    def open_ports(self):
        """Open the receiver COM port"""
        self.receiver = serial.Serial(self.receiver_port, self.baud, timeout=1)
        time.sleep(2)

    def close_ports(self):
        """Close the receiver COM port"""
        if self.receiver and self.receiver.is_open:
            self.receiver.close()

    def read_all_100_messages(self):
        """Read 100 firmware messages"""
        expected_messages = [
            "FLASH_ESP32","BLINK_LED_ON","BLINK_LED_OFF","POWER_ON_ESP","POWER_OFF_ESP",
            # Add all 100 messages here
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

        for i, msg in enumerate(expected_messages):
            if received[i] != msg:
                raise Exception(f"Message {i+1} mismatch: expected '{msg}' got '{received[i]}'")
