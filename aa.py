def my_func(my_list, x, y):
	new_list = []
	for item in my_list:
		if item % x == 0 and item < y:
			new_list.append(item)
	return new_list


def my_func2(my_list, x, y):
	new_list = []
	for item in my_list:
		new_list.append((item + x) ** y)
	return new_list

def main():
	cd = [5, 8, 12, 2, 3]
	print(my_func(cd, 2, 12))
	x = 2
	y = 12
	
	new_list = [item for item in cd if item % x == 0 and item < y]
	print(new_list)
	
	new_list_lambda_1 = lambda cd, x, y: [item for item in cd if item % x == 0 and item < y]
	print(new_list_lambda_1(cd, x, y))

	print(my_func2(cd, 1, 2))
	
	x = 1
	y = 2
	new_list = [((item + x) ** y) for item in cd]
	print(new_list)
	
	new_list_lambda_2 = lambda cd, x, y: [((item + x) ** y) for item in cd]
	print(new_list_lambda_2(cd, x, y))
	
	x = 2
	y = 12
	print(list(filter(lambda a: a if a % x == 0 and a < y else None, cd)), '<--- filter(lambda a: a if a % x == 0 and a < y else None, cd')
	print(list(map(lambda a: a if a % x == 0 and a < y else None, cd)), '<--- map(lambda a: a if a % x == 0 and a < y else None, cd)')
	
	print(list(filter(lambda a: (a+x)**y, cd)), '<---filter(lambda a: (a+x)**y, cd)')
	print(list(map(lambda a: (a+x)**y, cd)), '<--- map(lambda a: (a+x)**y, cd)')
	
	
	
if __name__ == '__main__':
	main()

	
	
	
	


	
	


	
	