# map函数
def mymap(func, iter):

 for val in iter:
  ret = func(val)
  yield ret
  
  

# 调用
g = (mymap(str, [1, 2]))
print(next(g))
print(next(g))


# 这里只实现了map对单个可迭代元素的处理，如果是多个可迭代元素呢？尝试写一下。
