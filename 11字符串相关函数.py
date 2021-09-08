#coding:utf-8

'''
zfill()为字符串定义长度
newstr = string.zfill(width)
width：新字符串希望的长度

希望的长度小于等于当前字符的长度，则不发生变化；与字符串的字符无关
'''

# heart = 'love'
#
# if __name__ =='__main__':
#     print('   '+heart)
#     print(heart.zfill(9))
#     print(heart.zfill(9))
#     print(heart.zfill(8))
#     print(heart.zfill(6))
#     print(heart.zfill(4))
#     print(heart.zfill(2))



'''
count()返回当前字符串中元素的个数
inttype =string。count（item）
item是查询个数的元素
查询元素不存在，则返回0
'''

#多行字符串用三个单引号？
info = '''
GitHub Universe is coming October 27 and 28. From product deep 
dives to interactive roundtables, you’ll gather the tips, tools, 
and connections to help you do the best work of your life.
'''

a = info.count('a')
b = info.count('b')
c = info.count('c')
d = info.count('d')
f = info.count('f')
print(a,b,c,d,f)

#把它们放到列表里
# number_list = [a,b,c,d,f]
# print(number_list)
# print('在列表中最大的数值是：',max(number_list))
#
# number_dict = {
#     'a':a,
#     'b':b,
#     'c':c,
#     'd':d,
#     'f':f
# }
# print('每个成员对应的数值分别是：',number_dict)


'''
startswith（）判断字符串的开始位是否是某个成员（元素）
string。startswith（item） 返回一个布尔值
endswith（）判断字符串的开始位是否是某个成员（元素）
string。endswith（item） 返回一个布尔值
'''


'''字符串中位置是从左向右，从0开始,空格算一个位置
find()返回想要寻找的成员的位置，找不到位置返回-1
string.find（item）返回一个整型

index()返回想要寻找的成员的位置，找不到会报错
string.index（item）返回一个整型
'''


'''
strip（）去掉字符串左右两边的指定元素，默认是空格
newstr = string.strip(item)括弧内需要传一个想要去掉的元素，可以不填写
lstrip()仅仅去掉字符串开头的指定元素或者空格
newstr = string.lstrip(item)
rstrip()仅仅去掉字符串结尾的指定元素或者空格
newstr = string.rstrip(item)
'''

info = '    my name is miaomiao     '
info_strip = info.strip()  #默认是去掉字符串两端的空格
print('.'+info_strip+'.')

info_01 = 'my name is miaomiao'
new_info_01 =info_01.strip(info_01)
print(new_info_01)
print(len(new_info_01))

print(info_01)
print(info_01.lstrip('m'))  #当左边有空格的时候，左边m去不掉呀，还是一样的，当左边没有空格的时候可以去掉
print(info_01.rstrip('o')) #右边同上

'''
repalce()将字符串中旧的元素替换成新的元素
newstr = string.replace(old,new,max)
max可选，代表替换几个，默认是全部替换全部匹配的old元素
'''

repository = ('Repository name: 仓库名称'   #每行用单引号来引住字符串内容，也是一个定义超长字符串的方法
           'Description(可选): 仓库描述介绍'
           'Public, Private : 仓库权限（公开共享，私有或指定合作者）'
           'Initialize this repository with a README: 添加一个README.md'
           'itignore: 不需要进行版本管理的仓库类型，对应生成文件.gitignore'
           'license: 证书类型，对应生成文件LICENSE)')

repository_replace = repository.replace('仓库','repository',2)
print(repository_replace)

a = '仓库'
b = 'repository'
repository_replace02 = repository.replace(a,b)
print(repository_replace02)

c = '类型'
d =  '**'
repository_replace_all = repository.replace(a,b).replace(c,d)  #一次性处理多种替换
print(repository_replace_all)

'''
字符串中返回bool类型的

isspace（）判断字符串是否有空格组成
booltype =string。isspace（）  无参数  只有空格组成的会返回true

istitle（）判断字符串是否是一个标题类型（英文标题是驼峰型？），该函数只用于英文
booltype = string。istitle()  无参数 

isupper（）判断字符串中的字母是否都是大写，无参数，返回布尔类型

islower（）判断字符串中的字母是否都是小写，无参数，返回布尔类型

'''

title = 'Back of China'
print(title.istitle())