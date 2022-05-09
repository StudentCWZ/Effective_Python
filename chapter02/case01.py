# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022/5/6 14:36
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022/5/6 14:59


# 第十四条: 尽量用异常来表示特殊情况，而不要返回 None

"""
    1. Python 程序员首先接触的代码组织工具，就是函数(function)。
    2. 与其他编程语言类似，Python 的函数也可以把一大段程序分成几个小部分，使每个部分都简单一些。这样做可以令代码更加易懂，也更便于使用。
    3. 函数还为复用和重构提供了契机。
    4. 编写工具函数时，Python 程序员喜欢给 None 这个返回值赋予特殊意义，这么做有时是合理的。例如，要编写辅助函数，计算两数相除的商。在除数
       为 0 的情况下，计算结果是没有明确含义的，所以似乎应该返回 None。
    5. 分子若是 0, 会怎么样呢，在那种情况下，如果分母非零，那么计算结果就是 0。当在 if 等条件语句中拿这个计算做判断时，就会出现问题。我们可
       能不会专门去判断函数返回值是否为 None，而是会假定：只要返回了与 False 等效的运算结果，就说明函数出错。
    6. 如果 None 这个返回值，对函数有特殊意义，那么在编写 Python 代码来调用该函数时，就很容易犯上面这种错误。由此可见，令函数返回 None，
       可能会使调用它的人写出错误的代码。有两种方法可以减少这种错误。
    7. 第一种方法，是把返回值拆成两部分，并放在二元组里面。二元组的首个元素，表示操作是否成功，接下来的那个元素，才是真正的运算结果。
    8. 第二种方法更好一些，那就是根本不返回 None，而是把异常抛给上一级，使得调用者必须应对它。
    9. 总结：
       - 用 None 这个返回值来表示特殊意义的函数，很容易使调用者犯错，因为 None 和 0 及空字符串之类的值，在条件表达式里都会评估为 False。
       - 函数在遇到特殊情况时，应该抛出异常，而不要返回 None。调用者看到该函数的文档所描述的异常之后，应该就会编写相应的代码来处理它们了。
"""


# Example One
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


result = divide(10, 2)
if result is None:
    print("Invalid inputs ...")
print(result)
print('--------------------------')

# Example Two
result = divide(0, 5)
if not result:
    print("Invalid inputs ...")  # This is wrong!
print(result)
print('--------------------------')


# Example Three
def divide_two(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = divide_two(0, 5)
if not success:
    print("Invalid inputs ...")  # This is wrong!
print(result)
print('--------------------------')


# Example Four
def divide_three(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs ...") from e


try:
    result = divide_three(5, 2)
except ValueError:
    ValueError("Invalid inputs ...")
else:
    print("Result is %.1f" % result)
print('--------------------------')
