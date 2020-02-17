# filter函数

def myfilter(func, iterable):
    lst = []

    for c in iterable:
        if func(c):
            yield c



# 调用示例
g = myfilter(lambda x: x > 3, (1, 2, 3, 5, 6))
print(list(g))

# 这里的代码只考虑的正常的情况，如果故意给出一个出错的情形
# 那么代码就无法处理了，可以考虑一下加入一点错误判断的逻辑
