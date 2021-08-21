*** Settings ***
Library  Collections
*** Test Cases ***
使用多个循环变量
    FOR  ${index} ${v1}  ${v2}  IN
    ...  1  cat  kissa
    ...  2  dog  koira
    ...  3  horse  hevonen
        add to dictionary  ${v1}  ${v2}  ${index}
    END
    FOR  ${name} ${id}  IN  @{dic}
        create ${name}  ${id}
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
        LOG TO CONSOLE  ${index}+${item}
    END

FOR-IN-ZIP循环
    comment  将几个相关的列表并在一起处理
    @{key}  create list  ${1}    ${2}    ${3}    ${4}
    @{val}  create list  a    b    c    d
    FOR    ${k}    ${v}  IN ZIP   @{key}  @{val}
        LOG TO CONSOLE  ${k}=${v}
    END

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

