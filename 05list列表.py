# coding:utf-8


'''
列表就是队列，是各种数据类型的集合，也是一种数据结结构
列表是内容有序且内容可重复的复合类型；列表无限制长度，但是也要控制长度，处理起来比较麻烦
'''

str_array = ['miaomiao','hhhhh',' ','']
int_array =[1,2,1,2,12,]



# 列表长度不为0，其判断真假时就是真
bool_array = [None,None,None,]
print(bool(bool_array))

# in max,min在列表中的应用
# max和min在列表中使用时，列表中的元素不能是多种类型，类型不统一，会报错????视频里面报错了，但是我这里没有报错呀

max_list = [1,'miaomiao',3.1,[1,3,4]]
print(max_list)
print(max(max_list))
print(min(max_list))
