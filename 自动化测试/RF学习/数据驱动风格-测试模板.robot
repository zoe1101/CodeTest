*** Settings ***

*** Test Cases ***
关键字名称中嵌入参数
    [Template]    ${计算表达式}运算结果为${expected}
    1+1   2
    2+1   3

*** Keywords ***
${计算表达式}运算结果为${expected}
    ${actual}  evaluate  ${计算表达式}
    should be equal as strings  ${actual}  ${expected}
