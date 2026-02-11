import serial
import time

sender = None
receiver = None

def open_ports(sender_port, receiver_port, baudrate=115200):
    global sender, receiver
    sender = serial.Serial(sender_port, baudrate, timeout=2)
    receiver = serial.Serial(receiver_port, baudrate, timeout=2)
    time.sleep(2)
    print("PORTS OPENED")

def read_from_sender():
    global sender
    if sender and sender.in_waiting > 0:
        msg = sender.readline().decode(errors='ignore').strip()
        if msg != "":
            print(f"SENDER SENT: {msg}")
        return msg
    return ""

def read_from_receiver():
    global receiver
    if receiver and receiver.in_waiting > 0:
        msg = receiver.readline().decode(errors='ignore').strip()
        if msg != "":
            print(f"RECEIVER GOT: {msg}")
        return msg
    return ""

def close_ports():
    global sender, receiver
    if sender:
        sender.close()
    if receiver:
        receiver.close()
    print("PORTS CLOSED")
