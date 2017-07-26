x = int(input())
y = int(input())
z = int(input())

if x >= y:
	pass
else:
	x,y=y,x
if x >= z:
    pass
else:
	x,z=z,x
if y>=z:
	pass
else:
	y,z=z,y
print (z,y,x);
