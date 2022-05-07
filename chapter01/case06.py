# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022-04-10 16:31:25
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022-04-10 16:31:25


# 第六条：在单次切片操作内，不要同时指定 start、end 和 stride


"""
    1. 除了基本的切片操作之外，Python 还提供了 somelist[start:end:stride] 形式的写法，以实现步进式切割，也就是从每 n 个元素里面取 1 个
       出来。
    2. 例如，可以指定步进值，把列表中的位于偶数索引处和奇数索引处的元素分成两组。
    3. Python 中有一种常见的技巧，能够把以字节形式存储的字符串反转过来，这个技巧就是采用 -1 做步进值。这种技巧对字节串和 ASCII 字符有用，
       但是对已经编码成 UTF-8 字节串的 Unicode 字符来说，则无法奏效。
    4. 在切割列表时，如果指定了 stride ，那么代码可能会变得相当费解。在一对中括号里写上 3 个数字显得太过拥挤，从而导致代码难以阅读。这种写法
       是的 start 和 end 索引的含义变得模糊，当 stride 为负值尤其如此。
    5. 如果非要用 stride ，那么就尽量采用正值，同时省略 start 和 end 索引。 如果一定要配合 start 或 end 索引来使用 stride ，那么请考虑
       先做步进式切片，把切割结果赋给某个变量，然后在那个变量上面做第二次切割。
    6. 如果你所开发的程序对执行时间或内存用量的要求非常严格，那么就不能采用两阶段切割法，请考虑 Python 内置的 itertools 模块。该模块中有个
       islide 方法，这个方法不允许为 start、end 或 stride 指定负值。
    7. 总结：
       - 既有 start 和 end，又有 stride 的切割操作，可能会让人费解。
       - 尽量使用 stride 为正数，且不带 start 或 end 索引的切割操作。尽量避免用负数做 stride。
       - 在同一个切片操作内，不要同时使用 start、end 和 stride。如果确实需要执行这种操作，那就考虑将其拆解为两条赋值语句，其中一条做范围切
         割，另一条做步进切割，或考虑使用内置 itertools 模块中的 islice。
"""

# Example One
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)
print('---------------------------------------')

# Example Two
x = b'mongoose'
y = x[::-1]
print(y)
print('---------------------------------------')

# Example Three
b = a[::2]
c = b[1:-1]
print('---------------------------------------')
