#coding:utf-8

'''
元组tuple是数据结构，其内容可重复，和列表一样
列表里面可以嵌套列表；元组里面也可以嵌套原则，也可以嵌套列表（但是元组里的列表是不可以后续修改的）

和列表不同之处：
元组比列表占用资源更小；
列表是可变的，元组是不可变的
列表[],元组（）
'''

# in max,min在元组中的应用
# max和min在元组中使用时，列表中的元素不能是多种类型，类型不统一，会报错????视频里面报错了，但是我这里没有报错呀
from typing import Tuple

tuple_test = (1,2,3)
print(tuple_test)
print(type(tuple_test))