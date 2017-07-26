"""请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。"""

W = {'M':'Monday','Tu':'Tuesday','W':'Wednesday',
    'Th':'Thursday','F':'Friday','Sa':'Saturday','Su':'Sunday'}
a = input('First word')
a = a.upper()

if a =="T" or a =="S":
    b=input("second  word")
    b = b.lower()
    a = a+b
print (W[a])


