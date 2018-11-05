""" Human resources module

Data table structure:
	* id (string): Unique and random generated identifier
		at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
	* name (string)
	* birth_year (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common



def add(table, record):
	"""
	Add new record to table

	Args:
		table (list): table to add new record to
		record (list): new record

	Returns:
		list: Table with a new record
	"""
	index_id = 0
	record.insert(index_id, common.generate_random(table))
	table.append(record)
	data_manager.write_table_to_file("model/hr/persons.csv", table)
	return table


def remove(table, id_):
	"""
	Remove a record with a given id from the table.

	Args:
		table (list): table to remove a record from
		id_ (str): id of a record to be removed

	Returns:
		list: Table without specified record.
	"""

	for i, record in enumerate(table, 1):
		if str(i) == id_:
			del table[i - 1]
	data_manager.write_table_to_file("model/hr/persons.csv", table)
	return table


def update(table, id_, record):
	"""
	Updates specified record in the table.

	Args:
		table: list in which record should be updated
		id_ (str): id of a record to update
		record (list): updated record

	Returns:
		list: table with updated record
	"""
	for i, item in enumerate(table, 1):
		if str(i) == id_:
			index = 1
			for item_from_table, item_from_new_record in zip(table[i - 1][1:], record):  # TODO [1:] pomijam zchaszowany index
				if item_from_new_record != '':
					table[i - 1][index] = item_from_new_record
				index += 1
	data_manager.write_table_to_file("model/hr/persons.csv", table)
	return table


# special functions:
# ------------------

def get_oldest_person(table):
	"""
	Question: Who is the oldest person?

	Args:
		table (list): data table to work on

	Returns:
		list: A list of strings (name or names if there are two more with the same value)
	"""

	age_list = []
	oldest_list = []
	for person in table:
		age_list.append(person[2])
	age_list = common.sort_my(age_list)
	highest_age = age_list[0]
	for person in table:
		if person[2] == highest_age:
			oldest_list.append(person[1])
	return oldest_list


def get_persons_closest_to_average(table):
	"""
	Question: Who is the closest to the average age?

	Args:
		table (list): data table to work on

	Returns:
		list: list of strings (name or names if there are two more with the same value)
	"""

	age_summed = 0
	closest_to_avg = []
	for person in table:
		age_summed += int(person[2])
	age_avg = age_summed / len(table)
	diff_from_avg = abs(int(table[0][2]) - age_avg)
	for person in table:
		if abs(int(person[2]) - age_avg) < diff_from_avg:
			diff_from_avg = abs(int(person[2]) - age_avg)
	for person in table:
		if abs(int(person[2]) - age_avg) == diff_from_avg:
			closest_to_avg.append(person[1])
	return closest_to_avg
