# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-20 09:06:42
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-20 10:42:42


# 第二十五条：用 super 初始化父类


"""
    1. 初始化父类的传统方式，是在子类里用子类实例直接调用父类的 __init__ 方法。
    2. 这种方法对于简单的继承体系是可行的，但是在许多情况下会出现问题。
    3. 如果子类受到多重继承的影响，那么直接调用超类的 __init__ 方法，可能会产生无法预知的行为。在子类里调用 __init__ 的问题之一，是它的调用顺序并不固定。
    4. AnotherWay 类用另外一种顺序来定义它所继承的各个超类，但是并没有修改超类构造器的调用顺序，它还是和以前一样，先调用 TimesTwo.__init__ ，然后才调用
       PlusFive.__init__ ，这就导致该类所产生的结果与其超类的定义顺序不相符。
    5. 还有一个问题发生在钻石形继承之中。如果子类继承自两个单独的超类，而那两个超类又继承自同一个公共基类，那么就构成了钻石形继承体系。这种继承会使钻石顶部的
       那个公共基类多次执行其 __init__ 方法，从而产生意想不到的行为。
    6. 我们可能认为 ThisWay 的实例 value 属性对应输出结果是 27，因为 (5 * 5) + 2 = 27，但实际上却是 7，因为在调用第二个超类的构造器，也就是
       PlusTwo.__init__ 的时候，它会再度调用 MyBaseClass.__init__，从而导致 self.value 重新编变成 5。
    7. Python 2.2 增加了内置的 super 函数，并且定义了方法解析顺序，以解决这一问题。MRO 以标准的流程来安排超类之间的初始化顺序，它也保证钻石顶部那个公共基类的
       __init__ 方法只会运行一次。
    8. 得到 Goodway 实例执行结果为 35 后，我们可能觉得程序的计算顺序和自己所想刚好相反。应该先运行 TimeSFiveCorrect.__init__ ，然后运行
       PlusTwoCorrect.__init__，并得出 (5 * 5) + 2 = 27 才对啊，实际上却不是这样的。程序会与 GoodWay 类的 MRO 保持一致，这个 MRO 顺序可以通过名为 mro 的
       类方法来查询。
    9. 调用 GoodWay(5) 的时候，他会调用 TimesFiveCorrect.__init__，而 TimesFiveCorrect.__init__ 又会调用 PlusTwoCorrect.__init__ ，PlusTwoCorrect.__init__ 会调用
       MyBaseClass.__init__ 。到达了钻石体系的顶部之后，所有的初始化方法会按照与刚才那些 __init__ 相反的顺序来运作。于是，MyBaseClass.__init__ 会先把 value 设为 5，然后
       PlusTwoCorrect.__init__ 会为它加 2 ，使 value 变为 7 ，最后，TimesFiveCorrect.__init__ 会将 value 乘以 5，使其变为 35。
    10. 内置的 super 函数确实可以正常运作，但在 Python 2 中有两个问题值得注意：
        - super 语句写起来有点麻烦，我们必须指定当前所在的类和 self 对象，而且还要指定当前所在类和 self 对象，而且还要指定相关的方法名称(通常是 __init__ )以及那个方法的参数。对于 Python 编程
         新手来说，这种构造凡事有点费解。
        - 调用 super 时，必须写出当前类的名称。由于我们以后很可能修改类体系，所以类的名称也可能会变化，那时，必须修改每一条 super 调用语句才行。
    11. Python 3 则没有这些问题，因为它提供了一种不带参数的 super 调用方式，该方式的效果与用 __class__ 和 self 来调用 super 相同。Python 3 总是可以通过 super 写出清晰、精炼
        而准确的代码。
    12. 由于 Python 3 程序可以在方法中通过 __class__ 变量准确的引用当前类，所以 Explicit 这种写法能够正常运作，而 Python 2 没有定义 __class__ ，故不能采用这种写法。你可能想
        试着用 self.__class__ 做参数来调用 super，但实际上这么做是不行，因为 Python 2 是用特殊方式来实现 super 的。
    13. 总结：
        - Python 采用标准的方法解析顺序来解决超类初始化次序及钻石继承问题。
        - 总是应该使用内置的 super 函数来初始化父类。
"""


# Example One
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


print("-" * 40)


# Example Two
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print("First ordering is (5 * 2) + 5 =", foo.value)
print("-" * 40)


# Example Three
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = AnotherWay(5)
print("Second ordering is (5 * 2) + 5 =", foo.value)
print("-" * 40)


# Example Four
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print("Should be (5 * 5) + 2 = 27 but is", foo.value)
print("-" * 40)



# Example Five
# Python 2
from pprint import pprint


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class Goodway(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(Goodway, self).__init__(value)


foo = Goodway(5)
print("Should be 5 * (5 + 2) = 35 and is", foo.value)
pprint(Goodway.mro())
print("-" * 40)


# Example Six
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value
if Explicit(10).value == Implicit(10).value:
    print(True)
else:
    print(False)
print("-" * 40)






