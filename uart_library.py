import serial
import time

sender = None
receiver = None

def open_ports(sender_port, receiver_port, baudrate=115200):
    global sender, receiver
    sender = serial.Serial(sender_port, baudrate, timeout=2)
    receiver = serial.Serial(receiver_port, baudrate, timeout=2)
    time.sleep(2)

def read_from_sender():
    global sender
    if sender and sender.in_waiting > 0:
        return sender.readline().decode().strip()
    return ""

def read_from_receiver():
    global receiver
    if receiver and receiver.in_waiting > 0:
        return receiver.readline().decode().strip()
    return ""

def close_ports():
    global sender, receiver
    if sender:
        sender.close()
    if receiver:
        receiver.close()
