"""python 字典(dic) """

#hello
dic = {key1:value1,key2:value2}
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

#方法===dic[key]:取出value（没有key，报KeyError）。
#       dic[key]=NewValue:写入新的值进行覆盖，或者增加新的键值对。
#       del dic[key]:删除键是key的字典条目。
#       del dic:删除字典。
#       dic.clear():清空字典所有条目。
#       dic.copy():返回一个字典的浅复制。
#       dic.get(key,default=None):返回值指定键的值，若值不存在则返回default值。
#       dic.has_key(key):若存在key则返回true，不存在则返回false。
#       dic.items():以列表返回可遍历（键、值）元组组数。
#       dic.keys():以列表返回字典的所有键。
#       dic.values():以列表返回字典所有的值。
#       dic.update(dic2):把字典dic2的键、值更新到dic中。
#       dic.setdedault(key,default=None):若key不存在，添加key，设置values为default。
#       pop(key[default]):删除字典给的key对应的值，返回被删除的值，若不存在，则返回default。

#       len(dic):计算字典的元素个数，即键的总数
#       str(dic):输出字典可打印的字符串表示。


#注意===1、键值对不存在顺序
#       2、键（key）是唯一、不可改变的，若有相同的键，则后一个覆盖前一个，键不可以是列表
