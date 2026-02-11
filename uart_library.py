import serial
import time

class UartLibrary:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, sender_port='COM6', receiver_port='COM7', baud=115200):
        self.sender_port = sender_port
        self.receiver_port = receiver_port
        self.baud = baud
        self.receiver = None

    def open_ports(self):
        self.receiver = serial.Serial(self.receiver_port, self.baud, timeout=1)
        time.sleep(2)

    def close_ports(self):
        if self.receiver and self.receiver.is_open:
            self.receiver.close()

    def read_all_100_messages(self):
        expected_messages = [
            "FLASH_ESP32","BLINK_LED_ON","BLINK_LED_OFF","POWER_ON_ESP","POWER_OFF_ESP",
            "CHECK_UART","UPLOAD_FIRMWARE","ERASE_FLASH","READ_MAC_ADDRESS","RESET_DEVICE",
            "ENABLE_WIFI","DISABLE_WIFI","SCAN_WIFI","CONNECT_WIFI","DISCONNECT_WIFI",
            "ENABLE_BLUETOOTH","DISABLE_BLUETOOTH","START_BLE","STOP_BLE","CHECK_SIGNAL",
            "READ_TEMPERATURE","READ_HUMIDITY","READ_PRESSURE","START_ADC","STOP_ADC",
            "START_DAC","STOP_DAC","ENABLE_PWM","DISABLE_PWM","SET_PWM_DUTY",
            "START_TIMER","STOP_TIMER","RESET_TIMER","ENABLE_INTERRUPT","DISABLE_INTERRUPT",
            "CHECK_GPIO_STATUS","SET_GPIO_HIGH","SET_GPIO_LOW","READ_GPIO","CONFIGURE_PIN",
            "ENABLE_SPI","DISABLE_SPI","ENABLE_I2C","DISABLE_I2C","ENABLE_UART2","DISABLE_UART2",
            "CHECK_MEMORY","READ_FLASH","WRITE_FLASH","CHECK_BOOTLOADER",
            "ENTER_SLEEP_MODE","EXIT_SLEEP_MODE","ENABLE_DEEP_SLEEP","WAKE_FROM_SLEEP","CHECK_BATTERY",
            "ENABLE_RTC","DISABLE_RTC","SYNC_TIME","GET_SYSTEM_TIME","SET_SYSTEM_TIME",
            "ENABLE_WDT","DISABLE_WDT","RESET_WDT","CHECK_WDT_STATUS","ENABLE_LOGGING",
            "DISABLE_LOGGING","READ_LOGS","CLEAR_LOGS","CHECK_FIRMWARE_VERSION","UPDATE_FIRMWARE",
            "ENABLE_SECURITY","DISABLE_SECURITY","CHECK_ENCRYPTION","ENABLE_TLS","DISABLE_TLS",
            "START_HTTP_SERVER","STOP_HTTP_SERVER","START_MQTT","STOP_MQTT","CHECK_NETWORK_STATUS",
            "ENABLE_SENSOR_MODE","DISABLE_SENSOR_MODE","CALIBRATE_SENSOR","RESET_SENSOR","START_STREAM",
            "STOP_STREAM","CHECK_STORAGE","FORMAT_STORAGE","ENABLE_DEBUG","DISABLE_DEBUG",
            "SYSTEM_STATUS","DEVICE_INFO","HARDWARE_CHECK","SOFTWARE_CHECK","FINALIZE_PROCESS",
            "REBOOT_DEVICE","SAFE_MODE","NORMAL_MODE","START_SEQUENCE","END_SEQUENCE"
        ]

        received = []
        start_time = time.time()

        while len(received) < 100:
            if self.receiver.in_waiting:
                line = self.receiver.readline().decode(errors='ignore').strip()
                if line and not line.lower().startswith(("ets", "rst", "boot", "configsip", "clk_drv", "load", "entry")):
                    print(f"VALIDATING: {line}")
                    received.append(line)
            if time.time() - start_time > 60:  # 60 sec timeout
                raise Exception(f"Timeout waiting for 100 messages. Only received {len(received)}")

        # Compare each message
        for i, msg in enumerate(expected_messages):
            if received[i] != msg:
                raise Exception(f"Message {i+1} mismatch: expected '{msg}' got '{received[i]}'")
