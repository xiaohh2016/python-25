#实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间
from functools import wraps
import datetime

def timeit(fn):
    @wraps(fn) #使用内建wraps函数保证使用装饰器后函数属性不改变
    def inner(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        travel = (datetime.datetime.now()-start).total_seconds()
        msg = 'fn:{},take time:{} seconds'.format(fn.__name__,travel)
        print(msg)
        return ret
    return inner

@timeit   #等价式 testfunc = timeit(testfunc) =wrap(testfunc) = fn
def testfunc(times=1000000):
    #测试函数
    count = 0
    for i in range(times):
        count += 1
    return count

print(testfunc(100000000))

#写的很好，说明装饰器这节课的内容认真听完吸收了。这一个作业的内容和老师讲的一样，希望同学能够好好吸收这部分的内容，装饰器
# 在后面的实际开发工作中应用的还是比较广泛的。
