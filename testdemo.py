def func(N):
    def func1(N):
        if N < 1:
            return
        if N <= 2:
            return N
        return func1(N - 1) ** 2 + func1(N - 2) ** 2
    res=[]
    for i in range(1,N+1):
        res.append(func1(i))
    return res


print(func(5))
