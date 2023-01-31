#有时候，关键字可能需要非常长的时间来执行，或者只是无休止地挂起。Robot Framework 允许您为测试用例和用户关键字设置超时，如果一个测试或关键字没有在指定的时间内完成，则当前正在执行的关键字将被强制停止。
#以这种方式停止关键字可能会使库、测试环境或被测系统处于不稳定状态，只有在没有更安全的选项可用时才建议超时。一般来说，应该实现库，以便关键字不能挂起，或者它们有自己的超时机制。


#测试用例超时可以通过使用设置部分中的 Test Timeout 设置或针对单个测试用例的[ Timeout ]设置来设置。Test Timeout 为该套件中的所有测试用例定义了默认超时，而[ Timeout ]对特定测试用例应用了超时，并覆盖了可能的默认值。


*** Settings ***
#对所有案例都有效
Test Timeout       2 minutes

*** Variables ***

*** Test Cases ***
Default timeout
    [Documentation]    Default timeout from Settings is used.
    Some Keyword    argument

Override
    [Documentation]    Override default, use 10 seconds timeout.
    [Timeout]    10
    Some Keyword    argument

Variables
    [Documentation]    It is possible to use variables too.
    [Timeout]    ${TIMEOUT}
    Some Keyword    argument

No timeout
    [Documentation]    Empty timeout means no timeout even when Test Timeout has been used.
    [Timeout]
    Some Keyword    argument

No timeout 2
    [Documentation]    Disabling timeout with NONE works too and is more explicit.
    [Timeout]    NONE
    Some Keyword    argument