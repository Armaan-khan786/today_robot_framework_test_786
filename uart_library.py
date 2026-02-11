import serial
import time


class UartLibrary:

    def __init__(self):
        self.sender = None
        self.receiver = None

    # --------------------------------------------
    # OPEN PORTS
    # --------------------------------------------
    def open_ports(self):
        self.sender = serial.Serial("COM6", 115200, timeout=2)
        self.receiver = serial.Serial("COM7", 115200, timeout=2)

        time.sleep(2)

        self.sender.reset_input_buffer()
        self.receiver.reset_input_buffer()

    # --------------------------------------------
    # CLOSE PORTS
    # --------------------------------------------
    def close_ports(self):
        if self.sender:
            self.sender.close()
        if self.receiver:
            self.receiver.close()

    # --------------------------------------------
    # READ CLEAN LINE
    # --------------------------------------------
    def read_clean_line(self):
        line = self.receiver.readline().decode(errors="ignore").strip()

        # Ignore ESP32 boot logs
        ignore_words = [
            "ets",
            "rst:",
            "boot:",
            "configsip",
            "clk_drv",
            "load:",
            "entry",
            ""
        ]

        for word in ignore_words:
            if line.startswith(word):
                return None

        return line

    # --------------------------------------------
    # READ 100 VALID MESSAGES
    # --------------------------------------------
    def read_100_messages(self):

        expected = [f"MSG_{i}" for i in range(1, 101)]
        received = []

        start_time = time.time()

        while len(received) < 100:

            if time.time() - start_time > 30:
                raise Exception("Timeout waiting for 100 messages")

            line = self.read_clean_line()

            if line and line.startswith("MSG_"):
                print(f"RECEIVED: {line}")
                received.append(line)

        # STRICT VALIDATION
        if received != expected:
            raise Exception(f"Mismatch!\nExpected:\n{expected}\nReceived:\n{received}")

        return "ALL 100 MESSAGES VALIDATED SUCCESSFULLY"
