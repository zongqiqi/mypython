import datetime

d1 = datetime.datetime.strptime('2016-05-22 01:53:00', '%Y-%m-%d %H:%M:%S')

d2 = datetime.datetime.strptime('2017-10-03 12:03:20', '%Y-%m-%d %H:%M:%S')

delta = d1 - d2

print(delta.days)