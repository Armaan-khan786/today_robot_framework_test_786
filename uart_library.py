import serial
import time

class UartLibrary:

    def __init__(self):
        self.sender = None
        self.receiver = None

    def open_ports(self, sender_port, receiver_port, baudrate=115200):
        self.sender = serial.Serial(sender_port, baudrate, timeout=2)
        self.receiver = serial.Serial(receiver_port, baudrate, timeout=2)
        time.sleep(2)

    def read_from_sender(self):
        if self.sender.in_waiting > 0:
            return self.sender.readline().decode().strip()
        return ""

    def read_from_receiver(self):
        if self.receiver.in_waiting > 0:
            return self.receiver.readline().decode().strip()
        return ""

    def close_ports(self):
        if self.sender:
            self.sender.close()
        if self.receiver:
            self.receiver.close()
