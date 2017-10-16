import re


with open('yangshen.txt',encoding='utf-16') as file:
	lines=file.readlines()
	namelist=[]
	for line in lines:
		d=re.search('第.{1,5}章',line)
		if d:
			filename=d.group()
			namelist.append(filename)

# #create index.txt 	 contain all files name		
# with open('index.txt','a') as indexfile:
# 	for a in namelist:
# 		indexfile.write(a+'\n')
			print(filename)
			with open(filename+'.txt','a') as files:
				files.write(line)

		else:
			try:
				with open(filename+'.txt','a') as files:
					files.write(line)
			except NameError:
				with open('第一章'+'.txt','a') as files:
					files.write(line)
