
year = int(input())
month=int(input())
day = int(input())

months ={'1':'31','2':'29','3':'31',
		 '4':'30','5':'31','6':'30',
		 '7':'31','8':'31','9':'30',
		 '10':'31','11':'30','12':'31'}

if year%4==0:
	months['2']='28'
b = 0
for a in range(1,month):
    days = int(months[str(a)])
    b = b+days
ccc= b+day
print (ccc);


