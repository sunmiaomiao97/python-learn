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





