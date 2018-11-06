
""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
from model import data_manager
from model import common
from model.common import sort_my, convert_possible_item_in_list_into_int


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
	data_manager.write_table_to_file("model/sales/sales.csv", table)
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
	data_manager.write_table_to_file("model/sales/sales.csv", table)
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
	data_manager.write_table_to_file("model/sales/sales.csv", table)
	return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
	"""
	Question: What is the id of the item that was sold for the lowest price?
	if there are more than one item at the lowest price, return the last item by alphabetical order of the title

	Args:
		table (list): data table to work on

	Returns:
		 string: id
	"""
	index_index = 0
	index_title = 1
	index_price = -4
	index_first_game = 0
	min_price = int(table[index_first_game][index_price])
	lowest_price_games = []
	for game in table:
		if int(game[index_price]) < min_price:
			min_price = int(game[index_price])
	for game in table:
		if int(game[index_price]) == min_price:
			lowest_price_games.append(game)
	if len(lowest_price_games) > 1:
		list_titles = sort_my([game[index_title] for game in lowest_price_games])
		for game in lowest_price_games:
			if game[index_title] == list_titles[-1]:
				return game[index_index]
	return lowest_price_games[index_index][index_index]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
	"""
	Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

	Args:
		table (list): data table to work on
		month_from (int)
		day_from (int)
		year_from (int)
		month_to (int)
		day_to (int)
		year_to (int)

	Returns:
		list: list of lists (the filtered table)
	"""
	
	index_month = -3
	index_day = -2
	index_year = -1
	games_from_to = []
	for game in table:
		if year_from < int(game[index_year]) < year_to:
			games_from_to.append(game)
		elif year_from <= int(game[index_year]) <= year_to:
			if month_from < int(game[index_month]) < month_to:
				games_from_to.append(game)
			elif int(game[index_month]) == month_from:
				if int(game[index_day]) > day_from:  # TODO tutaj zmoenimy jeśli dany dzień ma być zawarty
					games_from_to.append(game)
			elif int(game[index_month]) == month_to:
				if int(game[index_month]) < day_to:  # TODO tutaj zmoenimy jeśli dany dzień ma być zawarty
					games_from_to.append(game)
	return convert_possible_item_in_list_into_int(games_from_to)






# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """
    table = data_manager.get_table_from_file("model/sales/sales.csv")
    sale_id_index = 0
    customer_id_index = -1
    for item in table:
        if sale_id == item[sale_id_index]:
            return item[customer_id_index]
    return None


    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code
    sale_id_index = 0
    customer_id_index = -1
    for item in table:
        if sale_id == item[sale_id_index]:
            return item[customer_id_index]
    return None


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    table = data_manager.get_table_from_file("model/sales/sales.csv")
    return set(item[-1] for item in table)


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    return set(item[-1] for item in table)


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code
    table = data_manager.get_table_from_file("model/sales/sales.csv")
    dictionary_of_customer_and_sales_ids = {}
    customer_id_index = -1
    sales_id_index = 0
    for item in table:
        if item[customer_id_index] in dictionary_of_customer_and_sales_ids.keys():
            dictionary_of_customer_and_sales_ids[item[customer_id_index]].append(item[sales_id_index])
        else:
            dictionary_of_customer_and_sales_ids[item[customer_id_index]] = []
            dictionary_of_customer_and_sales_ids[item[customer_id_index]].append(item[sales_id_index])
    return dictionary_of_customer_and_sales_ids



def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code
    dictionary_of_customer_and_sales_ids = {}
    customer_id_index = -1
    sales_id_index = 0
    for item in table:
        if item[customer_id_index] in dictionary_of_customer_and_sales_ids.keys():
            dictionary_of_customer_and_sales_ids[item[customer_id_index]].append(item[sales_id_index])
        else:
            dictionary_of_customer_and_sales_ids[item[customer_id_index]] = []
            dictionary_of_customer_and_sales_ids[item[customer_id_index]].append(item[sales_id_index])
    return dictionary_of_customer_and_sales_ids


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    table = data_manager.get_table_from_file("model/sales/sales.csv")
    dictionary_of_customer_and_sales_ids = {}
    customer_id_index = -1
    sales_id_index = 0
    
    for item in table:
        try:
            dictionary_of_customer_and_sales_ids[item[customer_id_index]] += 1
        except KeyError:
            dictionary_of_customer_and_sales_ids[item[customer_id_index]] = 1
            
    return dictionary_of_customer_and_sales_ids


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    dictionary_of_customer_and_sales_ids = {}
    customer_id_index = -1
    sales_id_index = 0
    
    for item in table:
        try:
            dictionary_of_customer_and_sales_ids[item[customer_id_index]] += 1
        except KeyError:
            dictionary_of_customer_and_sales_ids[item[customer_id_index]] = 1
            
    return dictionary_of_customer_and_sales_ids
