import datetime
import time

nowday = datetime.date.today()
print (nowday)
print (nowday.strftime('%d--%m--%Y--%X'))

print(time.strftime('%Y-%m-%d  %X',time.localtime()))
