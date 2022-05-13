# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-13 10:11:14
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-13 11:12:37


# 第二十条：用 None 和文档字符串来描述具有动态默认值的参数

"""
    1. 有时我们想采用一种非静态的类型，来做关键字参数的默认值。
    2. 例如，在打印日志消息的时候，要把相关事件的记录时间也标注在这条消息中，默认情况下，消息里面所包含的时间，应该是调用 log 函数那一刻的时间。
       如果我们以为参数的默认值会在每次执行函数时得到评估，那么就会写出 log 函数的代码。
    3. 两条时间戳是一样的，这是因为 datime.now 只执行了一次，也就是它只在函数定义的时候执行了一次。参数的默认值，会在每个模块加载进来的时候求出，
       而很多模块都是程序启动时加载的。包含这段代码的模块一旦加载进来，参数的默认值就固定不变了，程序不会再次执行 time.now。
    4. 在 Python 中若想正确实现动态默认值，习惯上是把默认值设为 None，并在文档字符串里面把 None 所对应的实际行为描述出来。编写函数代码时，如果
       发现该参数的值是 None，那就将其设为实际的默认值。
    5. 如果参数的实际默认值是可变类型，那就一定要记得用 None 作为形式上的默认值。
    6. 例如，从编码为 JSON 格式的数据中载入某个值。若解码数据时失败，则默认返回空的字典，有些人可能会用到 decode 函数中的错误用法。
    7. 这种错误的根本原因是：foo 和 bar 其实都等于写在 default 参数默认值中那个字典，它们都表示的是同一个字典对象。解决办法，是把关键字参数的默
       认值设为 None，并在函数的文档字符串中描述它的实际行为。
    8. 总结：
       - 参数的默认值，只会在程序加载模块并读到本函数的定义时评估一次。对于 {} 或 [] 等动态的值，这可能会导致奇怪的行为。
       - 对于以动态值作为实际默认值的关键字参数来说，应该把形式上的默认值写为 None，并在函数的文档字符串里面描述该默认值所对应的实际行为。
"""


# Example One
from datetime import datetime
import time

def log(message, when=datetime.now()):
    print("%s:%s" % (when, message))


log('Hi, there!')
time.sleep(0.1)
log('Hi, again!')
print("-" * 40)


# Example Two
def log_two(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print
        when: datetime of when the message occurred.
            Defaults to the present time.

    """
    when = datetime.now() if when is None else when
    print("%s:%s" % (when, message))


log_two('Hi, there!')
time.sleep(0.1)
log_two('Hi, again!')
print("-" * 40)


# Example Three
import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print("Foo:", foo)
print('Bar:', bar)
print("-" * 40)


# Example Four
def decode_two(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode_two("bad data")
foo["stuff"] = 5
bar = decode_two("also bad")
bar["meep"] = 1
print("Foo:", foo)
print('Bar:', bar)
print("-" * 40)




