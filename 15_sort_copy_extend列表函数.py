#coding:utf-8

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



