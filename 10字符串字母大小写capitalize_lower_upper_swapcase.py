# coding:utf-8

'''
对象，每个对象都有各自的属性和方法（函数或功能）

'''

'''
capitalize将字符串的首字母变换大写，只对第一个字母有效
只对字母有效，对数字和中文没有效果；首字母已经大写，则无效。
'''
# name = 'miaomiao'
# info = 'hello 苗苗'
# _info = '苗苗 hello'
#
#
# new_name = name.capitalize()
# new_info = info.capitalize()
# _new_info = _info.capitalize()
#
# print(new_name)
# print(new_info)
# print(_new_info)


'''
casefold()将字符串全体小写，函数括弧内什么都不用填写，只对字符串中的字母有效，如果已经是小写了，则无效
casefold可以将更多语种小写，德语之类的，lower则不行
lower（）将字符串全体小写，函数括弧内什么都不用填写，只对字符串中的字母有效，如果已经是小写了，则无效
'''

message01 = 'How Are You！MIAOMIAO'
message02 = '你好呀，MIAOMIAO'
#
# message01_lower = message01.lower()
# message02_lower = message02.lower()
# print(message01_lower)
# print(message02_lower)
#
# message01_lower01 = message01.casefold()
# message02_lower02 = message02.casefold()
# print(message01_lower01)
# print(message02_lower02)


'''
#upper()将所有字母都变成大写，对字母和数字无效，已经大写的也无效函数括弧内什么都不用填写
'''

message01_upper = message01.upper()
message02_upper = message02.upper()
print(message01_upper)
print(message02_upper)

'''
swapcase()将字符串中的大小写进行替换，大写变小写，小写变大写,对字母和数字无效
'''
message01_swapcase = message01.swapcase()
message02_swapcase = message02.swapcase()
print(message01_swapcase)
print(message02_swapcase)