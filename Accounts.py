#Pls enter the name and the price for the product
#Wrtie down the information for the product
#check if the file exists on the path;if it does, then pls indicate the user;if not, pls indicate the user as well
#function1--pls enter
def user_enter(products):
	while True:
		name = input('pls enter the name:')
		if name == 'b': 
			break
		price = input('pls enter the price:')
		products.append([name,price])
	return products


#function2--write file
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as file:
		file.write('Name,Price\n')
		for each in products:  
			file.write(each[0]+ ','+ each[1]+ '\n')  

#function3 -- read file
def read_file(filename):
	products = [] 
	with open(filename, 'r', encoding = 'utf-8') as filee:
		for line in filee:
			if line == 'Name,Price\n':
				continue
			products.append(line.strip().split(','))
	return products



filename = 'products.csv'
import os
if os.path.isfile(filename):
	print('You have it in this file!')
	products = read_file(filename)	
	for p in products: 
		print(p[0], '’s price is', p[1]) 
else:
	print('sorry,you did not find it')
products = user_enter(products) 
write_file('products.csv', products)