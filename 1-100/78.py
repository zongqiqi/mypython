"""找到年龄最大的人，并输出。请找出程序中有什么问题。"""

if __name__=='__main__':
    dic={"li":18,"wang":6,"zhang":20,"sun":22}
    m ='li'
    for key in dic.keys():
        if dic[m]<dic[key]:
            m=key
    print (dic[m])


