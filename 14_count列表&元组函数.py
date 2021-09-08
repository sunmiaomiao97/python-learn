# coding:utf-8

'''
count（）查询元素在列表或元组中的个数，元组用法和列表一致
inttype = list.count(item)
item是想要查询个数的那个元素，如果元素不存在，返回0
'''

name_list = ['miaomiao','dawei','xiaoyue','xiaoyue','xiaoyue']

print(name_list.count('xiaoyue'))
print(name_list.count('xiaohua'))

yue = name_list.count('xiaoyue')
hua = name_list.count('xiaohua')
miao = name_list.count('miaomiao')

print('列表里有 %s 人名字一样,都叫xiaoyue' % yue)
print(f'{hua}个人叫xiaohua')
print('{}个人叫miaomiao'.format(miao))

