# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:19:35 2021

@author: jzx
"""

"""
5-2 更多的条件测试 ：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。对于下面列出的各种测
试，至少编写一个结果为True 和False 的测试。
"""
#检查两个字符串相等和不等。
str='Love'
if 'Love'==str:
    print(True)
else:
    print(False)
    
if 'love'==str:
    print(True)
else:
    print(False)
            
#使用函数lower() 的测试。
if 'love'==str.lower():
    print(True)
else:
    print(False)

if 'lover'==str.lower():
    print(True)
else:
    print(False)
    
#检查两个数字相等、不等、大于、小于、大于等于和小于等于。
number_1=6
number_2=6
number_3=18
number_4=4

print(number_1==number_2)
print(number_1==number_3)

print(number_1!=number_3)
print(number_1!=number_2)

print(number_3 > number_2)
print(number_2 > number_3)

print(number_2 < number_3)
print(number_2 < number_4)

print(number_3 >= number_2)
print(number_2 >= number_3)


print(number_2 <= number_3)
print(number_2 <= number_4)

#使用关键字and 和or 的测试。
age_0=10
age_1=22
if age_0 >= 18 and age_1 >=18:
    print(True)
else:
    print(False)
    
if age_0 >= 18 or age_1 >=18:
    print(True)
else:
    print(False)    

#测试特定的值是否包含在列表中。
friends=['chen ying','lu xuyao','fu yuping']
if 'lu xuyao' in friends:
    print(True)
else:
    print(False)
    
if 'alice' in friends:
    print(True)
else:
    print(False)
    
#测试特定的值是否未包含在列表中。
friends=['chen ying','lu xuyao','fu yuping']
if 'alice' not in friends:
    print(True)
else:
    print(False)
    
if 'lu xuyao' not in friends:
    print(True)
else:
    print(False)
    
"""
5-3 外星人颜色#1 ：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
"""
#edition1
lien_color='green'
if lien_color=='green':
    print("You have got 5 points.")

#edition2
lien_color='red'
if lien_color=='green':
    print("You have got 5 points.")

"""
5-4 外星人颜色#2 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。
"""
#edition1
lien_color='green'
if lien_color=='green':
    print("You have got 5 points.")
else:
    print("You have got 10 points.")

#edition2
lien_color='yellow'
if lien_color=='green':
    print("You have got 5 points.")
else:
    print("You have got 10 points.")

"""
5-5 外星人颜色#3 ：将练习5-4中的if-else 结构改为if-elif-else 结构。
如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
"""
#edition1
lien_color='green'
if lien_color=='green':
    print("You have got 5 points.")
elif lien_color=='yellow':
    print("You have got 10 points.")
else:
    print("You have got 15 points.")

#edition2
lien_color='yellow'
if lien_color=='green':
    print("You have got 5 points.")
elif lien_color=='yellow':
    print("You have got 10 points.")
else:
    print("You have got 15 points.")

#edition3
lien_color='red'
if lien_color=='green':
    print("You have got 5 points.")
elif lien_color=='yellow':
    print("You have got 10 points.")
else:
    print("You have got 15 points.")

"""
5-6 人生的不同阶段 ：设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。"
"""
age=16
if age<2:
    print("He is a infant.")
elif age>=2 and age<4:
    print("He is toddling.")
elif age>=4 and age<13:
    print("He is a children.")
elif age>=13 and age<20:
    print("He is a teenager.")
elif age>=20 and age<65:
    print("He is an adult.")
else:
    print("He is an older.")
    
"""
5-7 喜欢的水果 ：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。
将该列表命名为favorite_fruits ，并在其中包含三种水果。
编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。
"""
favorite_fruits=['oranges','strawberries','cherries']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'oranges' in favorite_fruits:
    print("You really like oranges!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'cherries' in favorite_fruits:
    print("You really like cherries!")
if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")
    
"""
5-8 以特殊方式跟管理员打招呼 ：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问
候消息。遍历用户名列表，并向每位用户打印一条问候消息。
如果用户名为'admin' ，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。
否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
"""
admin=['alice','bob','cindy','admin','david','ella']
for user in admin:
    if user=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+user.title()+", thank you for logging in again.")

"""
5-9 处理没有用户的情形 ：在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
如果为空，就打印消息“We need to find some users!”。
删除列表中的所有用户名，确定将打印正确的消息。
"""
admin=[]
if admin:  
    for user in admin:
        if user=='admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+user.title()+", thank you for logging in again.")
else:
    print("We need to find some users!")

"""
5-10 检查用户名 ：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
创建一个至少包含5个用户名的列表，并将其命名为current_users 。
再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指
出这个用户名未被使用。
确保比较时不区分大消息；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN' 。
"""
current_users=['Alice','bob','Cindy','david','ella']
new_users=['Bob','jennie','rose','lisa','cindy']
for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print("Sorry, the name has been used, please choose another name!")
    else:
        print("The name hasn't been used, you can use it as your username")
        
"""
5-11 序数 ：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
在一个列表中存储数字1~9。
遍历这个列表。
在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序
数都独占一行。
"""
number_list=range(1,10)
for number in number_list:
    if number==1:
        print(str(number)+"st")
    elif number==2:
        print(str(number)+"nd")
    elif number==3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")
