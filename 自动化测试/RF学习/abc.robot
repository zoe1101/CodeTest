*** Settings ***

*** Variables ***

*** Test Cases ***
abcjdk
    ${a}    set variable    123
    log to console    ${a}
    ${b}    Create List    1    2    3
    log to console    ${b}
