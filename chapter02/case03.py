# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-10 16:37:43
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-10 17:26:40


# 第十六条：考虑用生成器来改写直接返回列表的函数

"""
    1. 如果函数要产生一系列结果，那么最简单的做法就是把这些结果都放在一份列表中，并将其返回给调用者。
    2. 例如，我们要查出字符串中每个词的首字母，在整个字符串里的位置。
    3. 这个 index_words 函数用生成器写出来会更好。生成器是使用 yield 表达式的函数。调用生成器函数时，它并不会真的运行，而是返回迭代器。
       每次在这迭代器上面调用内置的 next 函数时，迭代器会把生成器推进到下一个 yield 表达式那里。生成器传给 yield 的每一个值，都由迭代器返回给调用者。
    4. index_words_two 函数不需要包含与 result 列表相交互的那些代码，因而看起来比刚才那种写法清晰许多。原来那个 result 列表中的元素，现在都分别传给
       yield 表达式了。调用该生成器后所返回的迭代器，可以传给内置的 list 函数，以将其转换成列表。
    5. index_words 函数第二个问题是，它在返回前，要先把所有结果都放在列表里面。如果输出量非常大，那么程序就有可能耗尽内存并崩溃。相反，用生成器改写后的
       版本，则可以应对任意长度的输入数据。
"""

# Example One
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])
print("-" * 20)

# Example Two
def index_words_two(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1

address = 'Four score and seven years ago...'
result = list(index_words_two(address))
print(result[:3])
print("-" * 20)

# Example Three
from itertools import islice
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset

with open("address.txt", 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))
print("-" * 20)

