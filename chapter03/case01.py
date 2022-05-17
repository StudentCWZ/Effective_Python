# -*- coding: utf-8 -*-
# @Author: cuiweizhi
# @Date:   2022-05-17 08:54:05
# @Last Modified by:   cuiweizhi
# @Last Modified time: 2022-05-17 10:18:03



# 第二十二条：尽量使用辅助类来维护程序状态，而不要用字典和元组

"""
    1. 作为一门面向对象的编程语言，Python 提供了继承、多态、封装等各种面向对象的特性。
    2. 用 Python 编程时，我们经常需要编写新的类，并且需要规定这些新类的使用者应该如何通过接口与继承体系同该类相交互。
    3. Python 的类和继承使得我们很容易在程序中表达出对象所应具备的行为，也使得我们能够随时改进程序并扩充其功能，以便
       灵活地应对不断的变化的需求。善用类和继承，就可以写出易于维护的代码。
    4. Python 内置的字典类型可以很好地保存某个对象在其生命周期里的动态内部状态。所谓动态，是指这些待保存的信息，其标识符无法提前告知。
       例如，要把许多学生的成绩记录下来，但这些学生的名字，我们事先不知道。于是，可以定义一个类，把学生名字全部保存到字典里面，这样就
       不用把每个学生都表示成对象了，也无须在每个对象中预设一个存放其名字的属性。
    5. 由于字典用起来很方便，所以有可能因为功能过分膨胀而导致代码出现问题。例如，要扩充 SimpleGradebook 类，使它能够按照科目来保存成绩，
       而不像原来那样，把所有科目的成绩都保存到一起。要实现这个功能，可以修改 _grades 字典的结构，把每个学生的名字与另外一份字典关联起来，
       使得学生的名字成为 _grades 字典中每个条目的键，使得另外的那份字典成为该键所对应的值。然后，在另外那份字典中，把每个科目当作键，把
       该科目下的各项成绩当作值，建立映射关系。
    6. 现在需求又变了，除了要记录每次考试的成绩，还需记录此成绩占该科目总成绩的权重，例如，期中考试和期末考试所占的份量，比随堂考试要大。
       实现该功能的方法之一，是修改内部的字典。原来我们是把科目当作键，把该科目各次考试的分数当作值，而现在，则改用一系列元组做为值，每个
       元组都具备(score，weight)的形式。
    7. 但是这种修改，会使得类变得更复杂，那么我们就该从字典和元组迁移到类的体系了。
    8. 用来保存程序状态的数据结构一旦变得过于复杂，就应该将其拆解为类，以便提供更为明确的接口，并更好地封装数据。这样做也能够在接口与具体实
       现之间创建抽象层。
    9. 总结：
       - 不要使用包含其他字典的字典，也不要使用过长的元组。
       - 如果容器中包含简单而又不可变的数据，那么可以先使用 namedtuple 来表示，带稍后需要时，再修改为完整的类。
       - 保存内部状态的字典如果变得比较复杂，那就应该把这些代码拆解为多个辅助类。
"""


# Example One
class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student("Isaac Newton")
book.report_grade("Isaac Newton", 90)
print(book.average_grade("Isaac Newton"))


# Example Two
class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(score)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75)
book.report_grade("Albert Einstein", "Math", 65)
book.report_grade("Albert Einstein", "Gym", 90)
book.report_grade("Albert Einstein", "Gym", 95)
print(book.average_grade("Albert Einstein"))


# Example Three
import collections
Grade = collections.namedtuple("Grade", ("score", "weight"))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class FinalGradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = FinalGradebook()
albert = book.student("Albert Einstein")
math = albert.subject("Math")
math.report_grade(80, 0.10)
print(albert.average_grade())








