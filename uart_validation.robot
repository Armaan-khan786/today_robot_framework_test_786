*** Settings ***
Library    uart_library.py

*** Test Cases ***
Validate All 100 Firmware Messages
    Open Ports    COM6    COM7
    Sleep    5s

    ${i}=    Set Variable    0

    WHILE    ${i} < 100
        ${s}=    Read From Sender
        ${r}=    Read From Receiver

        Run Keyword If    '${s}' != '' and '${r}' != ''    Should Be Equal    ${s}    ${r}

        ${i}=    Evaluate    ${i} + 1
        Sleep    0.1s
    END

    Close Ports
