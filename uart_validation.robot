WHILE    ${received_count} < 10
    ${r}=    Read From Receiver

    Run Keyword If    '${r}' == ''    Continue For Loop

    ${clean}=    Replace String    ${r}    RECEIVED:     ${EMPTY}
    ${clean}=    Strip String    ${clean}

    # Ignore boot logs (if contains lowercase or space)
    ${is_valid}=    Evaluate    "${clean}".isupper() and "_" in "${clean}"

    Run Keyword If    not ${is_valid}    Continue For Loop

    Log To Console    VALID FIRMWARE: ${clean}

    List Should Contain Value    ${EXPECTED}    ${clean}

    ${received_count}=    Evaluate    ${received_count} + 1
END
