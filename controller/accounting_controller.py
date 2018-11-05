# everything you'll need is imported:
from controller.common import make_crud
from model import data_manager
from model.accounting import accounting
from view import terminal_view


def run():
	"""
	Starts this module and displays its menu.
	* User can access default special features from here.
	* User can go back to main menu from here.

	Returns:
		None
	"""
	
	list_options = [
		'Accounting',
		'Show all data',
		'Add',
		'Remove',
		'Update',
		'Year with the highest profit',
		'Average amount',
		'Exit to main menu'
	]
	list_labels = [
		['Month', 'month'],
		['Day', 'day'],
		['Year', 'year'],
		['Type', 'type'],
		['Amount', int]
	]
	data_file = "model/accounting/items.csv"
	crud_module = accounting
	while True:
		table = data_manager.get_table_from_file(data_file)
		max_id = len(table)
		user_choice = terminal_view.get_choice(list_options)
		if user_choice in ['1', '2', '3', '4']:
			make_crud(crud_module, list_labels[:], list_options, max_id, table, user_choice)
		elif user_choice == '5':
			terminal_view.print_result(accounting.which_year_max(table), 'Year with the highest income')
		elif user_choice == '6':
			year = terminal_view.get_inputs(['must'] + [['Year to get average', 'year'], ], '')
			terminal_view.print_result(accounting.avg_amount(table, year[0]), 'Average')
		elif user_choice == '0':
			break
		else:
			terminal_view.print_error_message("There is no such choice.")
