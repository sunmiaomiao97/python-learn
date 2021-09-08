# coding:utf-8

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


