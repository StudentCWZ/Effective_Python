# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-19 09:17:12
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-19 11:16:46


# 第二十四条：以 @classmethod 形式的多态去通用地构建对象


"""
    1. 在 Python 中，不仅对象支持多态，类也支持多态。
    2. 多态，使得继承体系中的多个类都能以各自所独有的方式来实现某个方法。这些类，都满足相同的接口和继承自相同的抽象类，但却有着各自不同的功能。
    3. 例如，为了实现一套 MapReduce 流程，我们需要定义公共基类来表示输入的数据。我们可能需要很多像 PathInputData 这样的类来充当 InputData
       的子类，每个子类都需要实现标准接口中的 read 方法，并以字节的形式返回待处理的数据。其他的 InputData 可能会通过网络读取并解压数据。
    4. 此外，我们还需要为 MapReduce 工作线程定义一套类似的抽象接口，以便用标准的方法的方式来处理输入的数据。下面定义具体的 Worker 子类，实现
       我们想要的 MapReduce 功能。本例所实现的功能，是一个简单的换行符计数器。
    5. 刚才这套 MapReduce 实现方式，看上去很好，但接下来却会遇到一个大问题，拿就是如何将这些组件拼接起来。上面写的那些类，都具备合理的接口与适
       合的抽象，但我们必须把对象构建出来才能体现出那些类的意义。最简单的方法是手工构建相关对象，并通过某些辅助函数将这些对象联系起来。
    6. generate_inputs 函数可以列出某个目录的内容，并为该目录下的每个文件创建一个 PathInputData 实例，然后，用 generate_inputs 方法返回的
       InputData 实例来创建 LineCountWorker 实例。
    7. 现在执行这些 Worker 实例，以便将 MapReduce 流程中的 map 步骤派发到多个线程之中。接下来，反复调用 reduce 方法，将 map 步骤的结果合并成
       一个最终值。
    8. 最后，把上面这些代码片段都拼装到函数里面，以便执行 MapReduce 流程的每个步骤。
    9. 但是，这种写法有一个大问题，那就是 MapReduce 函数不够通用。如果要编写其他的 InputData 或 Worker 子类，那就得重写 generate_inputs、
       create_workers 和 mapreduce 函数，以便与之匹配。
    10. 若要解决这个问题，就需要以一种通用的方式来构建对象。在其他编程语言中，可以通过构造器多态来解决，也就是令每个 InputData 子类都提供特殊的
        构造器，使得协调 MapReduce 流程那个辅助方法可以用它来通用地构造 InputData 对象。但是，Python 只允许名为 __init__ 的构造方法，所以我
        们不能要求每个 InputData 子类都提供兼容的构造器。
    11. 解决这个问题的最佳方案，是使用 @classmethod 形式的多态。这种多态形式，其实与 InputData.read 那样的实例方法多态非常相似，只不过它针对的
        是整个类，而不是从该类构建出来的对象。
    12. 现在，我们用这套思路来实现与 MapReduce 流程有关的类。首先修改 InputData 类，为它添加通用的 generate_inputs 类方法，该方法会根据通用的
        接口来创建新的 InputData 实例。
    13. 新添加的 generate_inputs 方法，接收一份含有配置参数的字典，而具体的 Generic_InputData 子类则可以解读这些参数。PathInputData 通过
        config 字典来查询输入文件所在的目录。
    14. 接下来，按照类似方式实现 GenericWorker 类的 create_workers 辅助方法。为了生成必要的输入数据，调用者必须把 GenericInputData 的子类传
        给该方法的 input_class 参数。该方法用 cls() 形式的通用构造器，来构建具体的 GenericWorker 子类实例。
    15. GenericWorker 所展示的重点就是 input_class.generate_inputs，它是个类别的多态方法。此外，我们还看到：create_workers 方法用另一种方式
        构造了 GenericWorker 对象，它是通过 cls 形式来构造的，而不像之前那样，直接使用 __init__ 方法。
    16. 至于具体的 GenericWorker 子类，则只需要修改它所继承的父类即可。
    17. 现在的 mapreduce 函数需要更多的参数，以便用更加通用的方式来操作相关对象。
    18. 总结：
        - 在 Python 程序中，每个类只能有一个构造器，也就是 __init__ 方法。
        - 通过 @classmethod 机制，可以用一种与构造器相仿的方式来构造类的对象。
        - 通过类方法多态机制，我们能够更加通用的方式来构建并拼接具体的子类。
"""


# Example One
import os
from threading import Thread

class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, reset = workers[0], workers[1:]
    for worker in workers:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


tmpdir = os.getcwd()
result = mapreduce(tmpdir)
print("There are", result, "lines")
print("-" * 50)


# Example Two
class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, reset = workers[0], workers[1:]
    for worker in workers:
        first.reduce(worker)
    return first.result


tmpdir = os.getcwd()
config = {"data_dir": tmpdir}
result = mapreduce(LineCountWorker, PathInputData, config)
print("There are", result, "lines")
print("-" * 50)





