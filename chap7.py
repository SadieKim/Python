# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:40:26 2021

@author: jzx
"""

"""
7-1 汽车租赁 ：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
"""
car=input("What kind of car do you want?")
print("Let me see if I can find you a "+car)

"""
7-2 餐馆订位 ：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
"""
number_of_guest=input("How many people are there?")
if int(number_of_guest) > 8:
    print("There is no empty table.")
else:
    print("There is an empty table.")

"""
7-3 10的整数倍 ：让用户输入一个数字，并指出这个数字是否是10的整数倍。
"""
number=input("Please input a number:")
if int(number)%10==0:
    print(number+" is an integer multiple of 10.")
else:
    print(number+" is not an integer multiple of 10.")
        
"""
7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。
每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
"""
prompt="Enter a series of pizza ingredients:"
prompt += "\nEnter 'quit' to end the program. " 
active=True
while active:
    ingredient=input(prompt)
    if ingredient!='quit':
        print("We would add "+ingredient+" in this pizza.")
    else:
        active=False

"""
7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；
超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
"""
prompt="Enter your age please:"
prompt += "\nEnter 'quit' to end the program. " 
active=True
while active:
    age=input(prompt)
    if age!='quit':
        if int(age) < 3:
            print("The ticket is free.")
        elif int(age) >= 3 and int(age) < 12:
            print("The ticket is 10$.")
        else:
            print("The ticket is 15$.")
    else:
        active=False

"""
7-6 三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
在while 循环中使用条件测试来结束循环。
使用变量active 来控制循环结束的时机。
使用break 语句在用户输入'quit' 时退出循环。
"""
prompt="Enter your age please:"
prompt += "\nEnter 'quit' to end the program. " 
active=True
while active:
    age=input(prompt)
    if age=='quit':
        break
    else:
        if int(age) < 3:
            print("The ticket is free.")
        elif int(age) >= 3 and int(age) < 12:
            print("The ticket is 10$.")
        else:
            print("The ticket is 15$.")

"""
7-8 熟食店 ：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个
名为finished_sandwiches 的空列表。遍历列表sandwich_orders ，对于其中的每种三明治，都
打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 。所
有三明治都制作好后，打印一条消息，将这些三明治列出来。
"""
sandwich_orders=['egg sandwich','bacon sandwich','fruit sandwich']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("I made your "+sandwich)
    finished_sandwiches.append(sandwich)

print("These sandwiches have been finished:")
for sandwich in finished_sandwiches:
    print(sandwich)

"""
7-9 五香烟熏牛肉（pastrami）卖完了 ：使用为完成练习7-8而创建的列表sandwich_orders ，并
确保'pastrami' 在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息，指出熟食店
的五香烟熏牛肉卖完了；再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。
确认最终的列表finished_sandwiches 中不包含'pastrami' 。
"""
sandwich_orders=['pastrami','egg','bacon','pastrami','fruit','pastrami']
finished_sandwiches=[]
print("Sorry,pastrami sandwiches have been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print("I made your "+sandwich)
    finished_sandwiches.append(sandwich)

print("These sandwiches have been finished:")
for sandwich in finished_sandwiches:
    print(sandwich)
    
"""
7-10 梦想的度假胜地 ：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit 
one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。
"""
dream_places={}
active=True
while active:
    name=input("What's your name?")
    dream_places[name]=input("If you could visit one place in the world, where would you go? ")
    print(name.title()+" would like to "+dream_places[name].title()+".")
    prompt=input("Is there anyone want to attend the survey?")
    if prompt=='no':
        active=False

print("The result of this survey are:")    
for key,value in dream_places.items():
    print(key.title()+" would like to "+value.title()+".")        
        
    