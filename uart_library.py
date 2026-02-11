import serial
import time


class uart_library:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.sender = None
        self.receiver = None

    # Robot keyword: Open Ports
    def open_ports(self):
        self.sender = serial.Serial("COM6", 115200, timeout=2)
        self.receiver = serial.Serial("COM7", 115200, timeout=2)

        time.sleep(2)

        self.sender.reset_input_buffer()
        self.receiver.reset_input_buffer()

        print("PORTS OPENED")

    # Robot keyword: Close Ports
    def close_ports(self):
        if self.sender:
            self.sender.close()
        if self.receiver:
            self.receiver.close()

        print("PORTS CLOSED")

    # Robot keyword: Read 100 Messages
    def read_100_messages(self):

        expected = [f"MSG_{i}" for i in range(1, 101)]
        received = []

        start_time = time.time()

        while len(received) < 100:

            if time.time() - start_time > 30:
                raise Exception("Timeout waiting for 100 messages")

            line = self.receiver.readline().decode(errors="ignore").strip()

            # Ignore ESP boot logs
            ignore_prefix = (
                "ets",
                "rst:",
                "boot:",
                "configsip",
                "clk_drv",
                "load:",
                "entry",
                ""
            )

            if line.startswith(ignore_prefix):
                continue

            if line.startswith("MSG_"):
                print(f"RECEIVED: {line}")
                received.append(line)

        if received != expected:
            raise Exception(f"Mismatch!\nExpected:\n{expected}\nReceived:\n{received}")

        return "ALL 100 MESSAGES VALIDATED SUCCESSFULLY"
