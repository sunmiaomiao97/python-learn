# coding:utf-8

'''
类的内置函数

'''

'''
__setattr__
key当前属性名
'''

class Test(object):
    def __str__(self):         #str() 函数将对象转化为适于人阅读的形式,参数是object -- 对象。返回一个对象的string格式。
        return 'this is a test class'

    def __getattr__(self, item):
        return '这个key:{}并不存在'.format(key)

    def __setattr__(self, key, value):
        print(key,value)
        print(self.__dict__)
        if key not in self.__dict__:
            self.__dict__[key] = value   #将key和value加入到这个字典中

    def __call__(self, **kwargs):
        print('args is {}'.format(kwargs))



t = Test()
print(t)

print('---------')
t.name = 'miaomiao'
print(t.name)


'''
__call__() 可以传任意参数
将一个实例化的类变成一个函数来使用
其返回值可有可无
'''
print('---------')
t1 = Test()
t1(name='miaomiaoya')


#让实例化对象支持链式调用

class Test2(object):
    def __init__(self,attr =''):
        self.__attr = attr

    def __getattr__(self, key):
        if self.attr:             #做判断，attr如果存在
            key ='{}.{}'.format(self.__attr,key)
        else:    #attr如果不存在
            key = key
        print(key)
        return Test2(key)

print('-----------实现链式操作   -------------')
t2 = Test2()
name = t2.a.b.c('miaomiao')        #动态生成一些不存在的函数