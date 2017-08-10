from die import Die

import pygal

#创建一个D6和一个D10
die_1=Die()
die_2=Die(num_sides=10)

#掷骰子多次，并将结果储存在一个列表中
results=[]
for roll_num in range(50000):
	result=die_1.roll()+die_2.roll()
	results.append(result)

frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist=pygal.Bar()
hist.title="Result of rolling a D6 and D10 50000 times"
hist.x_labels=[str(x) for x in range(2,17)]
hist.x_title='Result'
hist.y_title="Frenquency of Result"

hist.add("D6 + D10",frequencies)
hist.render_to_file('dice_visual_1111.svg')