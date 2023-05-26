import jmespath

test_data = {"a": "foo", "b": "bar", "c": "baz"}
print(jmespath.search("a", test_data))  # foo

test_data = {
    "book": [
        {"name": "平凡的世界", "author": "路遥", "sort": 3},
        {"name": "围城", "author": "钱钟书", "sort": 2},
        {"name": "围城", "author": "钱钟书", "sort": 2},
        {"name": "活着", "author": "余华", "sort": 1},
        {"name": "麦田里的守望者", "author": "塞林格", "sort": 4},
        {"name": "挪威的森林", "author": "村上春树", "sort": 5}
    ]
}
print(jmespath.search("book[*]", test_data))  # 源数据
print(jmespath.search("book[1:3]",
                      test_data))  # 切片,[{'name': '围城', 'author': '钱钟书', 'sort': 2}, {'name': '围城', 'author': '钱钟书', 'sort': 2}]
print(jmespath.search("book[?name=='活着']", test_data))  # 数据筛选。结果：[{'name': '活着', 'author': '余华', 'sort': 1}]
print(jmespath.search("book[*].name", test_data))  # ['平凡的世界', '围城', '围城', '活着', '麦田里的守望者', '挪威的森林']
print(jmespath.search("book[*].[name,sort]",
                      test_data))  # 多选列表， [['平凡的世界', 3], ['围城', 2], ['围城', 2], ['活着', 1], ['麦田里的守望者', 4], ['挪威的森林', 5]]
print(jmespath.search("book[].{name:name, sort:sort}",
                      test_data))  # 多选对象， [{'name': '平凡的世界', 'sort': 3}, {'name': '围城', 'sort': 2}, {'name': '围城', 'sort': 2}, {'name': '活着', 'sort': 1}, {'name': '麦田里的守望者', 'sort': 4}, {'name': '挪威的森林', 'sort': 5}]
print(jmespath.search("book[*].name | [1]", test_data))  # 管道表达式,结果：围城
print(jmespath.search("book[0] | values(@)", test_data))  # 只取值，结果：['平凡的世界', '路遥', 3]
print(jmespath.search("book[*].sort | sort(@)", test_data))  # 取sort值，并根据sort字段值进行排序。结果：[1, 2, 2, 3, 4, 5]
print(jmespath.search("book[*].author | sort(@) | [join(', ', @)]",
                      test_data))  # 取author值，并根据author字段值进行排序，最后通过逗号拼接成字符串。结果：['余华, 塞林格, 村上春树, 路遥, 钱钟书, 钱钟书']
print(jmespath.search("sort_by(book,&sort)", test_data))  # 排序,按照sort字段排序

test_data = {
    "myarray": [
        "foo",
        "foobar",
        "barfoo",
        "bar",
        "baz",
        "barbaz",
        "barfoobaz"
    ]
}
print(jmespath.search("myarray[?contains(@,'foo')]",
                      test_data))  # 过滤器表达式，包含提取，结果：['foo', 'foobar', 'barfoo', 'barfoobaz']
