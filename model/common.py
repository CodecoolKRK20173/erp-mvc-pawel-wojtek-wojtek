""" Common functions for models
implement commonly used functions here
"""
import random
import inspect


def generate_random(table):
	"""
	Generates random and unique string. Used for id/key generation:
		 - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
		 - it must be unique in the table (first value in every row is the id)

	Args:
		table (list): Data table to work on. First columns containing the keys.

	Returns:
		string: Random and unique string
	"""

	rand_gen = []
	letters_lower = "qwertyuiopasdfghjklzxcvbnm"
	letters_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
	digits = "0123456789"
	rand_gen.append(random.choice(letters_lower))
	rand_gen.append(random.choice(letters_upper))
	rand_gen.append(random.choice(digits))
	rand_gen.append(random.choice(digits))
	rand_gen.append(random.choice(letters_upper))
	rand_gen.append(random.choice(letters_lower))
	generated = "".join(rand_gen) + "#&"
	for record in table:
		if record[0] == generated:
			generate_random(table)
	return generated


def sort_my(my_list):
	for i in range(len(my_list)):
		for j in range(0, len(my_list)-i-1):
			if my_list[j] > my_list[j+1]:
				my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
	return my_list

def sort_buyers_spending(spending_list):
	sum_index = 1
	sorted_by_amount = sorted(spending_list, reverse = True, key = lambda x: x[sum_index])
	return sorted_by_amount

def convert_possible_item_in_list_into_int(my_list):
	converted_list = []
	for game in my_list:
		item_list = []
		for item in game:
			if item.isdigit():
				item_list.append(int(item))
			else:
				item_list.append(item)
		converted_list.append(item_list)
	return converted_list


def check_double_record(table, inputs):
	if 'accounting_controller.py' in inspect.stack()[4][1]:
		for item in table:
			if item[1] == inputs[0] and item[2] == inputs[1] and item[3] == inputs[2] and item[4] == inputs[3]:
				return True
	else:
		index_title = 1
		for item in table:
			if item[index_title] == inputs[0]:
				return True
	return False
	
	