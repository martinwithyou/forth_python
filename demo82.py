class Student(object):
    def __init__(self ,name):
        self.name = name
s = Student('bob')
s.score = 90
print(s)
print(s.name)