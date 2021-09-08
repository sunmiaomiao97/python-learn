#coding:utf-8


'''
dict（dictionary）用来表示字典，通过{}将一个个key和value存入字典中
key支持字符串、数字和元组，但是不支持列表，每一个key是唯一的（像是字典的页码）
value支持所有的python的数据类型
3.7之前的字典是无序的，（打印出来顺序或许颠倒的）
3.8是元素顺序不发生改变
'''


# 列表[]可以修改和添加
# 元组()不可修改添加
# 字典{} 是可以进行修改的添加


'''
列表和元组中的字典
'''
dict_array = [{1:1,2:2},{'one':1,'two':2}] #此处的字典可以进行修改，因为字典是作为列表里的元素，列表可以修改的
dict_tuple = ({1:1,2:2},{'one':1,'two':2}) #此处的字典无法进行修改，因为字典是作为元组里的元素，元组一旦创建是无法修改的
print(dict_array)
print(dict_array)

#字典可以使用内置运算符in进行查找
user_info = {'name':'miaomiao','age':23,'height':160}
# result = 'name' in user_info
# print(result)
# result = 'hope' in user_info
# print(result)

#字典可以返回长度
# count = len(user_info)
# print(count)

#字典可以查看布尔类型
# result_bool = bool(user_info)
# print(result_bool)
print(bool(user_info))

#创建空字典
empty_dict = {}
print(bool(empty_dict))

#查看字典的数据类型
# print(type(dict(empty_dict)))
print(type(empty_dict))

#max和min在字典中使用,返回值的是key
print(max(user_info))
print(min(user_info))