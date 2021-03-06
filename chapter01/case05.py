# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022-04-08 14:31:40
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022-04-08 14:31:40


# 第五条：了解切割序列的办法

"""
    1. Python 提供了一种把序列切成小块的写法。
    2. 这种切片操作，使得开发者能够轻易地访问由序列中的某些元素所构成的子集。
    3. 最简单的用法，就是对内置的 list、str、和 bytes 进行切割。
    4. 切割操作还可以延伸到实现了 __getitem__ 和 __setitem__ 这两个特殊方法的 Python 类上。
    5. 切割操作的基本写法是 somelist[start:end]，其中 start(起始索引) 所指的元素涵盖在切割后的范围内，而 end(结束索引) 所指的元素则不包
       括在切割结果之中。
    6. 如果从列表开头获取切片，那就不要在 start 那里写上 0，而是应该把它留空，这样代码看起来会清爽一些。 # assert a[:5] == a[0:5]
    7. 如果切片一直要取到列表末尾，那么应该把 end 留空，因为即便写了，也是多余。 # assert a[5:] == a[5:len(a)]
    8. 切割列表时，即便 start 或 end 索引越界也不会出问题。利用这一特性，我们可以限定输入序列的最大长度。
    9. 反之，访问列表中的单个元素时，下标不能越界，否则会导致异常。
    10. 对原列表进行切割之后，会产生另外一份全新的列表。系统依然维护着指向原列表中各个对象的引用。
    11. 在切割后得到新列表上进行修改，不会影响原列表。
    12. 在赋值时对左侧列表使用切割操作，会把该列表中处于指定范围内的对象替换为新值。
    13. 与元组 (tuple) 的赋值 (a, b = c[:2]) 不同，此切片的长度无需新值的个数相等。位于切片范围之前及之后的那些值都保留不变。列表会根据新
        值的个数相应地扩张或收缩。
    14. 如果对赋值操作右侧列表使用切片，而把切片的起止索引都留空，那么就会产生一份原列表的拷贝。
    15. 如果对赋值操作左侧的列表使用切片，而又没有指定起始索引，那么系统会把右侧的新值复制一份，并用这份拷贝来替换左侧列表的全部内容，而不会重
        新分配新的列表。
    16. 总结：
        - 不要写多余的代码：当 start 索引为 0，或 end 索引为序列长度时，应该将其省略。
        - 切片操作不会计较 start 与 end 索引是否越界，这使得我们很容易就能从序列的前端或后端开始，对其进行范围固定的切片操作。
        - 对 list 赋值的时候，如果使用切片操作，就会把原列表中处在相关范围内的值替换成新值，即便它们的长度不同也依然可以替换。
"""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print('First four:', a[:4])
print('Last four:', a[-4:])
print('Middle two:', a[3:-3])
print("-------------------------")

assert a[:5] == a[0:5]
first_twenty_items = a[:20]
last_twenty_items = a[-20:]
print(first_twenty_items)
print(last_twenty_items)
print("-------------------------")

b = a[4:]
print('Before: ', b)
b[1] = 99
print('After: ', b)
print('No change: ', a)
print("-------------------------")

print('Before ', a)
a[2:7] = [99, 22, 14]
print('After ', a)

b = a[:]
assert b == a and b is not a
print("-------------------------")

b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b
print('After: ', a)
