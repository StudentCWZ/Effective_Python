# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-13 08:57:24
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-13 09:52:43


# 第十九条：用关键字参数来表达可选的行为


"""
    1. 与其他编程语言一样，调用 Python 函数时，可以按位置传递参数。
    2. Python 函数中的所有参数，都可以按关键字传递。采用关键字形式来指定参数数值是，我们会在表示函数调用操作的那一对圆括号内，以赋值的格式，把参数名称
       和参数值分别放在等号左右两侧。
    3. 关键字参数的顺序不限，只要把函数所要求的全部位置参数都指定好即可。
    4. 还可以混合使用关键字和位置参数来调用函数。但位置参数必须出现在关键字参数之前。
    5. 每个参数只能指定一次。
    6. 灵活使用关键字参数，能带来三个重要好处：
       - 首先，以关键字参数来调用函数，能使读到这行代码的人更容易理解其含义。
       - 关键字参数的第二个好处是，它可以在函数定义中提供默认值。在大部分情况下，函数调用者只需使用这些默认值就够了，若要开启某些附加功能，则可以指定相应
         的关键字参数。这样做可以消除重复代码，并使代码变得更加整洁。
       - 使用关键字第三个好处，是可以提供一种扩充函数参数的有效方式，使得扩展之后的函数依然能与原有的那些调用代码相兼容。我们不需要迁移大量代码，即可给函数添加
         新的功能，这减少了引入 bug 概率。
    7. 例如，要扩充 flow_rate_three 函数，使它能够根据千克之外的其他重量单位来计算流率。为此，我们添加一个可选的参数，用以表示千克与那种重量单位之间的换算关系。
    8. 这种写法只有一个缺陷，那就是像 period 和 units_per_kg 这种可选的关键字参数，仍然可以通过位置参数的形式来指定。
    9. 最好的办法，是一直以关键字的形式来指定这参数，而决不采用位置参数来指定它们。
    10. 总结：
        - 函数参数可以按位置或关键字来指定
        - 只使用位置参数来调用函数，可能会导致这些参数值的含义不够明确，而关键字参数则能够阐明每个参数的意图。
        - 给函数添加新的行为时，可以使用带默认值的关键字参数，以便与原有的函数调用代码保持兼容。
        - 可选的关键字参数，总是应该以关键字形式来指定，而不应该以位置参数的形式来指定。
"""


# Example One
def remainer(number, divisor):
    return number % divisor


assert remainer(20, 7) == 6
print(remainer(20, 7))
print(remainer(20, divisor=7))
print(remainer(number=20, divisor=7))
print(remainer(divisor=7, number=20))
# print(remainer(number=20, 7)) # 报错
# print(remainer(20, number=7)) # 报错
print("-" * 20)


# Example Two
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print("%.3f kg per second" % flow)
print("-" * 20)


# Example Three
def flow_rate_two(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


weight_diff = 0.5
time_diff = 3
flow_per_second = flow_rate_two(weight_diff, time_diff, 1)  # 缺点：每次调用函数时，都要指定 period 参数，即便我们想计算最常见的每秒流率，也依然要把 1 传给 period 参数
print("%.3f kg per second" % flow_per_second)
print("-" * 20)


# Example Four
def flow_rate_three(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


weight_diff = 0.5
time_diff = 3
flow_per_second = flow_rate_three(weight_diff, time_diff)
flow_per_hour = flow_rate_three(weight_diff, time_diff, period=3600)
print("%.3f kg per second" % flow_per_second)
print("%.3f kg per hour" % flow_per_hour)
print("-" * 20)


# Example Five
def flow_rate_Four(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period


pounds_per_hour = flow_rate_Four(weight_diff, time_diff, period=3600, units_per_kg=2.2)
print("%.3f kg per hour" % pounds_per_hour)
print("-" * 20)





