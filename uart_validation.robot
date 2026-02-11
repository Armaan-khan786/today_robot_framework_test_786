*** Settings ***
Library    uart_library.py

*** Test Cases ***
Validate All Firmware Messages Properly
    Open Ports    COM6    COM7
    Sleep    3s

    ${started}=    Set Variable    False

    WHILE    True
        ${s}=    Read From Sender
        ${r}=    Read From Receiver

        # Ignore empty lines
        Run Keyword If    '${s}' == ''    Continue For Loop
        Run Keyword If    '${r}' == ''    Continue For Loop

        # Ignore READY messages
        Run Keyword If    '${s}' == 'SENDER READY'    Continue For Loop
        Run Keyword If    '${r}' == 'RECEIVER READY'  Continue For Loop

        # If DONE received, stop loop
        Run Keyword If    '${s}' == 'DONE'    Exit For Loop

        Log To Console    VALIDATING: ${s} == ${r}
        Should Be Equal    ${s}    ${r}

    END

    Close Ports
