# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022-04-06 15:22:09
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022-04-06 16:52:11


# 第三条：了解 bytes、str 与 unicode 区别

"""
    1. Python 3 有两种表示字符序列的类型：bytes 和 str。前者的实例包含原始的 8 位值；后者的实例包含 Unicode 字符。
    2. Python 2 也有两种表示字符序列的类型，分别叫做 str 和 unicode。与 Python 3 不同的是，str 的实例包含原始的 8 位值；而 unicode 的实例则包含 Unicode 字符。
    3. 把 Unicode 字符表示为二进制数据(也就是原始的 8 位值)有许多种办法，最常见的编码方式就是 UTF-8。
    4. 要想把 Unicode 字符转换成二进制数据，就必须使用 encode 方法，想要把二进制数据转换成 Unicode 字符，则必须使用 decode 方法。
    5. 由于字符类型有别，所以 Python 代码中经常会出现两种常见的使用情景：
        - 开发者需要原始 8 位值，这些 8 位值表示 UTF-8 格式(或其他编码格式)来编码的字符。
        - 开发者需要操作没有特定编码形式的 Unicode 字符。
    6. 在 Python 中使用原始 8 位值与 Unicode 字符时，有两个问题要注意：
        - 第一个问题可能会出现在 Python 2 里面：如果 str 只包含 7 位 ASCII 字符，那么 unicode 和 str 实例似乎就成了同一类型。
            - 可以用 + 操作符把这种 str 与 unicode 连接起来
            - 可以用等价与不等价操作符，在这种 str 实例和 unicode 实例之间进行比较。
            - 在格式字符串，可以用 '%s' 等形式来代表 unicode 实例
        - 那么第二个问题可能出现在 Python 3 里面。如果通过内置的 open 函数获取了文件句柄，那么请注意，该句柄默认会采用 UTF-8 编码格式来操作文件。
        - 而在 Python 2 中文件操作的默认编码格式则是二进制形式。
            - 为了解决这个问题，我们必须用二进制写入模式 'wb' 来开启待操作文件。
"""


# Python 3 字符转换
def to_str(bytes_or_str):
    """bytes 转 str"""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


def to_bytes(bytes_or_str):
    """str 转 bytes"""
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


# Python 2 字符转换
# def to_unicode(unicode_or_str):
#     """str 转 unicode"""
#     if isinstance(unicode_or_str, str):
#         value = unicode_or_str.decode('utf-8')
#     else:
#         value = unicode_or_str
#     return value  # Instance of unicode
#
#
# def to_str(unicode_or_str):
#     """unicode 转 str"""
#     if isinstance(unicode_or_str, unicode):
#         value = unicode_or_str.encode('utf-8')
#     else:
#         value = unicode_or_str
#     return value  # Instance of unicode
