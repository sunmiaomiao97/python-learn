# coding:utf-8

'''
集合不能通过索引获取元素
没有获取元素的方法
集合知识用来处理列表和元组的临时类型，不适合存储与传输
集合知识用来处理列表和元组的临时类型，不适合存储与传输

add()
set.add(item)  没有返回值
set是当前集合
he update功能一样，但是add每次智能添加一个
'''

a_list = ['python','java']

a_set = set()

a_set.add(a_list[0])
a_set.add(a_list[1])
print(a_set)

a_set.add(True)
a_set.add(None)
print(a_set)

'''
set.update(iterable) 无返回值，直接作用于原集合
iterable 集合、列表、元组、字符串
'''
a_set.update([3,4,5])
print(a_set)

tuple = ('a','b','c')
a_set.update(tuple)
print(a_set)

'''
集合的交集
a_set.intersection(b_set……)
b_set……是与当前集合对比的1个或者多个集合
返回的是当前集合与对比集合的交集

'''

#三个人名列表
a = ['xiaolan','xiaohong','xiaozi','xiaohua']
b = ['xiaobai','Gpang','xiaotu','xiaolan']
c = ['liangbo','xiaolan']
print(a,b,c)

#将三个列表转化为三个集合
s_set = set(a)
m_set = set(b)
n_set = set(c)
print(s_set,m_set,n_set)

#寻找三个集合的交集

print('三家超市都去过的人是：',s_set.intersection(m_set,n_set))

'''集合的并集
union（） 返回多个集合的并集
a_set.union(b_set……)
b_set……是与当前集合对比的1个或者多个集合
'''

un = s_set.union(m_set,n_set)
print('去过超市的全部人员如下：',un)

'''判断两个集合中是否有相同元素
isdisjoint()  返回布尔值没有相同的返回true。有相同的返回false
a_set.isdisjoint(b_set)
'''

print(m_set.isdisjoint(n_set))
