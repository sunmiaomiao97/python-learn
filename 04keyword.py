# coding:utf-8

name ='miaomiao'

'''
type函数用来查看数据类型
'''
print(type(name))  #type函数，用来查看数据类型

'''
使用内置符号in
'''
#使用内置符号in，判断'mi' 是否在 'miaomiao'这个字符串中 ->true or false

print('mi' in 'miaomiao')
info = 'python是一个非常有魅力的语言'
result = '魅力' in info
print(result)


'''
内置函数max   返回当前数据中最大的成员值
内置函数min   返回当前数据中最小的成员值
中文符号>字母>数字>英文符号，中文按照拼音首字母来计算
'''
#返回当前数据中最大的成员值。中文符号>字母>数字>英文符号，中文按照拼音首字母来计算
print(max('miaomiao'))

info2 = 'prthon is good!'
print(max(info2))
print(min(info2)) #最小的是空格，所以这里输出的是空格
print('.',min(info2),'.')

new_str = info + info2
print(new_str)

