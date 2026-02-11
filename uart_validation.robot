*** Settings ***
Library    uart_library.py
Library    String
Library    Collections

*** Variables ***
@{EXPECTED}
...    FLASH_ESP32
...    BLINK_LED_ON
...    BLINK_LED_OFF
...    POWER_ON_ESP
...    POWER_OFF_ESP
...    CHECK_UART
...    UPLOAD_FIRMWARE
...    ERASE_FLASH
...    READ_MAC_ADDRESS
...    RESET_DEVICE

*** Test Cases ***
Validate Receiver Firmware Messages
    Open Ports    COM6    COM7
    Sleep    3s

    ${received_count}=    Set Variable    0

    WHILE    ${received_count} < 10
        ${r}=    Read From Receiver

        Run Keyword If    '${r}' == ''    Continue For Loop

        # Clean prefix
        ${clean}=    Replace String    ${r}    RECEIVED:     ${EMPTY}
        ${clean}=    Strip String    ${clean}

        Run Keyword If    '${clean}' == ''    Continue For Loop

        Log To Console    RECEIVED: ${clean}

        List Should Contain Value    ${EXPECTED}    ${clean}

        ${received_count}=    Evaluate    ${received_count} + 1
    END

    Close Ports
