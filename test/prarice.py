# -*- coding:utf-8 -*-

# print("Hello World")

# def greet_user():
# 	"""显示简单的问候语"""
# 	print("HELLO")
# greet_user()

# def greet_user(username):
# 	print("Hello, "+username.title()+'!')
# greet_user('zongqiqi')

"""列表的展开"""
# list1=[1,[2,3,[4,[5,6,[7,[8,[9]]]]]]]
# def flatten(input_list):
# 	output_list=[]
# 	while True:
# 		if input_list==[]:
# 			break
# 		for index,i in enumerate(input_list):
# 			if type(i)==list:
# 				input_list=i+input_list[index+1:]
# 				break
# 			else:
# 				output_list.append(i)
# 				input_list.pop(index)
# 				break
# 	return output_list
# print(flatten(list1))

"""类的使用"""
# class Dog():
# 	"""docstring for Dog"""
# 	def __init__(self, name,age):
# 		self.name = name
# 		self.age = age
		
# 	def sit(self):
# 		print(self.name.title() + " is now sitting. ")

# 	def roll_over(self):
# 		print(self.name.title()+" rolled over!")
# mydog=Dog('willie',6)
# # print("my dog name is "+mydog.name.title()+'.')
# mydog.sit()
# mydog.roll_over()

# class Car():
# 	"""一次模拟汽车的简单尝试"""
# 	def __init__(self, make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading=0
# 	def get_descriptive_name(self):
# 		long_name=str(self.year)+' '+self.make+' '+self.model
# 		return long_name.title()
# 	def read_odometer(self):
# 		print("THis car has " +str(self.odometer_reading)+"miles on it!")
# 	def update_odometer(self,mileage):
# 		"""禁止将里程表读数回拨"""
# 		if mileage>self.odometer_reading:
# 			self.odometer_reading=mileage
# 		else:
# 			print("Do not roll back odometer")
# 	def increament_odoment(self,miles):
# 		self.odometer_reading+=miles


# my_new_car=Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()


with open("asd.txt",'r',encoding='utf8') as f:
	contens=f.read()
	print(contens)
