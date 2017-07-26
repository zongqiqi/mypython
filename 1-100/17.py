"""17  输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。"""

txt = input("Please input txt")
alpha = 0
number = 0
space = 0
others = 0
for a in txt:
	if a.isalpha():
		alpha+=1
	elif a.isspace():
		space+=1
	elif a.isdigit():
		number+=1
	else:
		others+=1
print( "alpha:%s,number:%s,space:%s,others:%s"% (alpha,number,space,others))


