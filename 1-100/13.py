
c= []
for x in range(1,10):
	for y in range(10):
		for z in range(10):
			a = x*100+y*10+z
			b = x**3+y**3+z**3
			if a==b:
				c.append(a)
				print (a)
print(c)

