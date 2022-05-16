# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-16 08:52:20
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-16 10:12:04



# 第二十一条：用只能以关键字形式指定的参数来确保代码清晰

"""
    1. 按关键字传递参数，是 Python 函数的一项强大的特性。由于关键字参数很灵活，所以在编写代码时，可以把函数的用法表达得更加明确。
    2. 例如，要计算两数相除的结果，同时要对计算机的特殊情况进行小心的处理。有时我们想忽略 ZeroDivisionError 异常并返回无穷。有时又想忽略 OverflowError 异常并放回 0。
    3. safe_division 函数用了两个 Boolean 参数，来分别决定是否应该跳过除法计算过程中的异常，而问题就在于，调用者写代码的时候，很可能分不清这两个参数，从而导致难以排查
       的 bug。
    4. 提升代码可读性的一种方法，是采用关键字参数。在默认情况下，safe_division_two 函数会非常小心地计算，并且总是会把计算过程中发生的异常重新抛出。
    5. 现在调用者可以根据自己的具体需求，用关键字参数来覆盖 Boolean 标志的默认值，以便跳过相关的错误。
    6. safe_division_two 函数这种写法还是有缺陷。由于这些关键字参数都是可选的，所以没有办法确保函数的调用者一定会使用关键字来明确指定这些参数的值。即便使用新的定义
       safe_division_two 函数，也依然可以以位置参数的形式调用它。
    7. 对于这种复杂的函数来说，最好是能够保证调用者必须以清晰的调用代码，来阐明调用该函数的意图。在 Python 3 中，可以定义一种只能以关键字的形式提供，而不能按位置提供。
    8. safe_division_three 函数带有两个只能以关键字形式来指定的参数。参数列表里的 * 号，标志着位置参数就此终结，之后的那些参数，都只能以关键字形式来指定。
    9. 与 Python 3 不同，Python 2 并没有明确的语法来定义这种只能以关键字形式指定的参数。不过，我们可以在参数列表中使用 ** 操作符，并且令函数在遇到无效的调用时抛出
       TypeErrors，这样就可以实现与 Python 3 相同的功能了。
    10. ** 操作符与 * 操作符类似，但区别在于，它不是用来接受数量可变的位置参数、而是用来接受任意数量的关键字参数。即便某些关键字参数没有定义在函数中，它也依然能够接受。
    11. 现在，既可以不用带关键字参数的方式来调用 safe_division_four 函数，也可以用有效的关键字参数来调用它。
    12. 与 Python 3 版本的函数一样，我们也不能以位置参数的形式来指定关键字参数的值。此外，调用者还不能传入不符合预期的关键字参数。
    13. 总结：
        - 关键字参数能够使得函数调用的意图更加明确。
        - 对于各参数之间很容易混淆的函数，可以声明只能以关键字形式指定的参数，以确保调用者必须通过关键字来指定它们。对于接受多个 Boolean 标志的函数，更应该这样做。
        - 在编写函数时，Python 3 有明确的语法来定义这种只能以关键字形式指定的参数。
        - Python 2 的函数可以接受 **kwargs 参数，并手工抛出异常，以便模拟只能以关键字形式来指定的参数。
"""


# Example One
def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)
result = safe_division(1, 0, False, True)
print(result)
print("-" * 30)


# Example Two
def safe_division_two(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division_two(1.0, 10**500, ignore_overflow=True)
print(result)
result = safe_division_two(1, 0, ignore_zero_division=True)
print(result)
print("-" * 30)


# Example Three
def safe_division_three(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


# result = safe_division_three(1.0, 10**500, True, False) # 报错
result = safe_division_three(1, 0, ignore_zero_division=True) # ok
print(result)

try:
    safe_division_three(1, 0)
except ZeroDivisionError:
    pass # Excepted

print("-" * 30)


# Example Four
# Python 2
def print_args(*args, **kwargs):
    print("Positional:", args)
    print("keyword: ", kwargs)


print_args(1, 2, foo="bar", stuff="meep")
print("-" * 30)


# Example Five
# Python 2
def safe_division_four(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError("Unexpected **kwargs: %r" % kwargs)
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise

result = safe_division_four(1, 10)
print(result)
result = safe_division_four(1, 0, ignore_zero_division=True)
print(result)
result = safe_division_four(1, 10**500, ignore_overflow=True)
print(result)
print("-" * 30)




