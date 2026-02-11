*** Settings ***
Library    uart_library.py
Library    String
Library    Collections

*** Variables ***
@{EXPECTED}    FLASH_ESP32    BLINK_LED_ON    BLINK_LED_OFF    POWER_ON_ESP    POWER_OFF_ESP    CHECK_UART    UPLOAD_FIRMWARE    ERASE_FLASH    READ_MAC_ADDRESS    RESET_DEVICE

*** Test Cases ***
Validate Receiver Firmware Messages
    ${received_count}=    Set Variable    0

    WHILE    ${received_count} < 10
        ${r}=    Read From Receiver
        Run Keyword If    '${r}' == ''    Continue For Loop

        ${clean}=    Replace String    ${r}    RECEIVED:     ${EMPTY}
        ${clean}=    Strip String    ${clean}

        ${is_valid}=    Evaluate    "${clean}".isupper() and "_" in "${clean}"
        Run Keyword If    not ${is_valid}    Continue For Loop

        Log To Console    VALID FIRMWARE: ${clean}
        List Should Contain Value    ${EXPECTED}    ${clean}

        ${received_count}=    Evaluate    ${received_count} + 1
    END
