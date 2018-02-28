#限制添加的属性#


#例一
class Student(object):
    __slots__ = ('name' , 'gender' , 'score')

    def __init__(self , name , gender , score):
        self.name = name
        self.gender = gender
        self.score = score

s = Student("guohong" , "男" , 22)
print(s.name)
print(s.gender)
print(s.score)




#例二

class Person(object):

    __slots__ = ('name' , 'gender')

    def __init__(self , name , gender):
        self.name = name
        self.gender = gender


class Students(Person):

    __slots__ = ('score')

    def __init__(self , name , gender , score):
        super(Students, self).__init__(name , gender)
        self.score = score

ss = Students("guohong" , "boy" , 87)
ss.score = 90
print(ss.score)


