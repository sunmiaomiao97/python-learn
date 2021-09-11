# coding:utf-8

'''
类的继承、父类和子类、

'''
import self as self

'''
继承
通过继承基类（父类）来得到基类的功能，子类可以拥有父类所有属性和方法，子类实例化后可以调用自己的和父类的函数和变量
父类不具备子类自有属性和方法

class parent（object） object是所有类的父类
'''

class Parent(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex



    def talk(self):
        return f'{self.name}are talking!'


    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name}is a boy'
        else:
            return f'{self.name}is a girl'

class ChildOne(Parent):
    def play_football(self):
        return f'{self.name}are playing football'


class ChildTwo(Parent):
    def play_basketball(self):
        return f'{self.name}are playing basketball'


p = Parent(name='小雪爸爸',sex='boy')
result = p.is_sex()
print(result)

print('--------------------------------------------')
c_one = ChildOne(name='夏雪',sex='girl')    #ChildOne类中没有定义name和sex属性，但是可以使用父类中的name和sex
result = c_one.talk()                #ChildOne类中没有talk函数，但是可以调用父类中的talk（）函数
c_one_result = c_one.play_football()
print(c_one_result)
print(result)

print('--------------------------------------------')
c_two = ChildTwo(name='夏雨',sex='boy')
result = c_two.is_sex()             #ChildTwo子类中没有is_sex（）函数，但是实例化后可以继承父类中的此函数
result0 = c_two.play_basketball()
print(result,result0)

'''
super关键字
子类继承父类的方法而使用的关键字

super（子类名，self）.父类函数名()
self是类的实例
'''

'''
多重继承：
可以继承多个弗父类

'''
class Tool(object):
    def work(self):
        return 'tool work'


#class Son(Parent,ChildOne):   #这里没必要继承同时Parent和ChildOne，因为ChildOne已经继承了Parent，其实直接继承ChildOne就可以获取全部父类函数
class Son(ChildOne,Tool):     #继承的父类之间不能有继承关系，不然会匹配出错,左边的类先继承，类中有相同函数，最先执行的先发生作用
    def eat(self):
        return '坐吃山空'

if __name__=='__main__':
    p = Son(name='bubu',sex='boy')
    p_eat = p.eat()
    p_talk = p.work()
    p_ball = p.play_football()
    print(p_eat,p_talk,p_ball)
    print(Son.__mro__)
    #打印结果。继承顺序链(<class '__main__.Son'>, <class '__main__.ChildOne'>, <class '__main__.Parent'>, <class '__main__.Tool'>, <class 'object'>)

