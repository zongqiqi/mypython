"""python文件管理(file)"""

#hello
with open('45.py','r',encoding='utf-8') as f:
    for i in f:#读取所有的行
        print(i)
    print(f.tell())

#with open代码块
#打开方式=== r：只能读。
#           r+：可读可写，不会创建不存在的文件，从顶部开始写，会覆盖此前的内容。
#           w+：可读可写，若文件存在，则覆盖整个文件，若不存在则创建。
#           w：只能写，覆盖整个文件，不存在则创建。
#           a：只能写，从文件底部添加内容，不存在则创建。
#           a+：可读可写，从顶部读取内容，从底部添加，不存在则创建。

#方法===file.write(str):将字符串写入文件，没有返回值。
#       file.close():关闭文件，关闭后文件不能再进行读写操作。
#       file.next():返回文件下一行。
#       file.read([size]):从文件读取指定的字节数，若未给定或为负则读取所有。
#       file.tell():返回文件的当前位置。
#       file.readline([size]):读取整行，包括"\n"字符。
#       file.readlines([size]):读取所有行并返回列表。
#       file.flesh():刷新文件内部缓冲，直接把内部缓存区的数据立刻写入文件。

