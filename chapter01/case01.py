# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022-04-05 15:37:06
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022-04-05 16:01:17


# 第一条：确认自己所用的 Python 版本

"""
1. 很多电脑都预装了多个版本的标准 CPython 运行的环境。然而，在命令行中输入默认的 python 命令之后，究竟会执行哪个版本则无法确定。
2. python 通常是 python 2.7 的别名，但也有可能是 python 2.6 或者 python 2.5 等旧版本的别名。
3. 请用 --version 标志来运行 python 命令，以了解所使用的具体 Python 版本。
$ python --version
2.7.8
4. 通常可以用 python3 命令来运行 Python 3
$ python --version
3.8.9
5. 运行程序的时候，也可以在内置的 sys 模块里查询相关的值，以确定当前使用的 Python 版本。
6. 下面代码输出结果如下：
sys.version_info(major=3, minor=8, micro=9, releaselevel='final', serial=0)
3.8.9 (default, Feb 18 2022, 07:45:34)
[Clang 13.1.6 (clang-1316.0.21.2)]
7. Python 2 和 Python 3 都处在 Python 社区的积极维护之中，但是 Python 2 的功能开发已经冻结，只会进行 bug 修复、安全增强以及移植等工作，
以便开发者能够顺利从 Python 2 迁移到 Python 3 。
8. 总结：
(1) 有两个版本的 Python 处于活跃状态，它们是：Python 2 和 Python 3 。
(2) 有很多流行的 Python 运行环境，例如，CPython、JPython、IronPython 以及 PyPy 等。
(3) 在操作系统的命令行中运行 Python 时，请确保该 Python 的版本与你想要使用的 Python 版本相符。
"""

import sys  # sys 模块

print(sys.version_info)
print(sys.version)
