*** Settings ***
Library    uart_library.py

*** Test Cases ***
Strict UART Firmware Validation
    Open Ports    COM6    COM7
    Sleep    3s

    ${sender_msg}=    Read From Sender
    ${receiver_msg}=    Read From Receiver

    Log    Sender: ${sender_msg}
    Log    Receiver: ${receiver_msg}

    Should Be Equal    ${sender_msg}    ${receiver_msg}

    Close Ports
