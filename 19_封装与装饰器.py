#coding:utf-8

'''
封装、装饰器、类中的装饰器

'''

'''
封装：将不对外的私有属性或方法通过可对外使用的函数而使用（类中定义私有的，只有类内部使用，外部无法访问）
原因主要是：保护隐私，明确区分内外

'''


'''
装饰器decorator（通俗来说，函数里面还有函数，类似于类）
是一种函数，可以接收函数作为参数，可以返回函数
接受一个函数，内部对其进行处理，然后返回一个新函数，动态增强函数功能

def out(func_args)          #外围函数  func_args参数函数，代表要处理的函数
    def inter(*args,**kwargs)     #内嵌函数
        return func_args(*args,**kwargs)
    return inter          #外围函数中返回内嵌函数

'''


'''
此装饰器对传入函数的结果进行一个检查

'''

def check_str(func):
    def inner(*args,**kwargs):
        print('args:',args,'kwargs:',kwargs)
        result = func(*args,**kwargs)           #在内嵌函数中调用外围函数的参数，并且将参数放回函数，因为要对结果进行检查，所以赋值给result
        if result == 'ok':
            return 'result is %s' %result
        else:
            return 'result is failed:%s' %result
    return inner

@check_str            #将函数与装饰器绑定
def test(data):
    return data

result = test('no')    #传入数据
print(result)

result = test('ok')
print(result)

'''
classmethod装饰器
将类函数可以不经过实例化而直接被调用

@classmethod
def func(cls,……）:   cls替换普通类函数中的self
    do
    
cls替代普通类函数中的self（self只能通过实例化才能调用）cls代表当前操作的是类

'''

class Test(object):
    def __init__(self,a = None):
        '''

        :param a:
        '''
        self.a = a

    def run(self):
        print('run')
        self.jump()   #可以在有self参数的函数内，调用有classmethod装饰器的函数
        self.sleep()  #可以在有self参数的函数内，调用有staticmethod装饰器的函数


    @classmethod     #将类函数可以不经过实例化而直接被调用, cls替换普通类函数中的self
    def jump(cls):
        print('jump')
        # cls.run()     #报错，不能在有classmethod装饰器中调用有self参数的函数
        cls.sleep()     #可以在有self参数的函数内，调用有staticmethod装饰器的函数


    @staticmethod        # 将类函数可以不经过实例化而直接被调用，不需要self或cls，无法在该函数内调用其他类函数和类变量
    def sleep():
        print('sleep')    #不能调用self，也不能调用cls的函数


#通过实例化调用run（）函数,不是实例化是不能调用run函数的，self
t = Test()
# t.run()

#通过类直接调用jump（）函数，因为参数是cls
Test.jump()
# t.jump()    #也可以实例化调用jump


'''
staticmethod装饰器
将类函数可以不经过实例化而直接被调用，不需要self或cls，无法在该函数内调用其他类函数和类变量

@staticmethod
def func(……)
    do
'''

# Test.sleep()  #不经过实例化可以调用有staticmethod装饰器的函数
# print('-------')
#
# t.sleep()   #实例化也可以调用有staticmethod装饰器的sleep函数


'''
property
将函数的执行免去括弧，类似于调用属性（变量）
'''

class Test1(object):
    def __init__(self,name):
        self.__name = name   #定义一个私有变量name

    @property   #通过property可以将一个函数变成一个类似于变量的存在，不需要加（）就可以读取函数里的返回值
    def name(self):
        return self.__name

    #给property封装器里的函数的返回值进行调整或者赋值
    @name.setter
    def name(self,value):
        self.__name = value

t1 = Test1(name='miaomiao')
t1.name           #调用函数name（）
print(t1.name)

t1.name = '小花'
print(t1.name)