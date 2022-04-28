# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022/4/28 13:36
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022/4/28 13:36


import random

# 第十条：尽量用 enumerate 取代 range


"""
    1. 在一系列整数上面迭代时，内置的 range 函数很有用。
    2. 对于字符串列表这样的序列式数据结构，可以直接在上面迭代。
    3. 当迭代列表的时候，通常还想知道当前元素在列表中的索引。例如，要按照喜好程度打印出自己爱吃的冰淇淋口味。一种是用 range 来做。
    4. 与单纯迭代 flavor_list 或是单纯使用 range 代码相比，下面相关这段代码有点生硬。我们必须获取列表长度，并且通过下标来访问数组。这种代码不便于理解。
    5. Python 提供了内置的 enumerate 函数，以解决此问题。 enumerate 可以把各种迭代器包装为生成器，以便稍后产生输出值。生成器每次产生一堆输出值，其中，
       前者表示循环下标，后者表示从迭代器中获取到的下一个序列元素，这样写出来的代码会非常简洁。
    6. 还可以直接指定 enumerate 函数开始计数时所用的值(从 1 开始记数)，这样能把代码写得更短。
    7. 总结：
       - enumerate 函数提供了一种精简的写法，可以在遍历迭代器时获知每个元素的索引。
       - 尽量用 enumerate 来改写那种将 range 与下标访问相结合的序列遍历代码。
       - 可以给 enumerate 提供第二个参数，以指定开始计数时所用的值(默认为 0)。
"""

# range 函数 迭代
random_bits = 0
for i in range(64):
    if random.randint(0, 1):
        random_bits |= 1 << i
print(random_bits)
print('--------------------------------------')

# 字符串列表
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s in delicious' % flavor)
print('--------------------------------------')

# 字符串列表的 range 操作
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))
print('--------------------------------------')

# 字符串列表的 enumerate 操作
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))
print('--------------------------------------')

# 字符串列表的 enumerate 操作，且添加第二参数
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
print('--------------------------------------')
