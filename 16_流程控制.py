#coding:utf-8

'''
逻辑判断


'''

#遇到:，下面就是新的代码块，要进行缩进

'''if条件语句
Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
if 判断条件:
    执行语句……
else:
    执行语句……
'''

info = 'my name is xiaomu'
info_list = info.split()  #split()方法。可以按照空格分离
print(info_list)

if info_list[0] == 'xiaomu':
    info_list[0] = 'miaomiao'

if info_list[1] == 'xiaomu':
    info_list[1] = 'miaomiao'

if info_list[2] == 'xiaomu':
    info_list[2] = 'miaomiao'

# if info_list[3] == 'xiaomu':
#     info_list[3] = 'miaomiao' #所以写3和索引写-1，实现的是一样的
if info_list[-1] == 'xiaomu':
    info_list[-1] = 'miaomiao'

print(info_list)

# info = ''.join(info_list)   #用于将序列中的元素以指定的字符连接生成一个新的字符串
# info = '-'.join(info_list)
print(info)


print('这里来判断：')
if info_list[1] == 'name' and len(info) !=15:
    print(info_list)
else:
    print(info)



'''
elif语句
if bool_result:
    do
elif bool_result:
    elifdo
elif bool_result:
    elifdo
else:
    do

'''


'''
循环控制
for循环
for item in iterable
    print(item)

iterable一切可以循环的数据类型
item是iterable中的每一个成员
'''
print('-------列表中的for循环---------')

l = ['小蓝','小紫','小红','小花']

for item in l:    #这里是循环列表，不是判断，所以item不是一个具体的值，而是一个变量，可以取变量名name,就是在for循环时，把L里的变量取出来赋值给item
    print(item)
print('finish')


print('-------字符串中的for循环---------')

for i in 'python':   #循环字符串
    print(i)


#循环字典
print('-------字典中的for循环---------')
users = {'name':'miaomiao','age':33}
for k in users:
    print(k)
   # print(users(k))

#嵌套for循环

a = [1,2,3]
b = [4,5,6]

for i in a:
    for j in b:
        print(i, j)

for i in a:
    print(i)
    print('------')
    for j in b:
        print(j)
    print('=======')
print(i,j)  #i循环了3次，j循环了6次



'''
while 循环

while bool_result:
    do

'''

count = 1
total = 0

while count <=100:
    total +=count
    count +=1
print(total)


'''
continue停止本次循环，进入下一次的循环
break停止循环
二者都需要在循环体内使用
'''

user =[
    {'username':'miaomiao','age':23,'sex':'女'},
    {'username':'xiaolan','age':20,'sex':'男'},
    {'username':'xiaohong','age':23,'sex':'男'},
    {'username':'xiaohua','age':23,'sex':'不详'}
]

# man = []
#
# for user in users:
#     if user.get('sex') == '女':
#         continue
#     man.append(user)
#     print('%s 加入了大家庭'% user.get('username'))
#
# print(man)

l =range(100)

for i in l:
    if i == 80:
        print('------')
        print('已经循环80次啦')
       # break        #这里使用了break，所以循环到80次，直接退出循环了
    print(i)
else:
    print('循环完毕啦！')



