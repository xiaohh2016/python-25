# 本周作业，希望大家认真完成哦（11.4-11.10）
# 1、请将 "1,2,3"，变成 ["1","2","3"]
# 2、使用Python copy一个文件，从a目录,copy文件到b目录
# 3、以下代码输出什么，请解释原因(写到问题下方):
# li = [ [ ] ] * 5
# li[0].append(10)
# print(li)
# li[1].append(20)
# print(li)
# li.append(30)
# print(li)
#1
nums = "1,2,3"
num_list = nums.split(",")
print(num_list)


#2
import os
print(os.system('cp a/xxx.py b/xxx.py'))
#3
li = [[[]]] * 5
print(li)
li[1][0].append(10)
print(li)
print(id(li))
print(id(li[0]))
print(id(li[1]))
print(id(li[2]))
print(id(li[0][0]))
print(id(li[1][0]))
print(id(li[2][0]))

#li 是 list， 其中包含5个list指向同一内存地址
#li[0] 的值等价于 li[1] li[2] li[3] li[4]，指向同一内存地址
#[[10], [10], [10], [10], [10]]
li[2][0].append(20)
print(li)
#[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
li.append(30)
print(li)
#[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]

"""
第一题中，如果不允许使用split()函数，该怎么实现，可以尝试一下。
nums = "1,2,3"
def str_to_list(string):
    number_list = []
    num = ""
    read_len = 0
    num_len = len(nums)
    for x in nums:
        if x!=",":
            num = num + x
        elif x=="," or read_len == num_len-1:
            number_list.append(num)
            num = ""
        read_len += 1
    return num_list
print(str_to_list(nums))
第二题里，直接使用cp是linux系统里的命令，如果是windows系统，是否同样适用？
windows应该用copy吧
第三题内，基本概念了解清楚了，可以尝试一下，如果是三层数据结构，会出现什么样的情况。


"""

# 很不错,老师提到的内容都自己尝试了,习题也都做对了,很棒.后面的内容学习了,也别忘了提交作业,阿飞老师都会批改的.
