# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:10:58 2021

@author: jzx
"""

# 3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names=['chen ying','lu xuyao','fu yuping']
print(names[0].title())
print(names[1].title())
print(names[-1].title())

#3-2 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
print("Dear "+names[0].title()+", how are you doing?")
print("Dear "+names[1].title()+", how are you doing?")
print("Dear "+names[2].title()+", how are you doing?")

# 3-3 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，
# 如“I would like to own a Honda motorcycle”。
means_of_transportation=['motorcycle','car','bicycle','bus','subway']
print("I'd like to own a "+means_of_transportation[0])
print("I'd like to own a "+means_of_transportation[1])
print("I'd like to own a "+means_of_transportation[2])
print("I'd like to own a "+means_of_transportation[3])
print("I'd like to own a "+means_of_transportation[4])

"""
3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的）
，你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使
用这个列表打印消息，邀请这些人来与你共进晚餐。
"""
name_list=['Jimmy Choo','Coco Chanel','Barfet']
print("Dear "+name_list[0]+",would you like to have dinner with me?")
print("Dear "+name_list[1]+",would you like to have dinner with me?")
print("Dear "+name_list[2]+",would you like to have dinner with me?")

"""
3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
"""
#以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
print("\nWhat a pity! Miss Chanel can't accept your invitation.")
#修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
del name_list[1]
name_list.insert(1,"Jack Ma")
#再次打印一系列消息，向名单中的每位嘉宾发出邀请。
print("Dear "+name_list[0]+",would you like to have dinner with me?")
print("Dear "+name_list[1]+",would you like to have dinner with me?")
print("Dear "+name_list[2]+",would you like to have dinner with me?")

"""
3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
"""
#以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
print("\nI have found a larger table")
#使用insert() 将一位新嘉宾添加到名单开头。
name_list.insert(0,'Xi jinping')
#使用insert() 将另一位新嘉宾添加到名单中间。
name_list.insert(2,'Bill Gats')
#使用append() 将最后一位新嘉宾添加到名单末尾。
name_list.append('Ma Huateng')
#打印一系列消息，向名单中的每位嘉宾发出邀请。
print("Dear "+name_list[0]+",would you like to have dinner with me?")
print("Dear "+name_list[1]+",would you like to have dinner with me?")
print("Dear "+name_list[2]+",would you like to have dinner with me?")
print("Dear "+name_list[3]+",would you like to have dinner with me?")
print("Dear "+name_list[4]+",would you like to have dinner with me?")
print("Dear "+name_list[5]+",would you like to have dinner with me?")

"""
3-9用len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
"""
print(len(name_list))

"""
3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
"""
#以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
print("\nI'm so sorry.For some reason,now I can only invite two guest to have dinner with me.")
#使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，
#都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
name=name_list.pop()
print("Dear "+name+",I'm so sorry,I can't invite you to have dinner with me.")
name=name_list.pop()
print("Dear "+name+",I'm so sorry,I can't invite you to have dinner with me.")
name=name_list.pop()
print("Dear "+name+",I'm so sorry,I can't invite you to have dinner with me.")
name=name_list.pop()
print("Dear "+name+",I'm so sorry,I can't invite you to have dinner with me.")
#对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
print("Dear "+name_list[0]+",you are still in the guest_list")
print("Dear "+name_list[1]+",you are still in the guest_list")
#使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
del name_list[0]
del name_list[0]
print(name_list)

"""
3-8 放眼世界 ：想出至少5个你渴望去旅游的地方。
 sort永久改变顺序（按字母升序），sorted临时改变顺序
 """
#将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
places=['paris','japan','new york','london','california']

#按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
print(places)

#使用sorted() 按字母顺序打印这个列表，同时不要修改它。
print(sorted(places))
#再次打印该列表，核实排列顺序未变。
print(places)

#使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(sorted(places,reverse=True))
#再次打印该列表，核实排列顺序未变。
print(places)

#使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
places.reverse()
print(places)

#使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
places.reverse()
print(places)

#使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
places.sort()
print(places)

#使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
places.sort(reverse=True)
print(places)