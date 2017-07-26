
profit = int(input())
a = 0
if profit<=10:
	a = profit * 0.1
if profit <=20 and profit >10:
	a = 10*0.1 + (profit-10)*0.075
if profit > 20 and profit <= 40:
	a = 10*0.1+10*0.075+(profit-20)*0.05
if profit >40 and profit <= 60:
	a= 10*0.1+10*0.075+20*0.05+(profit-40)*0.03
if profit >60 and profit <=100:
	a=10*0.1+10*0.075+20*0.05+20*0.03+(profit-60)*0.15
if profit >100:
	a=10*0.1+10*0.075+20*0.05+20*0.03+40*0.15+(profit-100)*0.01
print (a);



