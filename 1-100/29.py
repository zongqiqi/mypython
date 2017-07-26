"""给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。"""


n = str(input('please input a nuumber \n'))
print("%d位数"%len(n))
for a in range(1,len(n)):
    print(n[-a])
