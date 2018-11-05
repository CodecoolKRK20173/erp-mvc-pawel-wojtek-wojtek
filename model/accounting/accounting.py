""" Accounting module

Data table structure:
	* id (string): Unique and random generated identifier
		at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
	* month (number): Month of the transaction
	* day (number): Day of the transaction
	* year (number): Year of the transaction
	* type (string): in = income, out = outflow
	* amount (int): amount of transaction in USD
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
	data_manager.write_table_to_file("model/accounting/items.csv", table)
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
	data_manager.write_table_to_file("model/accounting/items.csv", table)
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
			for item_from_table, item_from_new_record in zip(table[i - 1][1:],
					record):  # TODO [1:] pomijam zchaszowany index
				if item_from_new_record != '':
					table[i - 1][index] = item_from_new_record
				index += 1
	data_manager.write_table_to_file("model/accounting/items.csv", table)
	return table


# special functions:
# ------------------

def which_year_max(table):
	"""
	Question: Which year has the highest profit? (profit = in - out)

	Args:
		table (list): data table to work on

	Returns:
		number
	"""
	
	index_year = 3
	first_year = 0
	years = []
	for day in table:
		if day[index_year] not in years:
			years.append(day[index_year])
	max_amount = avg_amount(table, years[first_year])
	max_amount_year = years[first_year]
	for year in years:
		if avg_amount(table, year) > max_amount:
			max_amount = avg_amount(table, year)
			max_amount_year = year
	return int(max_amount_year)


def avg_amount(table, year):
	"""
	Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

	Args:
		table (list): data table to work on
		year (number)

	Returns:
		number
	"""
	
	index_year = 3
	index_type = 4
	index_amount = 5
	days = [day for day in table if str(day[index_year]) == str(year)]
	if len(days) == 0:
		return str(f'Year {str(year)} not in library')
	amount_in = 0
	amount_out = 0
	for day in days:
		if day[index_type] == 'in':
			amount_in += int(day[index_amount])
	for day in days:
		if day[index_type] == 'out':
			amount_out += int(day[index_amount])
	return round(((amount_in - amount_out) / len(days)),3)
