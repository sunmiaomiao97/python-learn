# coding = utf-8

'''
数据类型之间的转换
将自身数据类型变成新的数据类型，并拥有新的数据类型的所有功能
'''

'''
字符串与数字之间的转换
'''

#整型转成字符串 str（）浮点型转成字符串 str（）
new_str = str(124657)
print(new_str,type(new_str))

new_str01 = str(124657.78)
print(new_str01,type(new_str01))


# 字符串转成整型 int（），字符串中内容只能是数字
new_int =int ('999')
print(new_int,type(new_int))

#字符串转成浮点型 float（）
new_float =float ('999.88')
print(new_int,type(new_float))





'''字符串与比特类型bytes的转换'''

#二进制数据流bytes
#一种特殊的字符串，但是在单引号之前要加个b
a = 'heollo miaomiao'
print(a,type(a))

b = b'hello miaomiao'  #比特类型
print(b,type(b))

print(b.capitalize())  #比特类型可以使用字符串函数capitalize
print(b.replace(b'miaomiao',b'xiaolan')) #使用的是比特类型，传参也要是比特类型，需要在字符串前加 b
print(b[4])  #返回的是索引所对应的字母的数字
print(b[:3])  #切片索引获取的是ASCII相对应位置的字母
print(b.find(b'm'))  #可以使用find（）功能

'''
encode() 字符串转化为比特（编码）
字符串的内置函数，返回比特类型
string.encode(encoding = 'utf-8',errors = 'strict')
encoding = 'utf-8'转换成的编码格式，可以是ASCII，gbk，默认是utf-8
errors出错时的处理方法，默认strict，直接抛出错误也可以选择ignore忽略错误
'''

'''
decode() 将比特bytes类型转换成字符串（解码）
返回一个字符串类型
bytes.encode(encoding = 'utf-8',errors = 'strict')
encoding = 'utf-8'转换成的编码格式，可以是ASCII，gbk，默认是utf-8
errors出错时的处理方法，默认strict，直接抛出错误也可以选择ignore忽略错误
'''

c = a.encode('utf-8')  #将字符串a转化为比特类型
print(c,type(c))
print(c.decode('utf-8'))  #将比特类型转换为字符串类型



'''
dir()内置函数
查找所对应的方法
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count',
  'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 
  'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace',
   'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
    'swapcase', 'title', 'translate', 'upper', 'zfill']

'''

print(dir(b))



'''  
元组()，列表[]，集合{}之间的转换

列表、元组转换成集合   set（[]或者（））
元组、集合转换成列表   list（（）或者{}）
列表、集合转换成元组   tuple（[]或者{}）
'''

l = [1,2,3]
m = (1,2,3)
n = {1,2,3}  #区分集合和字典，字典里面是键值对

print(set([1,2,3])) #把列表转换成元组
print (set((1,2,3)))  #把元组转换成集合
print(tuple(l),set(l)) #把列表转换成元组和集合
print(list((1,2,3)))
print(list({1,2,3}))
print(tuple(l))
print(tuple(n))

#所有类型都可以转换成字符串类型
print(str(l),type(str(l)))  #'[1,2,3]' 字符串类型
print(list(str(l))) #['[', '1', ',', ' ', '2', ',', ' ', '3', ']']转换不成原来的样子，会把里面元素分解

