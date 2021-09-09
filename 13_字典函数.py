# coding:utf-8

'''
[]处理法

dict[key值] 可以是添加字典元素，也可以是修改字典元素，这要看key值是否是字典里的key值，是的话，就是修改

'''

'''
update() 
dict.update(new_dict) 无返回值
元素取两个字典的并集，但是会取新字典里的值（key值相同，但是value值和旧字典里不同的话）
'''

num_dict = {'one':1,'two':5,'three':3}
# new_num_dict = {'one':1,'two':2,'three':3}
new_num_dict = {'one':1,'two':2}
num_dict.update(new_num_dict)
print(num_dict)

'''
dict.setdefault(key,value)获取某个key的value值，如果key不存在于字典中，将会把这对key value作为新元素添加到字典中
key需要获取的key值
value 如果key不存在，对应这个key存入字典的默认值

'''
value = num_dict.setdefault('one',2)  #字典中已经有’one',所以打印出来‘one'对应的仍旧是1，而不是给出的value值2
print(num_dict,value)
value = num_dict.setdefault('four',4)  #字典中没有‘four',所以这对键值就被添加到字典里了
print(num_dict,value)

'''字典中value的获取
value（）
获取字典中键值对中的值（value）
返回value集合的伪劣表（不具备列表所有功能，只能观察）

'''
keys = list(num_dict.keys())     #把num_list的key值都放在一个列表里
values = list(num_dict.values()) #把num_list的value值都放在一个列表里
print(keys,values)
print('{} | {} | {} | {}'.format(keys[0],keys[1],keys[2],keys[3]))   #获取key值
print('{}   | {}   | {}     | {}'.format(values[0],values[1],values[2],values[3])) #获取value值


'''字典中key的获取
dict[key]，key不存在 会报错，确定可以存在时，使用这个更方便

get()获取当前字典中指定的key所对应的value值
dict.get(key,default=None)
key需要获取的value对应的key
default：key不存在时则返回默认值，默认是None，也可以自定义
'''


'''字典的复制函数
copy（） 无参数，返回一个一样的字典，但是内存不一样

'''

fruits = {
    'apple':30,
    'banana':50,
    'pear':100
}

real_fruits = fruits.copy()
print(real_fruits)

real_fruits['orange']= 50     #添加字典元素
real_fruits.update({'cherry':100})  #添加字典元素
print(real_fruits)

#修改value值
real_fruits['apple'] = real_fruits['apple']-5
print(real_fruits)
real_fruits['apple'] = 0
print(real_fruits)

'''
字典中的成员判断
成员运算符in ，not in 可以判断列表、元组和字符串、字典中

get（）函数可以判断成员是否存在
bool（dict.get（'name'） 。

get是取value判断，成员运算符in是对key进行判断
'''
print( 'apple' in real_fruits)   #返回true
print(bool(real_fruits.get('apple')))  #返回了false，apple的值是0？
print(bool(real_fruits.get('cherry')))  #返回true



'''字典中popitem()函数
删除当前字典里末尾一组键值对，并将其返回
dict.popitem() 无参数
返回被删除的键值对，用元组包裹0索引是key,1索引是value
'''


print(real_fruits)
cherry = real_fruits.popitem()
print('水果店的 {} 还有 {} 个'.format(cherry[0],cherry[1]))  #0索引是key,1索引是value
print(real_fruits)  #再次输出，cherry已经被删除里了
