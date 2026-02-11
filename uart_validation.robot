*** Settings ***
Library    uart_library.py

Suite Setup    Open Ports
Suite Teardown    Close Ports

*** Test Cases ***
Validate All 100 Firmware Messages
    Read All 100 Messages
