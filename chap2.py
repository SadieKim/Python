# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#2-1 简单消息： 将一条消息存储到变量中，再将其打印出来。
sentence="加油，小金同志，你是最棒的！"
print(sentence)

#2-2 多条简单消息： 将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。
sentence="加油，小金同志，你是最棒的！"
print(sentence)
sentence="其实是最胖的！"
print(sentence)

#2-3 个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you liketo learn some Python today?”。
name="Jin zhongxiang"
print("Hello "+name+", would you like to learn some Python today?")

#2-4 调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name="jin zhongxiang"
print(name.lower())     #输出名字的小写形式
print(name.upper())     #输出名字的大写形式
print(name.title())     #输出名字的首字母大写形式

"""2-5 名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
Albert Einstein oncesaid,“Apersonwho never madea mistake never tried anything new.”
"""
print('Maxim Gorky once said,"Books are the ladder of human progress."')
    
#2-6 名言2： 重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
famous_person='Maxim Gorky'
quote='"Books are the ladder of human progress."'
print(famous_person+' once said,'+quote)

"""
2-7 剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
"""
name=" angela baby \n\trose marry \n\t cris wu "
print(name)
print(name.lstrip())    #删除左边开头的空格
print(name.rstrip())    #删除右边末尾的空格
print(name.strip())     #删除左边开头和右边末尾的空格

"""2-8 数字8： 编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。为使用print 语句来显示结果，务必将这些表达式用括号括起来，也
就是说，你应该编写4行类似于下面的代码："""
print(5+3)
print(9-1)
print(4*2)
print(int(48/6))

#2-9 最喜欢的数字： 将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。
favorite_number=8
message="My favorite number is: "+str(favorite_number)
print(message)
