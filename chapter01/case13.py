# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date:   2022/4/28 13:36
# @Last Modified by:   StudentCWZ
# @Last Modified time: 2022/5/05 15:45


# 第十三条：合理利用 try/except/else/finally 结构中的每个代码块

"""
    1. Python 程序的异常处理可能要考虑四种不同的时机。这些时机可以用 try、except、else 和 finally 块来表述。
    2. 如果既要将异常向上传播，又要在异常发生时执行清理工作，那么就可以使用 try/finally 结构。
    3. 这种结构有一项常见的用途，就是确保程序能够可靠地关闭文件句柄。
    4. open 方法必须放在 try 块后面，因为如果打开文件时，发生异常(例如，由于找不到该文件而抛出 IOError)，那么程序应该跳过 finally 块。
    5. try/except/else 结构可以清晰地描述哪些异常会由自己的代码来处理、哪些异常会传播到上一级。如果 try 没有发生异常，那么就执行 else 块。
       有了这种 else 块，我们可以尽量缩减 try 块内的代码量，使其更加易读。
    6. 如果数据不是有效的 JSON 格式，那么用 json.loads 解码时，会产生 ValueError。这个异常会由 except 块捕获并处理。如果能解码，那么
       else 块查找语句就会执行，它会根据键来查出相关的值。查询时若有异常，则该异常会先向上传播，因为查询语句并不在刚才那个 try 块范围内。
       这种 else 子句，会把 try/except 后面的内容和 except 块本身区分开，使异常的传播行为变得更加清晰。
    7. 如果要在复合语句中把上面几种机制都用到，那就编写完整的 try/except/else/finally 结构。例如，要从文件中读取某项事务的描述信息，处理
       该事务，然后就地更新该文件。为了实现此功能，我们可以用 try 块来读取文件并处理其内容，用 except 块来应对 try 块中可能发生的相关异常，
       用 else 块实时地更新文件并把更新中可能出现的异常回报给上级代码，然后用 finally 块来清理文件句柄。
    8. 总结：
       - 无论 try 块是否发生异常，都可以利用 try/finally 复合语句中的 finally 块来执行清理工作。
       - else 块可以用来缩减 try 块中的代码量，并把没有发生异常时所要执行的语句与 try/except 代码块隔开。
       - 顺利运行 try 块后，若想使某些操作能在 finally 块清理代码之前执行，则可将这些操作写到 else 块中。
"""
# Example One
import json

handle = open("my_file.txt")  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()  # Always run after try:
print('--------------------------')

# Example Two
data_json = json.dumps({"hero": "宋江"})
try:
    result_dict = json.loads(data_json)  # May raise ValueError
except ValueError as e:
    raise KeyError from e
else:
    print(result_dict["hero"])
print('--------------------------')

# Example Three
handle = open("my_data.json", "r+")  # May raise OSError
try:
    data = handle.read()    # May raise UnicodeDecodeError
    op = json.loads(data)   # May raise ValueError
    value = (op["numerator"] / op["denominator"])   # May raise ZeroDivisionError
except ZeroDivisionError as e:
    print(e)
else:
    op["result"] = value
    result = json.dumps(op)
    handle.seek(0)
    handle.write(result)    # May raise IOError
    print(result)
finally:
    handle.close()  # Always runs
