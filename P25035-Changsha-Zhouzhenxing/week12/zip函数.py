# zip函数
def myzip(*iterables):
    iterator = [iter(it) for it in iterables]

    sentinel = None

    while True:
        lst = []

        for it in iterator:
            elem = next(it, sentinel)

            if elem is sentinel:
                return
            lst.append(elem)

        yield tuple(lst)
		
		
		

# 调用示例
n = myzip('123', 'ABCDE')

print(list(n))

# 这里完成的非常不错。
