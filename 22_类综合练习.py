# coding:utf-8

'''
面向函数开发的学生信息库转向面向对象的
实现批量添加、批量删除、批量修改、模糊查找功能
'''

class StudentInfo(object):
    def __init__(self,students):   #把students字典传进去
        self.students = students

    def get_user_by_id(self,student_id):
        return self.students.get(student_id)


    def get_all_students(self):
        for id_, value in self.students.items():       #items()不要忘记s
            print('学号:{},姓名:{},年龄:{},性别:{},班级:{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number']
            ))
        return self.students   #一开始把return放在for循环里了，老师打印出来第一个学生的信息，不能打印全部的信息


    def add_student(self,**student):
        check = self.check_user_info(**student)
        if check != True:
            print(check)
            return
        self.__add(**student)
        #下面这里是重新定义的一个字典，和私有函数__add()的功能是一样的
        # id_ = max(students) + 1
        #
        # self.students[id_] = {
        #     'name': kwargs['name'],
        #     'age': kwargs['age'],
        #     'sex': kwargs['sex'],
        #     'class_number': kwargs['class_number']
        # }


    #实现批量添加，但是这里adds函数用到了check函数，调用add函数的时候又用到了,这样双重的检查浪费时间。
    def adds(self,new_students):    #传进去一个new_students列表
        for student in new_students:
            check = self.check_user_info(**student)
            if check !=True:
                print(check,student.get('name'))
                continue      #如果满足以上要求，就不往下执行了
           # self.add(**student)    #如果满足条件，就调用add()函数，将这一条学生信息添加进去
            self.__add(**student)     #定义了私有函数，可以直接调用私有函数


    # 把双重检查的公用信息拆出来，定义一个私有函数，节省时间
    #私有函数功能是添加新的学号，把新的学生入库
    def __add(self,**student):
        new_id = max(self.students) + 1  #添加一个字典
        self.students[new_id] = student


    def delete_student(self,student_id):
        if student_id not in self.students:
            print('{}并不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('学号是{}，{}同学的信息已经被删除了'.format(student_id, user_info))


    #实现批量删除
    def deletes(self,ids):
        for id_ in ids:
            if id_ not in self.students:       #先判断是否在学生信息库中
                print(f'{id_} 不存在学生库中')
                continue
            student_info = self.students.pop(id_)
            print(f'学号{id_} 学生{student_info["name"]}已经被移除')


    def update_student(self,student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在这个学号:{}'.format(student_id))

        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return

        self.students[student_id] = kwargs
        print('同学信息更新完毕')


    #实现批量更新
    def updates(self,update_students):
        for student in update_students:      #student是字典key是id,对应的是成员信息，update_students（没有ID）是个列表
            id_ = list(student.keys())[0]   #拿学生的学号进行验证，拿key的方法用keys()函数，student.keys()是一个伪列表，用list（）把它转成一个真实的列表，然后通过0索引，把id取出来
            if id_ not in self.students:    #判断学号id是否存在
                print(f'学号{id_}不存在')
                continue
            user_info = student[id_]    #因为要判断学生信息是否完全，所以通过key也就是这个字典中的id，来获取student字典中的value，也就是学生的其他信息
            check = self.check_user_info(**user_info)  #拿到学生信息后，进行验证
            if check != True:                   #如果信息不完全，打印出来
                print(check)
                continue
            self.students[id_] = user_info     #如果信息完全，就可以直接对学生信息进行修改
        print('所有用户信息更新完成')


    def search_users(self,**kwargs):
        values = list(self.students.values())
        key = None
        value = None
        result = []

        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs['sex']
        elif 'class_number' in kwargs:
            key = 'class_number'
            values = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        else:
            print('没有发现搜索的关键字')
            return

        # #精准查找
        # for user in values:
        #     if user[key] == value: #user里的value等于信息库里的value，相等的时候，左边后边问题不大，但是判断存在与否，左右就有影响
        #         result.append(user)
        # return result

        #模糊查找
        for user in values:      #values是一个列表，里面是学生信息[{name,age,sex,……},{},{}……]，通过user拿到成员name
            if value in user[key]:   #value是输入的查找词，是不完整的信息，应该用不完整的信息匹配完整的信息
                result.append(user)
        return result


    def check_user_info(self,**kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '缺少学生年龄'
        if 'sex' not in kwargs:
            return '缺少学生性别'
        if 'class_number' not in kwargs:
            return '缺少学生班级'
        return True       #如果以上条件都满足，则返回True


students = {
    1:{
        'name':'miaomiao',
        'age':23,
        'class_number':'A',
        'sex':'girl'
    },
    2:{
        'name': '小蓝',
        'age': 20,
        'class_number': 'C',
        'sex': 'boy'
    },
    3:{
        'name': '小红',
        'age': 21,
        'class_number': 'B',
        'sex': 'girl'
    },
    4:{
        'name': '小紫',
        'age': 22,
        'class_number': 'A',
        'sex': 'boy'
    },
    5:{
        'name': 'G胖',
        'age': 23,
        'class_number': 'D',
        'sex': 'boy'
    }
}


if __name__ == '__main__':
    student_info = StudentInfo(students)
    user = student_info.get_user_by_id(1)
    print(user)

    print('---------------------------------------------')
    student_info.add_student(name='小花',age=12,sex='boy',class_number='A')
    print(student_info.students)

    print('---------------------------------------------')
    #批量添加学生信息
    users = [
        {'name': 'miaoming', 'age': 23, 'class_number': 'A', 'sex': 'girl'},
        {'name': 'miaohong', 'age': 23, 'class_number': 'A', 'sex': 'boy'}
    ]
    student_info.adds(users)   #通过实例化对象student_info来调用adds函数，然后把users作为参数传进去
    student_info.get_all_students()

    print('---------------------------------------------')
    #批量删除学生信息
    student_info.deletes([7, 8])
    student_info.get_all_students()

    print('---------------------------------------------')
    #批量修改学生信息
    student_info.updates([
        {1:{'name':'miaomiao.sun','age':18,'class_number': 'A', 'sex': 'girl'},
         2:{'name':'孙小蓝','age':10,'class_number': 'B', 'sex': 'boy'}}
    ])
    student_info.get_all_students()

    print('---------------------------------------------')
    #模糊查找
    result = student_info.search_users(name='小')
    print(result)