*** Settings ***
Library    uart_library.py

Suite Setup    Open Ports
Suite Teardown    Close Ports

*** Test Cases ***
Validate All 100 Firmware Messages
    ${result}=    Read 100 Messages
    Log To Console    ${result}
