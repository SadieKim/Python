# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:59:58 2021

@author: jzx
"""

"""
6-1 人 ：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键
first_name 、last_name 、age 和city 。将存储在该字典中的每项信息都打印出来。
"""
person_info={
    'first_name':'sadie',
    'last_name':'kim',
    'age':24,
    'city':'bengbu',
    }
print("first_name: "+person_info['first_name'].title())
print("last_name: "+person_info['last_name'].title())
print("age: "+str(person_info['age']))
print("city: "+person_info['city'].title())

"""
6-2 喜欢的数字 ：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中
的键；想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为
让这个程序更有趣，通过询问朋友确保数据是真实的。
"""
favorite_number={
    'li liu':6,
    'bob':17,
    'cindy':10,
    'sadie':8,
    'ella':66,
    }
print("Li Liu's favorite number:"+str(favorite_number['li liu']))
print("Bob's favorite number:"+str(favorite_number['bob']))
print("Cindy's favorite number:"+str(favorite_number['cindy']))
print("Sadie's favorite number:"+str(favorite_number['sadie']))
print("Ella's favorite number:"+str(favorite_number['ella']))

"""
6-3 词汇表 ：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
也可在一行打印词汇，再使用换行符（\n ）插入一个空行，然后在下一行以缩进的方式打印词汇的含义。
"""
vocabulary={
    'upper':'capitalize the letters',
    'for':'iteration',
    'str':'transform other data type into string',
    'len':'get the length',
    'in':'judge whether A is existed in B',
   }
print("upper: "+vocabulary['upper'])
print("for: "+vocabulary['for'])
print("str: "+vocabulary['str'])
print("len: "+vocabulary['len'])
print("in: "+vocabulary['in'])
"""
6-4 词汇表2 ：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列
print 语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，再在词汇表中添加5个Python
术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
"""
vocabulary={
    'upper':'capitalize the letters',
    'for':'iteration',
    'str':'transform other data type into string',
    'len':'get the length',
    'in':'judge whether A is existed in B',
   }
for key,value in vocabulary.items():
    print(key+": "+value)
"""
6-5 河流 ：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是
'nile': 'egypt' 。使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
使用循环将该字典中每条河流的名字都打印出来。
使用循环将该字典包含的每个国家的名字都打印出来。
"""
rivers_info={
    'nile':'egypt',
    'changjiang':'china',
    'rhine':'germany',
    }
for key,value in rivers_info.items():
    print("The "+key.title()+" runs through "+value.title()+".")
    
"""
6-6 调查 ：在6.3.1节编写的程序favorite_languages.py中执行以下操作。创建一个应该会接受调查
的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。遍历这个人员名单，对于已参与调查的
人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
"""
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
investigated_list=['jen','phil']
for people in favorite_languages.keys():
    if people in investigated_list:
        print("Dear "+people+" ,thanks for attending investigation!")
    else:
        print("Dear "+people+", we sincerely invite you to attend our investigation!")

"""
6-7 人 ：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个
名为people 的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
"""
person_1={
    'first_name':'sadie',
    'last_name':'kim',
    'age':24,
    'city':'bengbu',
    }
person_2={
    'first_name':'linya',
    'last_name':'Peng',
    'age':24,
    'city':'bengbu',
    }
person_3={
    'first_name':'bob',
    'last_name':'donald',
    'age':24,
    'city':'bengbu',
    }
people=[person_1,person_2,person_3]
for person in people:
    print(person)
"""
6-8 宠物 ：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的
类型及其主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将宠物的所有信息都
打印出来。
"""
kitty={
       'type':'cat',
       'owner':'alice',
     }
bell={
      'type':'dog',
       'owner':'david',
      }
pets=[kitty,bell]
for pet in pets:
    print(pet)
"""
6-9 喜欢的地方 ：创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键；
对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练习更有趣些，可让一些朋友指出他们喜欢的
几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
"""
favorite_places={
    'li liu':['beijing','shanghai','shenzhen'],
    'alice':['paris','london','berlin'],
    'bob':['japan','italy','iceland'],
    }
for key,value in favorite_places.items():
    print(key.title()+"'s favorite places are: ")
    for place in value:
        print(place.title())
        
"""
6-10 喜欢的数字 ：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人
的名字及其喜欢的数字打印出来。
"""
favorite_number={
    'li liu':[6,8,10],
    'bob':[11,13],
    'cindy':[6,66],
    'sadie':[8,10,88],
    'ella':[16,18,25,28],
    }
for key,value in favorite_number.items():
    print(key.title()+"'s favorite number:")
    for number in value:
        print(str(number))
        


"""
6-11 城市 ：创建一个名为cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，
并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中，应包含
country 、population 和fact 等键。将每座城市的名字以及有关它们的信息都打印出来。
"""
cities={
        'paris':{'country':'france','population':'one million','fact':'center of fashion'},
        'london':{'country':'england','population':'five million','fact':'center of finance'},
        'berlin':{'country':'germany','population':'two million','fact':'center of industry'},
        }
for key,value in cities.items():
    print("Information about "+key+":")
    for k,v in value.items():
        print(k+":"+v)














































