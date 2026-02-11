*** Test Cases ***
Validate Receiver Firmware Messages
    FOR    ${i}    IN RANGE    20
        ${r}=    Read From Receiver
        Run Keyword If    '${r}' == ''    Continue For Loop

        ${clean}=    Replace String    ${r}    RECEIVED:     ${EMPTY}
        ${clean}=    Strip String    ${clean}

        Log To Console    RECEIVED CLEAN: ${clean}

        List Should Contain Value    ${EXPECTED}    ${clean}
    END
