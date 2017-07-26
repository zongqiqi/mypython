"""python序列：list"""

#hello
lst1 = [1,2,3,4,5]
lst2 = ["a", "b", "c", "d"]

#方法===lst1[0]：序列索引，正方向从0开始，负方向由-1开始。
#       lst1[2:4]:访问部分的列表值。
#       lst1[2]=0:列表可修改，重新赋值。
#       lst[:10:2]:前十个数，每两个取一个。
#       list = lst1+lst2:列表组合。
#       del lst1[2]:使用del语句删除列表的元素。
#       lst2.remove('a'):删除列表某个值的第一个匹配项。

#       len(lst1):列表元素个数。
#       max(lst1):返回列表元素最大值。
#       min(lst1):返回元素最小值。
#       list(seq):将元组转换为列表。

#       list.append(obj):在列表尾部添加新的对象。
#       list.count(obj):统计某个元素在列表中出现的次数。
#       list.extend(seq):在列表尾部一次性追加另一个序列的多个值。
#       list.index(obj):从列表中找到某个值第一个匹配项的索引值。
#       list.insert(index,obj):将对象插入特定位置。
#       list.pop(obj=list[-1]):删除列表的一个元素，默认最后一个元素，返回删除的值。
#       list.remove(obj):删除列表某个值的第一个匹配项。
#       list.reverse():反向列表中的元素（=list[::-1]）
#       list.sort([func]):对原列表进行排序。

#       list_2d = [[0 for col in range(cols)] for row in range(rows)]：创建二维列表。

