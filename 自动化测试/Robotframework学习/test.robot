*** Settings ***

*** Variables ***

*** Test Cases ***
testcase
    ${a}    set variable    123
    log to console    ${a}
    ${b}    Create List    1    2    3
    log to console    ${b}
    ${index} =    Set Variable    -1
    Log To Console    ${index}
