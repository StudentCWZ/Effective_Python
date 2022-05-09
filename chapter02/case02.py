# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022/5/9 08:55
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022/5/9 08:55


# 第十五条：了解如何在闭包里使用外围作用域中的变量

"""
    1. 假如有一份列表，其中的元素都是数字，现在要对其排序，但排序时要把出现在某个群组内的数字，放在群组外的那些数字之前。这种用法在绘制用户界面
       时候可能会遇到，我们可以用这个办法把重要的消息或意外的事件优先显示在其他内容前面。
    2. 实现该功能的一种常见做法，是在调用列表的 sort 方法时，把辅助函数传给 key 参数。这个辅助函数的返回值，将会用来确定列表中各元素的顺序。
       辅助函数可以判断受测元素是否处在重要群组中，并据此返回相应的排序关键字。
    3. Python 支持闭包：闭包是一种定义在某个作用域的函数，这种函数引用了那个作用域里面的变量。helper 函数之所以能够访问 sort_priority 的
       group 参数，原因就在于它是闭包。
    4. Python 的函数是一级对象，也就是说，我们可以直接引用函数、把函数赋给变量、把函数当成参数传给其他函数，并通过表达式及 if 语句对其进行比
       较和判断，等等。于是，我们可以把 helper 这个闭包函数，传给 sort 方法的 key 参数。
    5. Python 使用特殊的规则来比较两个元组。它首先比较各元组中下标为 0 的对应元素，如果相等，再比较下标为 1 的对应元素，如果还是相等，那就继
       续比较下标为 2 的对应元素，依次类推。
    6. 在表达式中引用变量时，Python 解释器将按如下顺序遍历作用域，以解析该引用：
       - 当前函数的作用域
       - 任何外围作用域(例如，包含当前函数的其他函数)
       - 包含当前代码的那个模块的作用域(也叫全局作用域)
       - 内置作用域(也就是包含 len 及 str 等函数的那个作用域)
    7. Python 3 中有一种特殊写法，能够获取闭包内的数据。我们可以用 nonlocal 语句来表明这样的意图，也就是：给相关变量赋值的时候，应该在上层
       作用域中查找该变量。nonlocal 唯一限制在于，它不能延伸到模块级别，这是为了防止它污染全局作用域。
    8. nonlocal 语句清楚表明：如果在闭包内给该变量赋值，那么修改的其实是闭包外那个作用域中的变量。这与 global 语句互为补充，global 用来表
       示对该变量的赋值操作，将会直接修改模块作用域里的那个变量。
    9. 然而，nonlocal 也会像全局变量那样，遭到滥用，所以，建议大家只在极其简单的函数里使用这种机制。nonlocal 的副作用很难追踪，尤其在比较长
       的函数中，修饰某变量的 nonlocal 语句可能和修改该变量的赋值操作离得比较远，从而导致代码更加难以理解。
    10. 如果使用 nonlocal 的那些代码，已经写得越来越复杂，那就应该将相关的状态封装成辅助类。
    11. 不幸的是， Python 2 不支持 nonlocal 关键字。为了实现类似的功能，我们需要利用 Python 的作用域规则来解决。这种做法虽然不优雅，但已
        经成了一种 Python 编程习惯。
    12. 总结：
        - 对于定义在某作用域内的闭包来说，它可以引用这些作用域中的变量。
        - 使用默认方式对闭包内的变量赋值，不会影响外围作用域中的同名变量。
        - 在 Python 3 中，程序可以在闭包内用 nonlocal 语句来修饰某个名称，使该闭包能够修改外围作用域中的同名变量。
        - 在 Python 2 中，程序可以使用可变值(例如，包含单个元素的列表) 来实现与 nonlocal 语句相仿的机制。
        - 除了那种比较简单的函数，尽量不要用 nonlocal 语句。
"""


# Example One
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
groups = {2, 3, 5, 7}
sort_priority(numbers, groups)
print(numbers)
print('----------------------------')


# Example Two
def sort_priority_two(values, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
groups = {2, 3, 5, 7}
loop = sort_priority_two(numbers, groups)
print('found:', loop)
print(numbers)
print('----------------------------')


# Example Three
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
groups = {2, 3, 5, 7}
sorter = Sorter(groups)
numbers.sort(key=sorter)
print('found:', sorter.found)
print(numbers)
assert sorter.found is True
print('----------------------------')


# Example Four
# Python 2 函数写法
def sort_priority_three(values, group):
    found = [False]

    def helper(x):
        if x in group:
            found[0] = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found[0]
