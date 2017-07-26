"""字符串排序。"""
if __name__=='__main__':
    str1=input('input string1:\n')
    str2 = input('input string2:\n')
    str3 = input('input string3:\n')
    print (str1,str2,str3)

    if str1>str2:
        str1,str2=str2,str1
    if str1>str3:
        str1,str3=sttr3,str1
    if str2>str3:
        str2,str3=str3,str3
    print(str1,str2,str3)


