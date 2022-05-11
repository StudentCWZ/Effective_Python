# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-11 08:41:49
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-11 10:56:34


# 第十七条：在参数上面迭代时，要多加小心


"""
    1. 如果函数接受的参数是一个对象列表，那么很有可能要在这个列表上面多次迭代。
    2. 例如，要分析去美国 Texas 旅游的人数。假设数据集是由每个城市的游客数量构成的，现在要统计来
       每个城市旅游的人数(单位是每年百万人)，占总游客数的百分比。
    3. 为此，需要编写标准化函数。它会把所有的输入值加总，以求出每年的游客总数。然后，用每个城市的
       游客数除以总数，以求出该城市所占的比例。
    4. 为了扩大函数的应用范围，现在把 Texas 每个城市的游客数放在一份文件里面，然后从该文件中读取
       数据。由于这套流程还能够分析全世界的游客数量，所以定义了生成器函数来实现此功能，以便稍后把
       该函数用到更庞大的数据集上面。
    5. 奇怪的是，以生成器所返回的那个迭代器为参数，来调用 normalize_two ，却没有产生任何结果。出
       现这种情况的原因在于，迭代器只能产生一轮结果。在抛出过 StopIteration 异常的迭代器或生成器
       上面继续迭代第二轮，是不会有结果的。
    6. for 循环、list 构造器以及 Python 标准库里的其他许多函数，都认为在正常的操作过程中完全有可
       能出现 StopIteration 异常，这些函数没办法区分这个迭代器是本来就没有输出值，还是本来有输出
       值，但现在已经用完了。
    7. 为了解决此问题，我们可以明确地使用该迭代器制作一份列表，将它的全部内容都遍历一次，并复制到这
       份列表里，然后，就可以在复制出来的数据列表上面多次迭代了。
    8. normalize_three 的写法问题在于，待复制的那个迭代器，可能含有大量输入数据，从而导致程序在复
       制迭代器的时候耗尽内存并崩溃。
    9. 一种解决方法是通过参数来接受另一个函数，那个函数每次调用后，都能返回新的迭代器。
    10. 使用 normalize_four 函数的时候，传入 lambda 表达式，该表达式会调用生成器，以便每次都能产
        生新的迭代器。
    11. 还有一个更好的方法，也能达到同样的效果，那就是新编一种实现迭代器协议的容器类。
    12. Python 在 for 循环及相关表达式中遍历某种容器的内容时，就要依靠这个迭代器协议。在执行类似于
        for x in foo 这样的语句时，Python 实际会调用 iter(foo)。内置 iter 会调用 foo.__iter__
        这个特殊方法。该方法必须返回迭代对象，而那个迭代器本身，则实现了名为 __next__ 的方法。
    13. 此后，for 循环会在迭代对象上面反复调用内置 next 函数，直至耗尽并产生 StopIteration 异常。
    14. 这听起来比较复杂，但实际上，只需要另自己的类把 __iter__ 方法实现为生成器，就能满足要求。
    15. normalize 函数中的 sum 方法会调用 ReadVisits.__iter__，从而得到新的迭代器对象，而调整数值
        所用的那个 for 循环，也会调用 __iter__，从而得到另外一个新的迭代器器对象，由于这两个迭代器会
        各自前进并走完一整轮，所以它们都可以看到全部的输入数据。这种方式唯一的缺点在于，需要多次读取数
        据。
    16. 迭代器协议有这样的约定：如果把迭代器对象传给内置的 iter 函数，那么此函数会把该迭代器返回，反之，
        如果传给 iter 函数的是个容器类型对象，那么 iter 函数则每次都会返回新的迭代器对象。于是，我们
        可以根据 iter 函数的这种行为来判断输入值是不是迭代器对象本身，如果是，就抛出 TypeError 错误。
    17. normalize_five 函数能够处理 list 和 ReadVisits 这样的输入参数，因为它们都是容器。凡遵从迭代
        器协议的容器类型，都与这个函数相兼容。
    18. 总结：
        - 函数在输入的参数上面多次迭代时要当心：如果参数时迭代器，那么可能会导致奇怪的行为并错失某些值。
        - Python 的迭代器协议，描述了容器和迭代器应该如何与 iter 和 next 内置函数、 for 循环以及相关表达式相互配合。
        - 把 __iter__ 方法实现为生成器，即可定义自己的容器类型。
        - 想判断某个值是迭代器还是容器，可以拿该值为参数，两次调用 iter 函数。若结果相同，则是迭代器，调用内置的 next 函数，即可令该迭代器前进一步。
"""


# Example One
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
print("-" * 60)


# Example Two
# 错误案例
def normalize_two(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits("my_numbers.txt")
percentages = normalize_two(it)
print(percentages)
print("-" * 60)


# Example Three
def normalize_three(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits("my_numbers.txt")
percentages = normalize_three(it)
print(percentages)
print("-" * 60)


# Example Four
def normalize_four(get_iter):
    total = sum(get_iter()) # New iterator
    result = []
    for value in get_iter(): # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


percentages = normalize_four(lambda: read_visits('my_numbers.txt'))
print(percentages)
print("-" * 60)


# Example Five
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = ReadVisits("my_numbers.txt")
percentages = normalize(visits)
print(percentages)
print("-" * 60)


# Example Six
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_five(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize_five(visits)
print(percentages)
visits = ReadVisits("my_numbers.txt")
percentages = normalize_five(visits)
print(percentages)
print("-" * 60)


# Example Seven
from itertools import islice
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_six(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError("Must supply a container")
    total = sum(numbers)
    for value in numbers:
        percent = 100 * value / total
        yield percent


visits = ReadVisits("my_numbers.txt")
percentages = normalize_six(visits)
results = islice(percentages, 0, 3)
print(list(results))
print("-" * 60)



