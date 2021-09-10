#coding:utf-8


'''
主要内容：类的定义、self一些注意、类的构造函数、私有函数和私有变量、

'''


class Dog(object):       #一般类名的首字母大写  加object可以使用类更多的内置函数
    '''
    一次模拟小狗的简单尝试

    '''


    def __init__(self,name,age=None):    #此方法是Python的默认方法（构造函数），下划线区分其他自定义的方法
        '''
        初始化属性name和age
        :param name:
        :param age:
        '''
        self.name = name
        self.age = age


    def sit(self):     #def 定义类的方法(或方法）
        '''
        模拟小狗坐下的动作
        :return:
        '''
        print(f'{self.name} is now sitting!')

    def roll_over(self):
        '''
        模拟小狗打滚
        :return:
        '''
        print(f'{self.name}rolled over')

xiaohua = Dog(name='小花',age=10)
xiaohua.sit()

#没有构造函数的时候可以这样写的：
# xiaohua = Dog()
# xiaohua.name = '小花'  #实例化对象，类里面的内容是不会被修改的，其他实例化的时候需要重新给值
# xiaohua.sit()

xiaolan = Dog(name='小蓝')      #这里只传了一个name参数。没有传age,因为构造函数定义的时候加给了一个默认None，如果不给默认None，还不传age的话会报错
xiaolan.top = 40
print(xiaolan.top)   #实例化对象可以自定义属性top
# print(xiaohua.top)   #报错，xioahua没有top这个属性，不同实例化自己定义的属性不通用


'''
self是类函数中的必传参数，必须放在第一个参数位置；self是一个对象，代表实例化的变量本身
self可以直接通过点，来定义一个类变量  self.name
self是属性和类的桥梁，属性和函数都可以通过self来调用，如果在类代码块中定义函数（方法）时候不添加self，不论是在类中的其他函数下还是类外调用该方法，都是报错
只有一种是可以调用：就是在这个没有self的函数中定义一个函数，然后去调用
'''



'''类的构造函数'''
#左右各两个下横线，类似形式的都是类的内置函数（方法）

# def __init__(self,name,age):    #此方法是Python的默认方法（构造函数），下划线区分其他自定义的方法
#     '''
#     初始化属性name和age
#     :param name:
#     :param age:
#     '''
#     self.name = name            #参数变成类的变量，可以拿来使用
#     self.age = age



'''
私有函数和私有变量:
就是无法被实例化后的对象调用的函数与变量，类内部是可以调用这些私有函数和私有变量的
只希望类内部业务进行调用，不希望被使用者调用

'''
#变量或者函数前添加__（两个下横线），变量或函数名后面不用添加

class Cat(object):
    '''
    小猫的类
    '''
    __cat_type = 'cat'  #私有变量创建一：通过属性的方式创建私有变量


    def __init__(self,name,sex):
        '''

        :param name:
        '''
        self.name = name
        self.__sex = sex

    def run(self):
        result = self.__run()   #私有变量创建一
        print(result)

    def __run(self):          #用两个下划线定义私有函数run
        return f'{self.__cat_type},小猫{self.name} {self.__sex}开心地奔跑着'

    def jump(self):
        pass  # pass用来占位的，不知道该方法（函数）要实现什么功能的时候，可以用pass先占位，以免造成不书写函数体被报错

    def __jump(self):
        return f'{self.__cat_type} 小猫{self.name} {self.__sex}沙雕地跳着'

class Test(object):
    pass    #pass也可作为类的占位符

cat = Cat(name='棉团儿',sex='boy')
cat.run()
# cat.__run()   #私有函数不可以通过实例化对象来调用


''' 
可以使用以下方法来调用私有化的函数
先查看实例化对象cat中可以使用的函数（方法）,然后可以看到可以绕个路来调用私有函数
'''
print(dir(cat))
#['_Cat__jump', '_Cat__run', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', 'jump', 'name', 'run']

# print(dir(Cat))  #查看类Cat可以使用的函数（方法）
# #['_Cat__jump', '_Cat__run', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# # '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# # '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# # '__str__', '__subclasshook__', '__weakref__', 'jump', 'run'

'''调用私有函数__run ,可以通过_Cat__run()来调用'''

print(cat._Cat__run())

