#coding:utf-8
'''
主要内容：函数参数、函数参数的定义、局部变量和全局变量、递归函数、匿名函数lambda
'''

'''
函数分类：
内置函数 python提供的函数
自定义函数

def 函数名（）:
    todo sth

return 只能在函数体中使用,支持返回所有的python类型
有返回值的函数可以直接赋值给一个变量
'''

def add(a,b):
    c = a+b
    return c   #return代表函数的结束，下面的代码不会再执行了
    print('语句不会执行到这里')

result = add(a=1,b=6)
print(result)


# 使字符串首字母大写的函数
def capitalize(data):
    index = 0
    temp = ''

    for item in data:
        if index == 0:
            temp =item.upper()
        else:
             temp += item
        index +=1
    return temp

result = capitalize('hello miaomiao')
print(result)

#print 不支持赋值语句
#return 支持赋值语句

def message(message,message_type):
    new_message = '[%s] %s' % (message_type,message)
    print(new_message)

result = message(message='今天起得很早',message_type='info')  #info代表消息类型
print(result)

# print()只是单纯将对象打印，不支持赋值语句
# return是对函数执行结果的返回，支持赋值语句


'''
函数传参：
必传参数：定义的参数没有默认值，在函数调用时如果不传则会报错，没有默认值且必须在函数执行的时候传递进去的参数，顺序要与参数顺序相同。
默认参数：定义函数时，定义的参数含有默认值，可以有等号赋值语句给与默认值
可变参数：没有固定参数名和数量    如add（*args,**kwargs）

'''

def add(a,b,c=3):   #a,b 是必传参数，c是默认参数，在调用该函数时，a,b必须传值
    return a+b+c

result = add(1,2)
print(result)
result = add(5,6,7)  #默认参数位置传入了新的参数，新的参数会覆盖之前的默认参数
print(result)



'''
add（*args,**kwargs）
*args：可变元组参数，将无参数的值合并成元组；
**kwargs：可变字典参数，代表将有参数与默认值的赋值语句合并成字典
'''

def test_args(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

test_args(1,2,3,4,5,name='miaomiao',age=23,top=174)


def super_args(*args,**kwargs):
    if len(args) >=2:
        print(args[2])
    else:
        print('提示：缺少元素值！')

    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('提示：缺少姓名！')
    print(args,len(args))      #打印的时候是不放*号的
    print(kwargs,len(kwargs))

super_args(1,2,3,4,name='miaomiao',age=23)

print('------------------------')
super_args(1,age=23)

print('------------------------')
super_args(1,name='xiaolan')

#另一种传参方式，定义变量，再传递
print('------------另一种传参方式------------')
a = ('python','django','java')    #定义a变量，是一个元组
b = {'name':'xiaolan'}     #定义b变量，是一个字典
super_args(*a,**b)         #传参的时候记得加上*号，如果a不给*号，会把a等号后面的所有内容当成一个元素对待，元组长度为1


print('-------------参数的多种传递方式-------------')

def test(a,b,*args):
    print(a,b,args)

s = (1,2)
test(1,2,*s)

#赋值传参
#test(a=1,b=2,*s)
#必选参数、默认参数和可选元组参数在一起的时候，如果需要使用赋值传参，需要在定义函数的时候，把元组类型放第一位，之后是必传参数和默认参数（这是一个特例）


print('--------------------------')

def test2(a,b,**kwargs):
    print(a,b,kwargs)

test2(1,2,name='miaomiao')

test2(a=1,b=2,name='xiaohua')
test2(name='xiaolan',age=23,a=1,b=1)   #传参顺序不对应也是可以进行传参的



'''
函数参数的定义
'''
def person(name:str,age:int=23):   #这种定义方法主要方便肉眼查看
    print(name,age)

person(name='xiaolan')

def all(a:int,b:int=3,*args:int,**kwargs:str):
    print(a,b,args,kwargs)

all(1,2,3,'4',name='小红')


'''
全局变量：可以在函数内取出其值，但是在函数内不能修改

局部变量：函数内进行定义和修改的变量

global可以将全局变量在函数体内进行修改（工作中，不建议对全局变量进行修改）
global只支持数字、字符串、布尔类型、空类型；
如果使用列表和字典，可以直接在函数体内使用和修改，不用global

'''

name1 = 'xiaomu'
age = 18
def test5():
    global name1      #要改变多个全局变量，直接一起声明即可
    global age
    name1 = 'xiaohua'
    age =10
test5()
print(name1)   #全局变量这里已经改变成为‘xiaohua'
print(age)


'''
递归函数

返回值直接回到自身函数，就可以达到递归效果。

'''



'''
匿名函数lambda
轻量化函数
即用即删除，适合只需要完成一项功能，但是此功能只在此一处使用的情况

无参数形式：
f=lambda :value
然后赋值给一个变量，用变量进行调用即可，value是具有return效果的
有参数形式：
f=lambda x,y : x*y
'''

f = lambda :1
result = f()
print(result)


f1 = lambda x,y=2:x*y  #如果有必传参数和默认参数，必传参数在前面
print(f1(3,4))

f2 = lambda x,y:x>=y  #如果有必传参数和默认参数，必传参数在前面
print(f2(3,4))


users = [
    {'name':'miaomiao'},
    {'name':'xiaolan'},
    {'name':'xiaohong'}
]

users.sort(key=lambda x:x['name'])   # x代表users列表中的每一个成员，通过lambda，将列表中的每一个成员作为参数传入，然后将key值'name'作为排序的对象
print(users)










