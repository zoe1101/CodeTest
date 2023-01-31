*** Settings ***
Library  Collections

*** Test Cases ***
使用多个循环变量
    FOR    ${index}    ${english}    ${finnish}    IN
    ...    1           cat           kissa
    ...    2           dog           koira
    ...    3           horse         hevonen
        Log To Console    ${english}-> ${finnish}->${index}
    END
    ${EMPLOYERS}  Create List     张三  1
    FOR    ${name}    ${id}    IN    @{EMPLOYERS}
        Log To Console    ${name}->${id}
    END

FOR-IN-RANGE循环
    FOR  ${i}  IN RANGE  ${10}
        LOG TO CONSOLE  ${i}
    END
    FOR  ${i}  IN RANGE  ${5}  ${10}
        LOG TO CONSOLE  ${i}
    END
    FOR  ${i}  IN RANGE  ${1}  ${10}  ${3}
        LOG TO CONSOLE  ${i}
    END

FOR-IN-ENUMERATE循环
    comment  循环迭代某个列表,同时又跟踪当前元素在列表中的位置
    @{LIST}  create list  1    2    3    4
    FOR    ${index}    ${item}  IN ENUMERATE   @{LIST}
        LOG TO CONSOLE  ${index}->${item}
    END

FOR-IN-ENUMERATE with start
    Comment   Start=<index> 语法必须在 FOR 头中显式使用
    @{LIST}   Create List     a    b    c
    ${START}    Set Variable    10
    FOR    ${index}    ${item}    IN ENUMERATE    @{LIST}    start=1
        Log To Console    ${index}->${item}
    END
#    Start as variable
    FOR    ${index}    ${item}    IN ENUMERATE    @{LIST}    start=${start}
        Log To Console     ${index}->${item}
    END

FOR-IN-ZIP循环
    comment  将几个相关的列表并在一起处理
    ${key}  create list     ${1}    ${2}    ${3}    ${4}
    ${val}  create list     a    b    c    d
    FOR    ${k}    ${v}  IN ZIP   ${key}  ${val}
        Log To Console  ${k}->${v}
    END

FOR-IN-ZIP with multiple lists
    @{ABC}    create list       a    b    c
    @{XYZ}    create list       x    y    z
    @{NUM}    create list       1    2    3    4    5
    FOR    ${a}    ${x}    ${n}    IN ZIP    ${ABC}    ${XYZ}    ${NUM}
        Log To Console   ${a}->${x}->${n}
    END

FOR-IN-ZIP with one variable
    @{ABC}    create list       a    b    c
    @{XYZ}    create list       x    y    z
    @{NUM}    create list       1    2    3    4    5
    FOR    ${items}    IN ZIP    ${ABC}    ${XYZ}    ${NUM}
        Length Should Be    ${items}    3
        Log To Console    ${items}[0]->${items}[1]->${items}[2]
    END

#普通的 FOR 循环和 FOR-IN-ENUMERATE 循环支持对字典中的键和值进行迭代。此语法要求至少一个循环值为字典变量。可以使用多个字典变量，并在 key = value 语法中给出其他项。按照定义的顺序迭代项，如果同一个键获得多个值，则使用最后一个值。
FOR循环迭代字典
    &{dict}  create dictionary    a=1    b=2    c=3
    FOR    ${item}  IN   &{dict}
        LOG TO CONSOLE  key=${item}[0],val=${item}[1]
    END
    FOR    ${k}    ${v}  IN   &{dict}
        LOG TO CONSOLE  ${k}=${v}
    END
    FOR    ${i}  ${k}    ${v}  IN ENUMERATE  &{dict}
        LOG TO CONSOLE  索引位置${i}的元素是${k}=${v}
    END
    FOR    ${item}  IN ENUMERATE  &{dict}
        length should be  ${item}  ${3}
    END
    FOR    ${key}   IN    @{dict}   #对键进行迭代,要求使用字典作为列表变量
        LOG TO CONSOLE   Key is '${key}' and value is '${dict}[${key}]'.
    END

FOR循环迭代多个字典
    comment  如果多次使用相同的键，则使用最后一个值，但保留键的原始顺序。
    &{dict1}  create dictionary    a=1    b=2    c=3
    &{dict2}  create dictionary    c=1    d=2    e=3
    FOR    ${k}    ${v}  IN   &{dict1}    &{dict2}
        LOG TO CONSOLE  ${k}=${v}
    END



FOR循环支持直接嵌套
    FOR    ${i}  IN RANGE  ${5}
        FOR    ${j}  IN RANGE  ${5}
            IF    1!=1
                log to console  ${i},${j},FAIL
            ELSE
                log to console  ${i},${j},PASS
            END
        END
    END


#BREAK 和 CONTINUE 语句在 Robot Framework 5.0中是新的，类似于 WHILE。早期版本支持使用内置关键字 Exit FOR Loop、 Exit FOR Loop If、 ContinuforLoop 和 ContinuforLoop If 来控制 FOR 循环。这些关键字仍在继续工作，但将来会被弃用和删除。
提前退出FOR循环-break
  comment  调用 BuiltIn_ 关键字 Exit For Loop 和 Exit For Loop If. 它们的作用类似于编程语言中的 break 语句.
    ${text}  set variable  &{EMPTY}
    FOR    ${v}  IN   one  two
        log to console  ${v}
        exit for loop if  '${v}'=='two'
        ${text} =  set variable  ${text}${v}
    END
    should be equal  ${text}  one

继续FOR循环-continue
  comment  使用 BuiltIn_ 关键字 Continue For Loop 和 Continue For Loop If
    ${text}  set variable  &{EMPTY}
    FOR    ${v}  IN   one  two  three
        log to console  ${v}
        continue for loop if   '${v}'=='two'
        ${text} =  set variable  ${text}${v}
    END
    should be equal  ${text}  onethree



条件执行
    ${v}  set variable  ${3}
    ${RES}  SET VARIABLE  NONE
    IF  ${v}<${3}
        ${RES}=  SET VARIABLE  -1
    ELSE IF  ${v}==${3}
        ${RES}=  SET VARIABLE  0
    ELSE
        ${RES}=  SET VARIABLE  1
    END
    LOG TO CONSOLE  ${RES}

重复单个关键字
    Repeat Keyword    5    Some Keyword    arg1    arg2
    Repeat Keyword    4 times    My Keyword
    ${var}  Set Variable  5
    Repeat Keyword    ${var}    Another Keyword    argument


WHILE迭代限制
    #Limit as iteration count
    WHILE    True    limit=100
        Log    This is run 100 times.
    END
    #Limit as time
    WHILE    True    limit=10 seconds
        Log    This is run 10 seconds.
    END
#    No limit
    WHILE    True    limit=NONE
        Log    This must be forcefully stopped.
    END

嵌套WHILE循环
    ${x} =   Set Variable    10
    WHILE    ${x} > 0
        ${y} =   Set Variable    ${x}
        WHILE    ${y} > 0
            ${y} =    Evaluate    ${y} - 1
        END
        IF    ${x} > 5
            ${x} =    Evaluate    ${x} - 1
        ELSE
            ${x} =    Evaluate    ${x} - 2
        END
    END

*** Keywords ***
Some Keyword
    [Arguments]     ${arg1}   ${arg2}
    Log To Console    Some Keyword=${arg1},${arg2}

My Keyword
    Log To Console    My Keyword

Another Keyword
    [Arguments]     ${argument}
    Log To Console    Another Keyword=${argument}