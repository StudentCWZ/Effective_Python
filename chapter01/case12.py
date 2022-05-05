# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022/4/28 13:36
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022/5/05 14:53


# 第十二条：不要在 for 和 while 循环后面写 else 块

"""
    1. Python 提供了一种很多编程语言都不支持的功能，那就是可以在循环内部的语句块后面直接写 else 块。
    2. 奇怪的是，这种 else 块语句会在整个循环执行完之后立刻运行。
    3. 在 if/else 语句中，else 的意思是：如果不执行前面那个 if 块，那就执行 else 块。在 try/except 语句中，except 的定义也类似：如果
       前面的 try 块没有失败，那就执行 except 块。
    4. 实际上 for 循环后面接的 else 块跟 if/else 语句中 else 块意思相反，在循环里用 break 语句提前跳出，会导致程序不执行 else 块。
    5. 还有一个奇怪的地方：如果 for 循环要遍历的序列是空的，那么就会立刻执行 else 块。
    6. 初始循环条件为 false 的 while 循环，如果后面跟着 else 块，那它也会立刻执行。
    7. 知道了循环后面的 else 块所表现出来的行为之后，我们会发现，在搜索某个事务的时候，这种写法是有意义的。例如，要判断两个数是否互质(也就是
       判断两者除了 1 之外，是否没有其他的公约数)，可以把有可能成为公约数的每个值都遍历一轮，逐个判断两数是否能以该值为公约数。尝试完每一种可
       能的值之后，循环就结束了。如果两个数确实互质，那么在执行循环的过程中，程序就不会因为 break 语句而跳出，于是，执行完循环后，程序会紧接
       着执行 else 块。
    8. 实际上，我们并不会这样写代码，而是会使用辅助函数来完成计算。这样的辅助函数，有两种常见的写法。
    9. 第一种写法是，只要发现受测参数符合自己想要搜寻的条件，就尽早返回。如果整个循环都完整地执行了一遍，那就说明受测参数不符合条件，于是返回
       默认值。
    10. 第二种写法是，用变量来记录受测参数是否符合自己想要搜寻的条件。一旦符合，就用 break 跳出循环。
    11. 总结：
        - Python 有种特殊语法，可在 for 及 while 循环的内部语句块之后紧跟一个 else 块。
        - 只有当整个循环主题都没遇到 break 语句时，循环后面的 else 才会执行。
        - 不要在循环后面使用 else 块，因为这种写法既不直观，又容易引人误解。
"""
# Example One
for i in range(3):
    print('Loop %d' % i)
else:
    print('Else block!')
print('--------------------------')

# Example Two
for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print('Else block!')
print('--------------------------')

# Example Three
for x in []:
    print('Never runs')
else:
    print('For else block!')
print('--------------------------')

# Example Four
while False:
    print('Never runs')
else:
    print('For else block!')
print('--------------------------')

# Example Five
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')
print('--------------------------')


# Example Six
def coprime(y, z):
    for w in range(2, min(y, z) + 1):
        if y % w == 0 and z % w == 0:
            return False
    else:
        return True


if coprime(a, b):
    print('Coprime')
else:
    print('Not coprime')
print('--------------------------')


# Example Seven
def coprime_two(y, z):
    is_coprime = True
    for w in range(2, min(y, z) + 1):
        if y % w == 0 and z % w == 0:
            is_coprime = False
            break
    return is_coprime


if coprime_two(a, b):
    print('Coprime')
else:
    print('Not coprime')
print('--------------------------')
