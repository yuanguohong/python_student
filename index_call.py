#实例变可调用抽象对象

#例一

class Person(object):
    def __init__(self , name , gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('my name is' , self.name , "，")
        print('my friend is' , friend , "。")

p = Person('guohong' , "male")
p("wu")


#例二
# 斐波那契数列（写的很好）

class Fib(object):
    def __call__(self, number):
        L , x , y = [] , 0 , 1
        for i in range(number):
            L.append(x)
            x , y = y , x + y

        return L

f = Fib();
print(f(1))