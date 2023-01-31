*** Settings ***

*** Test Cases ***
#当关键字失败时，Robot Framework 的默认行为是停止当前测试并执行其可能的拆卸。但是，在执行过程中也可能需要处理这些故障。Robot Framework 5.0为此引入了本地 TRY/EXCEPT 语法，但也有其他处理错误的方法。
#Robot Framework的 TRY/EXCEPT 语法受到 Python 异常处理语法的启发。它和 Python 有相同的 TRY、 EXCEPT、 ELSE 和 FINALLY 分支，而且它们的工作方式基本相同。不同之处在于 Python 使用小写的 try，但是对于 Robot Framework，所有这类语法都必须使用大写字母。一个更大的区别是，Python 异常是对象，而 Robot Framework 是将错误消息作为字符串处理。
EXCEPT匹配所有异常
    TRY
        Some Keyword
    EXCEPT  AS  ${error}
        Log To Console    ${error}
    ELSE
        Log To Console    No error occurred!
    FINALLY
        Log To Console    Always executed.
    END

使用 EXCEPT 捕获异常
    TRY
        Some Keyword
    EXCEPT    1 (string) != 1 (integer)
        Error Handler Keyword
    END

一个EXCEPT对应多个错误信息
    TRY
        Some Keyword
    EXCEPT    1 (string) != 1 (integer)    2 (string) != 2 (integer)    # Match any of these.
        Error Handler Keyword
    END

#默认情况下，使用 EXCEPT 匹配错误需要精确匹配。可以使用配置选项 type = 更改它，将其作为独立子句的参数。该选项的有效值是 GLOB、 REGEXP 或 START (不区分大小写) ，分别用于使匹配成为全局模式匹配、正则表达式匹配或仅匹配错误的开头。使用值 LITERAL 具有与默认行为相同的效果。如果 EXCEPT 有多个消息，则此选项将应用于所有消息。该选项的值也可以用变量定义。
#请记住，正则表达式中经常使用的反斜杠字符是 Robot Framework 数据中的转义字符。因此，在正则表达式中使用它时，需要使用另一个反斜杠来转义它。
使用模式匹配错误
#Glob pattern
    ${pattern}  Set Variable    11
    TRY
        Some Keyword
    EXCEPT    ValueError: *    type=GLOB
        Log To Console    ValueError
    EXCEPT    [Ee]rror ?? occurred    ${pattern}    type=glob
        Log To Console    [Ee]rror ?? occurred
    EXCEPT
        Log To Console    OTHER ERROR
    END

#Regular expression
    ${MATCH TYPE}  Set Variable     GLOB
    TRY
        Some Keyword
    EXCEPT    ValueError: .*    type=${MATCH TYPE}
        Log To Console    GLOB Error
    EXCEPT    [Ee]rror \\d+ occurred    type=Regexp    # Backslash needs to be escaped.
        Log To Console    Regular Error
    EXCEPT
        Log To Console    OTHER ERROR
    END

#Match start
    ${beginning}    Set Variable  1
    TRY
        Some Keyword
    EXCEPT    ValueError:    ${beginning}    type=start
        Log To Console    START Error
    EXCEPT
        Log To Console    OTHER ERROR
    END

#Explicit exact match
    TRY
        Some Keyword
    EXCEPT    ValueError: invalid literal for int() with base 10: 'ooops'    type=LITERAL
        Log To Console    ValueError: invalid literal for int() with base 10: 'ooops'
    EXCEPT    Error 13 occurred    type=LITERAL
        Log To Console    Error 13 occurred
    EXCEPT
        Log To Console    OTHER ERROR
    END
    
    
*** Keywords ***
Some Keyword
    Should Be Equal    1    ${1}

Error Handler Keyword
    Log To Console    两个变量不相等

