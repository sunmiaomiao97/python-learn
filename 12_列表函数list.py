# coding:utf-8

'''
len()函数可以计算除了数字类型以外的其他所有数据类型的长度

列表和元组之间的累加和乘法
new_names = names + names

new_name = names*2

'''
print('下面是列表')
name_list = ['miaomiao','dawei','xiaoyue']
new_name_list = name_list + name_list   #列表之间的累加，直接用加号
new_name_list01 = name_list + ['abc']  #列表可以加列表，但是列表不能加字符串，要把字符串放入列表中，才能实现加法
new_name_list +=['cdf']  #也可以使用加法运算符
print(new_name_list)
print(new_name_list01)

new_name_list02 = name_list*3   #列表乘法
print(new_name_list02)
name_list *=2         #也可以使用乘法运算符
print(new_name_list02)

#元组的加法和乘法
print('下面是元组')
name_tuple = ('miaomiao','dawei','xiaoyue')
new_name_tuple = name_tuple + name_tuple #元组之间的累加
new_name_tuple02 = name_tuple*10   #元组之间的乘法
print(new_name_tuple)
print(new_name_tuple02)

#len()函数计算数据类型的长度
print('name_list的长度是：',len(name_list),'new_name_list的长度是：',len(new_name_list),'new_name_list02的长度是：',len(new_name_list02))
print('name_tuple的长度是：',len(name_tuple),'new_name_list的长度是：',len(new_name_tuple),'new_name_list02的长度是：',len(new_name_tuple02))


'''
in 判断某个成员或者元素是否在该数据结构中
not in 判断某个成员或者元素是否在该数据结构中
'''
print('xiaoyue' in name_list)  #'xiaoyue'在列表中
print('xiaoyue'  not in name_list)

print('xiaoyue'  in name_tuple) #'xiaoyue'在元组中
print('xiaoyue'  not in name_tuple)


'''
list.insert(index,new_item)
index是新的元素要放的位置（数字），如果传入的位置不在列表中，将新元素添加到末尾
字符串、元组、列表的位置都是从0开始计算的
new_item 要添加的新元素（成员）

append()只能将新元素添加到列表末尾
'''

#定义students列表
students = [
    {'id':1,'name':'xiaoyue','sex':'男','age':25},
    {'id':2,'name':'miaomiao','sex':'女','age':23}
]

#定义xiaohua字典
xiaohua = {
    'id':3,'name':'xiaohua','sex':'女','age':10
}

#将xiaohua信息插入学生列表中
students.insert(0,xiaohua)
print(students)

#列表中插入空位
students.insert(3,None)
students.insert(4,None)
print(students)
students.insert(0,None)  #元素不是被替代，而是被挤到后面啦！
print(students)


'''
list.remove(item)
item是准备删除的元素（成员）,元素不存在会报错，
remove（）函数不是返回一个新的列表，而是在原列表上对元素进行修改
'''
name_list = ['miaomiao','dawei','xiaoyue','xiaoyue01','xiaoyue02']
# name_list.remove('xiaoyue01','xiaoyue02') #报错了，一次只能删一个
name_list.remove('xiaoyue')  #也不能删一样名字的，一样名字的有很多个，但是只能删一个
print(name_list)


'''
 del 变量名
 del可以将整个列表变量删除，也可以删除列表中的成员
'''
# del name_list
# print(name_list) #会报错，提示这个变量没有被定义，说明已经被删除了



'''
reverse()将当前列表顺序进行翻转

'''
name_list = ['miaomiao','dawei','xiaoyue']
print(name_list)
# print(name_list.reverse())  #不能这样打印，语法有问题
name_list.reverse()
print('反转后的列表是{}'.format(name_list))


'''
count（）查询元素在列表或元组中的个数，元组用法和列表一致
inttype = list.count(item)
item是想要查询个数的那个元素，如果元素不存在，返回0
'''

name_list = ['miaomiao','dawei','xiaoyue','xiaoyue','xiaoyue']

print(name_list.count('xiaoyue'))
print(name_list.count('xiaohua'))

yue = name_list.count('xiaoyue')
hua = name_list.count('xiaohua')
miao = name_list.count('miaomiao')

print('列表里有 %s 人名字一样,都叫xiaoyue' % yue)
print(f'{hua}个人叫xiaohua')
print('{}个人叫miaomiao'.format(miao))

'''
列表sort函数
sort（）将当前列表按照一定规律排序
list.sort(key=None,revsrse=False)
key参数比较;reverse是排序规则，等于True是降序，等于False是升序
使用sort函数，列表中的元素必须相同类型，否则无法排序
'''
name_list = ['miaomiao','dawei','xiaoyue','xiaoyue01','xiaoyue02']
name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)


'''
clear()将当前列表元素清空

'''
# print('列表长度是：',len(name_list))
# name_list.clear()
# print('清空列表',len(name_list))

'''
list.copy() 无参数，返回一个一模一样的列表
二次赋值的变量与原有变量享有相同的内存空间
但是copy函数新列表与原始列表不是一个内存空间，不同享数据变更

浅拷贝：copy属于浅拷贝
（前提是，列表里的元素还是列表，即有深数据）原件与copy件相互影响，一个变，另一个也变
深拷贝：deepcopy（） 不仅对第一层数据进行
'''
print('这里是copy')
new_name_list = name_list.copy()
print(new_name_list)
print('新列表改变后，老列表情况')
new_name_list.append('xiaomei')  #给新列表添加元素，老列表不会改变
print(new_name_list)
print(name_list)


print('这里是二次赋值')
new_name_list01 = name_list
new_name_list01.append('xiaobai') #在二次赋值的新列表中添加新元素，老列表同样元素同样会改变
print(name_list)

'''
extend()将其他列表或者元组中的元素一次性导入当前列表中
list.extend(iterable) 无返回值，iterable代表要导入列表或元组名
'''
print('这里是extend')
students = ['miaomiao','dawei','xiaoyue']
new_students = ['xiaomei','xiaobai']
students.extend(new_students)
print(students)



'''
索引 列表名[位置]
索引是对单个元素进行访问，切片是对一定范围内的元素进行的访问
切片 列表名[位置范围]  [0:10]
'''

name = ['miaomiao', 'dawei', 'xiaoyue', 'xiaomei', 'xiaobai']
print(name[3])
print(name[0:3]) #切片规则：左含，右不含，所以第三个元素没有被打印出来
print('打印全部元素方法一',name[:])   #打印全部列表元素的方法一
print('打印全部元素方法二',name[0:])  #打印全部列表元素的方法二
print(name[:-1])  #打印全部列表元素的方法三，但是这不能取最后一个元素，因为左含右不含规则
print('反序打印列表',name[::-1])
print('反序切片获取',name[-3:-1]) #负值数字也只能从小到大

print('跳跃获取元素',name[0:4:2])  #第二个冒号后是指跳跃间隔
print('切片生成空列表',name[0:0])

'''列表的修改
列表的修改只能在存在的索引范围内
'''
name[1] = '大奎'
print(name)


