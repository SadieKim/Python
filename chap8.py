# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:48:09 2021

@author: jzx
"""

"""
8-1 消息 ：编写一个名为display_message() 的函数，它打印一个句子，指出你在本章学的是什么。
调用这个函数，确认显示的消息正确无误。
"""
def display_message():
    print("I learned function in this section.")

display_message()


"""
8-2 喜欢的图书 ：编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个
函数打印一条消息，如One of my favorite books is Alice in Wonderland 。调用这个函数，
并将一本图书的名称作为实参传递给它。
"""
def favorite_book(title):
    print("One of my favorite books is "+title)
favorite_book("Alice in Wonderland")
  
  
"""
8-3 T恤 ：编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数
应打印一个句子，概要地说明T恤的尺码和字样。使用位置实参调用这个函数来制作一件T恤；再使用关键字
实参来调用这个函数。
"""
def make_shirt(size,word):
    print("The T-shirt's size is: "+size+", word is "+word.title())
make_shirt('M', 'fabulous')
make_shirt(size='L', word='fantastic')


"""
8-4 大号T恤 ：修改函数make_shirt() ，使其在默认情况下制作一件印有字样“I love Python”的
大号T恤。调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件
印有其他字样的T恤（尺码无关紧要）。
"""
def make_shirt(size,word='I love Python'):
    print("The T-shirt's size is: "+size+", word is: "+word)
make_shirt(size='L')
make_shirt('M')
make_shirt(size='S', word='fantastic')


"""
8-5 城市 ：编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如Reykjavik is in Iceland 。给用于存储国家的形参指定默认值。
为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
"""
def describe_city(name,country='china'):
    print(name.title()+" is in "+country.title())
describe_city('beijing')   
describe_city('paris',country='france') 
describe_city('tokyo','japan')
describe_city(name='new york',country='america')


"""
8-6 城市名 ：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数
应返回一个格式类似于下面这样的字符串："Santiago, Chile"
至少使用三个城市-国家对调用这个函数，并打印它返回的值。
"""
def city_country(city,country):
    info=city+", "+country
    return info.title()
info_1=city_country('paris', 'france')
print(info_1)
info_2=city_country('london', 'england')
print(info_2)
info_3=city_country('berlin', 'germany')
print(info_3)


"""
8-7 专辑 ：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手
的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印
每个返回的值，以核实字典正确地存储了专辑的信息。
"""
def make_album(singer,album):
    album_info={'singer':singer,'album':album}
    return album_info
album_1=make_album('tylor', 'red')
print(album_1)
album_2=make_album('twice', 'knock kncok')
print(album_2)
album_3=make_album('blackpink', 'lovesick girls')
print(album_3)

"""
给函数make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了
歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
"""
def make_album(singer,album,number_of_songs=''):
    if number_of_songs:
        album_info={'singer':singer,'album':album,'number_of_songs':number_of_songs}
    else:
        album_info={'singer':singer,'album':album}
    return album_info
album_1=make_album('tylor', 'red')
print(album_1)
album_2=make_album('twice', 'knock kncok',10)
print(album_2)


"""
8-8 用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和
名称。获取这些信息后，使用它们来调用函数make_album() ，并将创建的字典打印出来。在这个while 
循环中，务必要提供退出途径。"
"""
while True:
    singer=input("Please enter the singer's name:")
    if singer=='q':
        break
    
    album=input("Please enter the album's name:")
    if album=='q':
        break
    print(make_album(singer, album))
    
    
"""
8-9 魔术师 ：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，
这个函数打印列表中每个魔术师的名字。
"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
magicians_name=['alice','bob','cindy']
show_magicians(magicians_name)
    

"""
8-10 了不起的魔术师 ：在你为完成练习8-9而编写的程序中，编写一个名为make_great() 的函数，
对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。调用函数show_magicians() 
，确认魔术师列表确实变了。
"""
def make_great(magicians,new_magicians):
    while magicians:
        magician=magicians.pop() 
        magician='the Great '+magician
        new_magicians.append(magician)
magicians_name=['alice','bob','cindy']
new_magicians=[]
make_great(magicians_name,new_magicians)
show_magicians(new_magicians)
    
"""
8-11 不变的魔术师 ：修改你为完成练习8-10而编写的程序，在调用函数make_great() 时，向它传递
魔术师列表的副本。由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。分别使用
这两个列表来调用show_magicians() ，确认一个列表包含的是原来的魔术师名字，而另一个列表包含的
是添加了字样“the Great”的魔术师名字。
"""
def make_great(magicians,new_magicians):
    while magicians:
        magician=magicians.pop() 
        magician='the Great '+magician
        new_magicians.append(magician)
magicians_name=['alice','bob','cindy']
new_magicians=[]
make_great(magicians_name[:],new_magicians)
show_magicians(new_magicians)
show_magicians(magicians_name)

"""
8-12 三明治 ：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参
（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次
，每次都提供不同数量的实参。
"""
def make_sandwich(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(topping)
make_sandwich('egg','bacon','tomato','chicken') 

"""
8-13 用户简介 ：复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关
你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
"""
def user_profile(first,last,**user_info):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_info=user_profile('zhongxiang','jin',city='bengbu',age='24',sex='female')
print(user_info)   

"""
8-14 汽车 ：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，
还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色
和选装配件。这个函数必须能够像下面这样进行调用：
"""
def build_car(manufacturer,model,**other_info):
    car_info={}
    car_info['manufacturer']=manufacturer
    car_info['model']=model
    for key,value in other_info.items():
        car_info[key]=value
    return car_info
car=build_car('bmw', 'x5', color='red',tow_package=True)    
print(car)


"""
8-16 导入 ：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
在主程序文件中，使用下述各种方法导入这个函数，再调用它：
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
