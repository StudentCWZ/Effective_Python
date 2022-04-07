# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022-04-07 13:36:16
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022-04-07 13:36:48


# 第四条：用辅助函数来取代复杂的表达式

"""
    1. Python 的语法非常精练，很容易就能用一行表达式来实现许多逻辑。
    2. 例如，要从 URL 中解码查询字符串。在下例所举的查询字符中，每个参数都可以表示一个整数值。
    3. 查询字符串中的某些参数可能有多个值，某些参数可能只有一个值，某些参数可能是空白值，还有些参数则没有出现在查询字符之中。
    4. 用 get 方法在 my_values 字典中查询不同的参数时，就有可能获得不同的返回值。
    5. 如果待查询的参数没有出现在字符串，或当该参数的值为空白时能够返回默认值 0，那就更好了。
    6. 这个逻辑看上去似乎并不值得用完整的 if 语句或辅助函数来实现，于是，你可能会考虑用 Boolean 表达式
    7. 这样长的表达式虽然语法正确，但却很难阅读，而且有时也未必完全符合要求。
    8. 应该把它总结为辅助函数了，如果需要频繁使用这种逻辑，那就更应该这样做。
    9. 总结：
        - 开发者很容易过度运用 Python 的语法特性，从而写出那种特别复杂并且难以理解的单行表达式。
        - 请把复杂的表达式一如辅助函数中，如果要反复使用相同逻辑，那么就更应该这么做。
        - 使用 if/else 表达式，要比用 or 或 and 这样的 Boolean 操作符写成的表达式更加清晰。
"""

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(my_values)
print('Red:', my_values.get('red'))
print('Green:', my_values.get('green'))
print('Opacity:', my_values.get('opacity'))
print("--------------------------------------------")


# For query string
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red: %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)
print("--------------------------------------------")


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


yellow = get_first_int(my_values, 'yellow')
print('Yellow: %r' % yellow)
