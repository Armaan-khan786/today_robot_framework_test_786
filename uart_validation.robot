*** Settings ***
Library    uart_library.py

*** Test Cases ***
Validate Firmware Messages Cleanly
    Open Ports    COM6    COM7
    Sleep    3s

    WHILE    True
        ${s}=    Read From Sender
        ${r}=    Read From Receiver

        # Ignore empty lines
        Run Keyword If    '${s}' == ''    Continue For Loop
        Run Keyword If    '${r}' == ''    Continue For Loop

        # Ignore boot logs
        Run Keyword If    'ets ' in '${s}'    Continue For Loop
        Run Keyword If    'rst:' in '${s}'    Continue For Loop
        Run Keyword If    'load:' in '${s}'   Continue For Loop
        Run Keyword If    'entry ' in '${s}'  Continue For Loop
        Run Keyword If    'SENDING 100 MESSAGES' in '${s}'    Continue For Loop

        # Stop when DONE
        Run Keyword If    '${s}' == 'DONE'    Exit For Loop

        # Clean receiver prefix
        ${clean_r}=    Replace String    ${r}    RECEIVED:     ${EMPTY}
        ${clean_r}=    Strip String    ${clean_r}

        Log To Console    VALIDATING: ${s} == ${clean_r}
        Should Be Equal    ${s}    ${clean_r}

    END

    Close Ports
