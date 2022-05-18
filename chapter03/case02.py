# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-18 09:03:38
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-18 10:17:42


# 第二十三条：简单的接口应该接受函数，而不是类的实例

"""
    1. Python 有许多内置的 API，都允许调用者传入函数，以定制其行为。API 在执行的时候，会通过这些挂钩函数，回调函数内的代码。
    2. 例如，list 类型的 sort 方法接受可选的 key 参数，用以指定每个索引位置上的值之间应该如何排序。所以可以用 lambda 表达
       式充当 key 挂钩，以便根据每个名字的长度来排序。
    3. 其他编程语言可能会用抽象类来定义挂钩。然而在 Python 中，很多挂钩只是无状态的函数，这些函数有明确的参数及返回值。用函数
       做挂钩是比较合适的，因为它们很容易描述出这个挂钩的功能，而且比定义一个类要简单。
    4. Python 中的函数之所以能充当挂钩，原因在于，它是一级对象，也就是说，函数与方法可以像语言中的其他值那样传递和引用。
    5. 例如，要定制 defaultdict 类的行为。这种数据结构允许使用者提供一个函数，以后在查询字典时，如果里面没有待查的键，那就用
       这个函数为该键创建新值。当字典中没有待查询的键时，此函数必须返回那个键所应具备的默认值。
    6. log_missing 这个挂钩函数会在字典找不到待查询的键时打印一条信息，并返回 0 ，以作为该键所对应的值。
    7. 例如，现在要给 defaultdict 传入一个产生默认值的挂钩，并令其统计出该字典一共遇到了多少个缺失的键。一种实现方式是使用带状
       态的闭包。
    8. 把带状态的闭包函数用作挂钩有一个缺点，就是读起来要比无状态的函数难懂一些。还有个办法也能实现上述功能，那就是定义有个小型类，
       把需要追踪的状态封装起来。
    9. 总结：
       - 对于连接各种 Python 组件的简单接口来说，通常应该给其直接传入函数，而不是先定义某个类，然后再传入该类的实例。
       - Python 中的函数和方法都可以像一级类那样引用，因此，它们与其他类型的对象一样，也能够放在表达式里面。
       - 通过名为 __call__ 的特殊方法，可以使类的实例能够像普通的 Python 函数那样得到调用。
       - 如果要用函数来保存，那就应该定义新的类，并令其实现 __call__ 方法，而不要定义带状态的闭包。
"""


# Example One
names = ["Socrates", "Archimeds", "Plato", "Aristotle"]
names.sort(key=lambda x: len(x))
print(names)
print("-" * 60)


# Example Two
from collections import defaultdict

def log_missing():
    print("Key added")
    return 0


current = {"green": 12, "blue": 3}
increments = {
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
}
result = defaultdict(log_missing, current)
print("Before:", dict(result))
for key, amount in increments:
    result[key] += amount
print("After:", dict(result))
print("-" * 60)


# Example Three
from collections import defaultdict

def increment_with_report(current, increments):
    added_count = 0


    def missing():
        nonlocal added_count
        added_count += 1
        return 0


    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


current = {"green": 12, "blue": 3}
increments = {
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
}
result, count = increment_with_report(current, increments)
assert count == 2
print(dict(result))
print("-" * 60)


# Example Four
from collections import defaultdict

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


current = {"green": 12, "blue": 3}
increments = {
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
}
counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(dict(result))
print("-" * 60)


# Example Five
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


current = {"green": 12, "blue": 3}
increments = {
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
}
counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(dict(result))
print("-" * 60)










