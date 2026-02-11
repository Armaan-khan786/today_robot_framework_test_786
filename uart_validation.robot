*** Settings ***
Library    uart_library.py

*** Test Cases ***
Strict UART Firmware Validation
    Open Ports    COM6    COM7
    Sleep    3s

    ${s}=    Read From Sender
    ${r}=    Read From Receiver

    Log    Sender: ${s}
    Log    Receiver: ${r}

    Close Ports
