# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022/4/28 13:36
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022/4/28 14:33


# 第十一条：用 zip 函数同时遍历两个迭代器

"""
    1. 在编写 Python 代码，我们通常需要面对很多列表，而这些列表里的对象，可能也是相互关联的。通过列表推导，很容易就能根据某个表达式从源列表
       推算出一份派生类表。
    2. 对于本例中派生列表和源列表来说，相同索引处的两个元素之间有着关联。如果想要平行地迭代这两份列表，那么可以根据 names 源列表的长度
       来执行循环。
    3. 下面代码的问题在于，整个循环语句看上去很乱。用下标来访问 names 和 letters 会使得代码不易阅读。用循环下标 i 来访问数组的写法一共出现
       两次。该用 enumerate 来做可以稍微缓解这个问题，但仍然不够理想。
    4. 使用 Python 内置的 zip 函数，能够令上述代码变得更加简洁。在 Python 3 中的 zip 函数，可以把两个或两个以上的迭代器封装为生成器，以便
       稍后求值。这种 zip 生成器，会从每个迭代器中获取该迭代器的下一个值，然后这些值汇聚成元组。与通过下标来访问多份列表的写法相比，这种用 zip
       写出来的代码更加清晰。
    5. 内置的 zip 函数有两个问题：
       - 第一个问题是，Python 2 中的 zip 并不是生成器，而是会把开发者所提供的那些迭代器，都平行地遍历一次，在此过程中，它都会把那些迭代器
       所产生的值汇聚成元组，并把那些元组所构成的列表完整地返回给调用者。这可能会占用大量内存并导致程序崩溃。如果要在 Python 2 里用 zip
       来遍历数据量非常大的迭代器，那么应该使用 itertools 内置模块中 izip 函数
       - 第二个问题是，如果输入的迭代器长度不同，那么 zip 会表现出奇怪的行为。例如，我们又给 names 里添加了一个名字，但却忘了把这个名字的
       字母数量更新到 letters 之中。现在，如果用 zip 同时遍历这两份列表，那么就会产生意外的结果。
    7. 新元素 'Rosalind' 并没有出现在遍历结果中。这正是 zip 的运作方式。受封装的那些迭代器中，只要有一个耗尽，zip 就不再产生元组了。
       如果待遍历的迭代器长度都相同，那么这种运作方式不会出问题，由列表推导所推算出的派生列表一般都和源列表等长。如果待遍历的迭代器长度不同，
       那么 zip 会提前终止，这将会导致意外的结果。如不能确定 zip 所封装的列表是否等长，则可考虑改用 itertools 内置模块中 zip_longest
       函数。
    8. 总结：
       - 内置的 zip 函数可以平行地遍历多个迭代器。
       - Python 3 中的 zip 相当于生成器，会在遍历过程中逐次产生元组，而且 Python 2 中的 zip 则是直接把这些元组完全生成好，并一次性地返回
         整份列表。
       - 如果提供的迭代器长度不等，那么 zip 就会自动提前终止。
       - itertools 内置模块中的 zip_longest 函数可以平行地遍历多个迭代器，而不用在乎它们的长度是否相等。
"""

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

# 常规写法
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)
print('--------------------------------------')

# 利用 enumerate 改进
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)
print('--------------------------------------')

# 利用 zip 改进
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

# names 多了一个元素
names.append("Rosalind")
for name, count in zip(names, letters):
    print(name)
print('--------------------------------------')