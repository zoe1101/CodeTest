def foo():
    for a in range(0, 101):
        for b in range(0, 101):
            if a + b == 100:
                yield a, b
if __name__ == '__main__':
    for item in foo():
        print(item)


# 通过命令行执行调用：python -m cProfile -s cumulative "cProfile --性能分析.py"