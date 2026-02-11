*** Settings ***
Library    uart_library.py

*** Test Cases ***
Strict UART Firmware Validation
    Open Ports    COM6    COM7
    Sleep    3s

    ${sender}=    Read From Sender
    ${receiver}=  Read From Receiver

    Log    Sender: ${sender}
    Log    Receiver: ${receiver}

    Should Be Equal    ${sender}    ${receiver}

    Close Ports
