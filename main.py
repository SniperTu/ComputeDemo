"""
# def get_lines():
#     with open('file.txt', 'rb') as f:
#         return f.readlines()
#
#
# if __name__ == '__main__':
#     if e in get_lines():
#         process(e)  # 处理每一行数据
# 要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines函数而其他代码保持不变的情况下，如何实现？
# 方法一：
def get_lines():
    with open('file.txt', 'rb') as f:
        for i in f:
            yield i


# 但该方法读取次数太多以下方法增加设置行数


def get_lines():
    line = []
    with open('file.txt', 'rb') as f:
        data = f.readlines(60000)
    line.append(data)
    yield line


# 方法二：


from mmap import mmap


def get_lines(fp):
    with open(fp, 'r+') as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b"\n":
                yield m[tmp: i + 1].decode()
                tmp = i + 1


if __name__ == '__main__':
    for i in get_lines("fp_some_huge_file"):
        print(i)

# 这个函数接收文件夹的名称作为输入参数
# 返回该文件夹中文件的路径
# 以及其包含文件夹中文件的路径

import os


def print_dictionary_contents(s_path):
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_dictionary_contents(s_child_path)
        else:
            print(s_child_path)


# 输入日期，判断这一天是这一年的第几天


import datetime


def which_day():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1


print(which_day())

# 打乱一个排好序的list对象alist

import random

alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)

# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序
d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
print(sorted(d.items(), key=lambda x: x[1]))
# x[0]代表用key进行排序， x[1]代表用value进行排序

# 字典推导式
# d = {key: value for (key, value) in iterable}

# 反转字符串
print("aStr"[::-1])

# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}

str1 = "k:1 |k1:2|k2:3|k3:4"


def change_to_dict(str1):
    dict1 = {}
    for item in str1.split('|'):
        key, value = item.split(':')
        dict1[key] = value
    return dict1


# 字典推导式
d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"),)}

# 请按alist中元素的age由大到小排序
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 19}, {'name': 'c', 'age': 22}, {'name': 'd', 'age': 29}]


def sort_by_age(list1):
    return sorted(alist, key=lambda x: x['age'], reverse=True)


# 写一个列表生成式，产生一个公差为11的等差数列
print([x * 11 for x in range(10)])

# 给定两个列表，怎么找出他们相同的元素和不同的元素
list1 = [1, 2, 3]
list2 = [3, 5, 2]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)


# 请写出一段python代码实现删除list里面的重复元素
# 方法一：
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = list(set(l1))
print(l2)

# 用list类的sort方法：
# 方法二：
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
list.sort(l1)

# 方法三：
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = sorted(set(l1), key=l1.index)
print(l2)

# 方法四（遍历）：
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)



# python 实现单例模式的两种方法：
# 方法一：使用装饰器


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Foo(object):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


# True

# 方法二：使用基类（重写基类的new方法）
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)



# 方法三：使用元类（在调用call时保证始终只创建一个实例）

class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


# 反转一个整数，例如-123——>-321
class Solution(object):
    def reverse_str(self, x):
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != '-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x


if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse_str(-120)
    print(reverse_int)

# 设计实现遍历目录与子目录，抓取.pyc文件
# 第一种方法
import os


def get_files(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    print(res)


get_files("./", '.pyc')

# 第二种方法
import os


def pick(obj):
    if obj.endswitch(".pyc"):
        print(obj)


def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)


if __name__ == '__main__':
    path = input('输入目录')
    scan_path(path)

# 第三种方法
from glob import iglob


def func(fp, postfix):
    for i in iglob(f"{fp}/**/*{postfix}", recursive=True):
        print(i)


if __name__ == '__main__':
    postfix = ".pyc"
    func("D:\python_basic_practice", postfix)

# 实现1-100之和
count = sum(range(1, 101))
print(count)

# Python 遍历列表时删除元素的正确做法
# 遍历在新列表操作，删除在原来的列表操作

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(id(a))
print(id(a[:]))
for i in a[:]:
    if i > 5:
        pass
    else:
        a.remove(i)
    print(a)
print("------------")
print(id(a))
print(a)
print(a[:])

# filter方法
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = filter(lambda x: x > 5, a)
print(list(b))

# 列表遍历
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i for i in a if i > 5]
print(b)

# 倒序删除
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(id(a))
for i in range(len(a) - 1, -1, -1):
    if a[i] > 5:
        pass
    else:
        a.remove(a[i])
print(id(a))
print(a)


# 2255879083200
# 2255879083200

# 字符串操作
def get_missing_letter(a):
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    s2 = set(a.lower())
    ret = "".join(sorted(s1 - s2))
    return ret


print(get_missing_letter("python"))

# 转换大小写
# 方法一：
import string

letters = string.ascii_lowercase
# 方法二:
letters = "".join(map(chr, range(ord('a'), ord('z') + 1)))
"""
# 可变类型和不可变类型：
# 可变类型：list, dict;不可变类型：String, number, tuple
# 进行修改操作时，可变类型传递的是内存中的地址，即直接修改内存中的值，没有开辟新的内存
# 不可变类型改变时，不改变原内存地址中的值， 而是开辟一块新的内存，将源地址中的值复制过去。


# is和==的区别：
# is：是比较两个对象的id是否相等，即比较俩对象是否为同一个实例对象，是否指向同一个内存地址
# ==：比较两对象的内容/值是否相等，默认会调用对象的eq()方法


# 求出列表所有奇数并构造新列表
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i % 2 == 1]
print(res)

# 用一行代码写出1+2+3+10248
from functools import reduce

# 1.使用内置sum求和函数
num = sum([1, 2, 3, 10248])
print(num)
# 2.reduce函数
num1 = reduce(lambda x, y: x + y, [1, 2, 3, 10248])
print(num1)

# 变量作用域：LEGB
# L:local函数内部作用域
# E:enclosing函数内部与内嵌函数之间
# G:global全局作用域
# B:build_in内置作用

#
