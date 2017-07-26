"""打印出杨辉三角形（要求打印出10行如下图）。　　"""

yanghui = [[1, 1]]  # 初始化
for i in range(10-2):   #打印10行，计算的行数只有8行
    l_temp = [1]        #每行的第一个数为1
    for j in range(len(yanghui[i])-1):  #遍历上一行
        l_temp.append(yanghui[i][j]+yanghui[i][j+1])
    else:
        l_temp.append(1)    #最后一行也为1
    yanghui.append(l_temp)  #加入杨辉list中
yanghui.insert(0, [1])      # 按要求添加第一行的元素
for i in yanghui:
    print (i)   
