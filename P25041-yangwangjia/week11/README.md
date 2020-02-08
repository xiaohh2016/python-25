## 题目

自己实现python自带的map、zip和filter函数



## 思路

1. `map`函数：遍历iterable将每次遍历的值转换成传入类型的值，返回生成器表达式。或抛出异常。
2. `zip`函数：遍历传入的iterable的长度，取出最短的然后依次获取内容封装到元组中返回迭代器
3. `filter`函数：传递函数，对iterable的值进行处理，为真保留否则过滤掉。