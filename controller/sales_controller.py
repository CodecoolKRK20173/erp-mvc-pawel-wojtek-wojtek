# everything you'll need is imported:
from controller.common import make_crud
from model import data_manager
from model.sales import sales
from view import terminal_view
from controller import common


def run():
	"""
	Starts this module and displays its menu.
	* User can access default special features from here.
	* User can go back to main menu from here.

	Returns:
		None
	"""

	list_options = [
		'Sales',
		'Show all data',
		'Add',
		'Remove',
		'Update',
		'Get lowest price item id',
		'Get items sold between',
		'Exit to main menu'
	]
	data_file = "model/sales/sales.csv"
	crud_module = sales
	while True:
		table = data_manager.get_table_from_file(data_file)
		max_id = len(table)
		list_labels = [
			['Title', str],
			['Price', int],
			['Month', 'month'],
			['Day', 'day'],
			['Year', 'year']
		]
		user_choice = terminal_view.get_choice(list_options)
		if user_choice in ['1', '2', '3', '4']:
			make_crud(crud_module, list_labels, list_options, max_id, table, user_choice)
		elif user_choice == '5':
			result = sales.get_lowest_price_item_id(table)
			terminal_view.print_result(result, "Lowest price item ID")
		elif user_choice == '6':
			inputs_labels_between = [
				['Date from', 'date'],
				['Date to', 'date'],
			]
			inputs = terminal_view.get_inputs(['must'] + inputs_labels_between, 'Date from to')
			inputs = [int(item) for item in inputs]
			result = sales.get_items_sold_between(table, *inputs)
			print(common.bcolors.WARNING + common.bcolors.BOLD)
			terminal_view.os.system('clear')
			if common.check_if_empty(result):
				terminal_view.print_table(result, list_labels)
			print(common.bcolors.ENDC)
		
		elif user_choice == '0':
			break
		
		else:
			terminal_view.print_error_message("There is no such choice.")
