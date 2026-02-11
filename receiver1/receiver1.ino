// Receiver ESP32 - UART2
HardwareSerial MySerial(2); // UART2

void setup() {
  Serial.begin(115200);
  MySerial.begin(115200, SERIAL_8N1, 16, 17); // RX2=16, TX2=17 from sender
  delay(2000);
  Serial.println("RECEIVER READY");
}

void loop() {
  if(MySerial.available()){
    String msg = MySerial.readStringUntil('\n');
    msg.trim();
    if(msg.length() > 0){
      Serial.print("RECEIVED: ");
      Serial.println(msg);
    }
  }
}
