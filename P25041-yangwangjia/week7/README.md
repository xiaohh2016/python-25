# 本周作业

1. 请将 "1,2,3"，变成 ["1","2","3"]
2. 使用Python copy一个文件，从a目录,copy文件到b目录
3. 以下代码输出什么，请解释原因(写到问题下方):

   li = [ [ ] ] * 5

   li[0].append(10)

   print(li)



​       li[1].append(20)

​       print(li)



​      li.append(30)

​      print(li) 



## 思路

1、使用字符串分割函数split()以 , 分割即可

2、没有学到文件读写操作(￣▽￣)"，学到后再来完成

3、以下代码输出什么，请解释原因(写到问题下方):

li = [ [ ] ] * 5

li[0].append(10)

print(li)

```
输出:[[10], [10], [10], [10], [10]]

原因：第一步创建了一个列表对象，该列表对象*5后其实质是将列表的地址进行了5份拷贝，故修改li[0]，其他的元素也随之产生了变动。
```

li[1].append(20)

print(li)

```
输出：[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
原因：同上。
```

li.append(30)

print(li) 

```
输出：[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
原因：此处的append追加没有涉及到对引用类型数据的修改，故在此处append不会对其列表它元素产生影响，所以这里显示为在列表后面增加了一个元素30。
```


