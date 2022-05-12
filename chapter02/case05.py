# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-12 10:17:37
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-12 11:27:24


# 第十八条：用数量可变的位置参数减少视觉杂讯

"""
    1. 令函数接受可选位置参数(由于这种参数习惯上写为 *args，所以又称为 star args，星号参数)，能够使代码更加清晰，并能减少视觉杂讯。
    2. 例如，要定义 log 函数，以便把某些调试信息打印出来。假如该函数的参数个数固定不变，那它就必须接受一段信息及一份含有带打印值的列
       表。
    3. log 函数中，即便没有值要打印，只想打印一条消息，调用者也必须手工传入一份空列表。这种写法既麻烦，又显得杂乱。最好是能令调用者把
       第二个参数完全省略掉。
    4. 如果想在 Python 中实现此功能，可以把最后那个位置参数前面加一个 * ，于是，现在的 log_two 函数来说，只有第一个参数 message 是
       调用者必须要指定，该参数后面，可以跟任意数量的位置参数。函数体不需要修改，只需修改调用该函数的代码。
    5. 如果要把已有的列表，传给像 log_two 这样带有变长参数的函数，那么调用的时候，可以给列表前面加上 * 操作符。这样 Python 就会把这
       个列表里的元素视为位置参数。
    6. 接受数量可变的位置参数，会带来两个问题
       - 第一个问题是，变长参数在传给函数时，总是要先转化成元组。这就意味着，如果带有 * 操作符的生成器为参数，来调用这种函数，那么
         Python 就必须先把该生成器完整的迭代一轮，并把生成器所生成的每一个值，都放入元组之中。这可能会消耗大量内存，并导致程序崩溃。
         只有当我们能够确定输入的参数个数比较少时，才应该令函数接受 *arg 式的变长参数。在需要把很多字面量或变量名称一起传给某个函数
         的场合，使用这种变长参数，是比较理想的。该参数主要是为了简化程序员的编程工作，并使得代码更加易读。
        - 使用 *arg 参数的第二个问题是，如果以后要给函数添加新的位置参数，那就必须修改原来调用该函数的那些代码。若是只给参数列表前方
          添加新的位置参数，而不更新现有的调用代码，则会产生难以调试的错误。
    7. log_three 函数中的第二条 log 语句是以前写好的，当时的 log 函数还没有 sequence 参数，现在多了这参数，使得 7 从 values 值的
       一部分，变成了 message 参数的值，这种 bug 很难追踪，因为这段代码仍然可以运行，而且不抛出异常。为了彻底避免此类情况，我们应该
       使用只能以关键字形式指定的参数，来扩展这种接受 *args 的函数。
    8. 总结：
       - 在 def 语句中使用 *args，即可令函数接受数量可变的位置参数。
       - 调用函数时，可以采用 * 操作符，把序列中的元素当成位置参数，传给该函数。
       - 对生成器使用 * 操作符，可能导致程序耗尽内存并崩溃。
       - 在已经接受 *args 参数的函数上面继续添加位置参数，可能会产生难以排查的 bug。
"""


# Example One
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s: %s" % (message, values_str))


log('My numbers are', [1, 2])
log("Hi there", [])
print("-" * 30)


# Example Two
def log_two(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s: %s" % (message, values_str))


favorites = [7, 33, 99]
log_two("Favorite color: ", *favorites)
print("-" * 30)


# Example Three
def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)
print("-" * 30)


# Example Four
def log_three(sequence, message, *values):
    if not values:
        print("%s: %s" % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print("%s: %s: %s" % (sequence, message, values_str))


log_three(1, "Favorites", 7, 33)
log_three('Favorite numbers', 7, 3)
print("-" * 30)







