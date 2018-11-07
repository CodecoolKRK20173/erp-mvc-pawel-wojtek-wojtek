# def get_bigger (a, b):
# 	return a if a > b else b
#
#
# def gets_even_elements_greater_than(collection, x):
# 	if not collection:
# 		raise ValueError('Collection is empty')
# 	for item in collection:
# 		if item > x and item % 2 == 0:
# 			yield item
#
#
# def default_compare(x):
# 	return x[0]
#
# def price_compare(x):
# 	return x[1]
#
# def _compare(x):
# 	return x[2]
#
# def my_max(collection, compare_by=None):
# 	if not collection:
# 		raise ValueError('Collection is empty')
#
# 	if not compare_by:
# 		compare_by = default_compare
# 	# elif compare_by == 1:
# 	# 	compare_by = price_compare
#
# 	max_element = collection[0]
#
# 	for element in collection:
# 		if compare_by(element) > compare_by(max_element):
# 			max_element = element
# 	return max_element


def my_func(my_list, x, y):
	new_list = []
	for item in my_list:
		if item % x ==0 and item < y:
			new_list.append(item)
	return new_list


cd = [5, 8, 12, 2, 3]
my_func(cd, 2, 2)
	


# def main():
	# x = [['woda', 3, 100], ['piwo', 5, 99], ['kawa', 25, 20]]
	# get_max = lambda items: max([item[1] for item in items])
	# # print(my_max(x, price_compare))
	# print(my_max(x, compare_by=lambda x: x[0]))
	# c = 3
	# d = 4
	# # print(get_bigger(c, d))
	# get_bigger_l = lambda a, b: a if a > b else b
	# # print(get_bigger_l(1, 3))
	# gets_even_elements_greater_than_l = lambda collection, x: ValueError('Collection is empty') if not collection else [item for item in collection if item > x and item % 2 == 0]
	# # print(gets_even_elements_greater_than_l([1,2,3,4], 3))
	# # for item in gets_even_elements_greater_than([], 3):
	# # 	print(item)
	


# if __name__ == '__main__':
# 	main()
