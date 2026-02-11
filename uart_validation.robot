*** Settings ***
Library    uart_library.py
Library    String

*** Test Cases ***
Validate Firmware Messages Cleanly
    Open Ports    COM6    COM7
    Sleep    3s

    WHILE    True
        ${s}=    Read From Sender
        ${r}=    Read From Receiver

        Run Keyword If    '${s}' == ''    Continue For Loop
        Run Keyword If    '${r}' == ''    Continue For Loop

        # Ignore ESP boot logs
        Run Keyword If    'ets ' in '${s}'    Continue For Loop
        Run Keyword If    'rst:' in '${s}'    Continue For Loop
        Run Keyword If    'load:' in '${s}'   Continue For Loop
        Run Keyword If    'entry ' in '${s}'  Continue For Loop

        # Ignore startup messages
        Run Keyword If    '${s}' == 'SENDER READY'    Continue For Loop
        Run Keyword If    '${r}' == 'RECEIVER READY'  Continue For Loop
        Run Keyword If    'SENDING 100 MESSAGES' in '${s}'    Continue For Loop

        # Stop when DONE comes
        Run Keyword If    '${s}' == 'DONE'    Exit For Loop

        # Clean RECEIVED prefix
        ${clean_r}=    Replace String    ${r}    RECEIVED:     ${EMPTY}
        ${clean_r}=    Strip String    ${clean_r}

        Log To Console    VALIDATING: ${s} == ${clean_r}
        Should Be Equal    ${s}    ${clean_r}
    END

    Close Ports
