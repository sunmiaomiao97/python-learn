#coding:utf-8

'''

赋值运算符
=等于运算符
+=加法
-=减法
*=乘法
/=除法
%=取模
**=幂运算符
//=整除运算符

'''

a=1
b=2
c=3

# d=a+b+c
# d+=c
# print(d)

a/=b
print(a)

c%=2
print(c)

# b,kb,mb,gb转换

#字符串无法和字符串做乘法
# 字符串只可以和数字做乘法
name='miaomiao'
print(name*3)

# 列表和元组可以做乘法,字典
list1 = [1,2,3]
array1 =(1,2,3)
dict1={1:1,2:2,3:3}
print(list1*2)
print(array1*3) #返回的是一个新的元组不是在原来的元组上进行操作
# print(dict1*2) #字典类型不支持乘法