# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022-04-11 11:30:11
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022-04-11 11:30:11


# 第七条：用列表推导来取代 map 和 filter


"""
    1. Python 提供了一种精练的写法，可以根据一份列表来制作另外一份。这种表达式成为列表推导。
    2. 除非是调用只有一个参数的函数，否则，对于简单情况来说，列表推导要比内置的 map 函数更清晰。如果使用 map，那么就要创建 lambda 函数，以便计算新列表中各个元素的值，这会使代码看起来有些乱。
    3. 列表推导则不像 map 那么复杂，它可以直接过滤原列表中的元素，使得生成的新列表不会包含对应的计算结果。
    4. 把内置的 filter 函数与 map 结合起来，也能达成同样的效果，但是代码会写得非常的难懂。
    5. 字典与集，也有和列表类似的推导机制。编写算法时候，可以通过这些推导机制来创建衍生的数据结构。
    6. 总结:
       - 列表推导要比内置的 map 和 filter 函数清晰，因为它无需额外编写 lambda 表达式。
       - 列表推导可以跳过输入列表中的某些元素，如果改用 map 来做，那就必须辅以 filter 方能实现。
       - 字典与集也支持推导表达式。
"""

# Example one
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
print('---------------------------')

# Example two
squares = map(lambda x: x ** 2, a)
print(squares)
print('---------------------------')

# Example three
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)
print('---------------------------')

# Example Four
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)
print('---------------------------')

# Example five
chile_ranks = {'ghost': 1, 'hero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
print('---------------------------')