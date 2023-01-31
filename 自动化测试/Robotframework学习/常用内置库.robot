*** Settings ***
Documentation  一个例子说明RF常用关键字的使用
Force Tags  测试套件标签
Default Tags  RF常用关键字
Suite Setup  Suite Start
Suite Teardown  Suite End
Library  Screenshot

*** Variables ***
${START_EORD}                   测试开始
${END_WORD}                     测试结束

*** Test Cases ***
test_01
    [Documentation]             Robotframework中打印使用 “log”
    [Tags]                      test 1.0
    [Setup]                     Test Start
    log                         holle Robotframework
    [Teardown]                  Test Down

test_02
    [Documentation]             测试定义变量
    [Tags]                      test 1.0
    Set Variable

test_03
    [Documentation]             测试连接多个信息
    [Tags]                      test 1.0
    Catenate variables

test_04
    [Documentation]             测试创建列表变量
    [Tags]                      test 1.0
    Create List Data

test_05
    [Documentation]             测试RF时间操作
    [Tags]                      test 1.0
    [Setup]                     Test Start
    Time Operation
    [Teardown]                  Test Down

test_06
    [Documentation]             测试if关键字
    [Tags]                      test 1.0
    [Setup]                     Test Start
    IF Keyword
    [Teardown]                  Test Down

test_07
    [Documentation]             测试FOR关键字
    [Tags]                      test 1.0
    [Setup]                     Test Start
    FOR Keyword
    [Teardown]                  Test Down

test_08
    [Documentation]             Evaluate关键字测试
    [Tags]                      test 1.0
    Evaluate Keyword



*** Keywords ***
Suite Start
    [Documentation]             开始运行测试套件
    log                         ${START_EORD}

Suite End
    [Documentation]             测试套件运行结束
    log                         ${END_WORD}

Test Start
    [Documentation]             测试开始前执行的动作
    log                         测试开始前执行的动作

Test Down
    [Documentation]             测试用例执行完毕后执行的动作
    log                         测试用例执行完毕后执行的动作

Set Variable
    [Documentation]             FR定义变量
    ${a}    BuiltIn.Set Variable    1234
    log    ${a}

Catenate variables
    [Documentation]             连接多个信息
    ${content1}    Catenate     Holle    World!!!
    log    ${content1}
    ${content2}    Catenate    SEPARATOR=^^^    你好    中国
    log    ${content2}

Create List Data
    [Documentation]             创建列表变量
    ${list_data1}    Create List    1    2    3    4
    log    ${list_data1}
    @{list_data2}    Create List    a    b    c    d
    BuiltIn.log Many    @{list_data2}

Time Operation
    [Documentation]             RF时间操作
    ${time}    Get Time                     # 获取当前时间，年-月-日 时:分:秒
    log    ${time}
    ${secs}    Get Time    epoch            # 获取当前时间的描述
    log    ${secs}
    ${year}    Get Time    return year      # 获取当前的年份
    log    ${year}
    ${yyyy}    ${mm}    ${dd}=    Get Time    year,month,day    # 获得年月日的分别变量值
    log    ${yyyy}
    log    ${mm}
    log    ${dd}
    @{time}    Get Time    year month day hour min secs       # 获得年月日时分秒的列表参数
    BuiltIn.Log Many    @{time}
    ${s}    Get Time    seconds     # 获取秒数
    log    ${s}
    ${y}    Get Time    year    # 获取年数
    log     ${y}
    log     等到时间3秒
    Sleep    3

IF Keyword
    [Documentation]             if关键字
    ${age}    BuiltIn.Set Variable    10
    run Keyword if    ${age}>=90    log    老年人
    ...               ELSE IF    ${age}>=50    log    中年人
    ...               ELSE IF    ${age}>=20    log    青年人
    ...               ELSE    log    小孩子

FOR Keyword
    [Documentation]             for关键字
    :FOR    ${i}    INRANGE    10        # 打印0-9的数
    \     log    ${i}
    :FOR    ${ii}    in range    1    11   # 打印1-10的数
    \        log    ${ii}
    :FOR    ${iii}    in range   1    11    2    # 答应1,3,5,7,9
    \        log    ${iii}
    @{my_list}    Create List    q    w    e    r    t    # 遍历列表
    :FOR    ${iiii}    in    @{my_list}
    \        log    ${iiii}
    @{abc}    Create List    1    2    3    4    # 循环中判断
    :FOR    ${f}    in    @{abc}
    \        Exit for loop if    '${f}'=='2'
    log    ${f}

Evaluate Keyword
    [Documentation]             强大的Evaluate关键字
    ${d}    Evaluate    int(2)
    log    ${d}
    ${len}    Evaluate    type(${d})
    log    ${len}
    Take Screenshot    # 截屏
    ${dd}    Evaluate    random.randint(1, 10000)    random     # 格式为： 变量名  Evaluate(关键字)  函数   需要import的包（类型python导入包）
    log    ${dd}
    Evaluate    os.system('python3 C:/MYTEST/VScode_Spider/Test/test_格式化日期输出.py')    os
