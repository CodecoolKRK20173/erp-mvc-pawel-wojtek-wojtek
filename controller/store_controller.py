# everything you'll need is imported:
from controller.common import make_crud
from model import data_manager
from model.store import store
from view import terminal_view


def run():
	"""
	Starts this module and displays its menu.
	* User can access default special features from here.
	* User can go back to main menu from here.
	"""
	
	list_options = [
		'Store',
		'Show all data',
		'Add',
		'Remove',
		'Update',
		'Get counts by manufacturers',
		'Get average by manufacturer',
		'Exit to main menu'
	]
	list_labels = [
		['Title', str],
		['Manufacturer', str],
		['Price', int],
		['In stock', int]
	]
	data_file = "model/store/games.csv"
	crud_module = store
	while True:
		table = data_manager.get_table_from_file(data_file)
		max_id = len(table)
		user_choice = terminal_view.get_choice(list_options)
		if user_choice in ['1', '2', '3', '4']:
			make_crud(crud_module, list_labels, list_options, max_id, table, user_choice)
		elif user_choice == '5':
			terminal_view.print_result(store.get_counts_by_manufacturers(table), 'Counts by manufactures')
		elif user_choice == '6':
			manufacturer = terminal_view.get_inputs([['Manufacturer to get average', str], ], 'Manufacturer')
			terminal_view.print_result(
				store.get_average_by_manufacturer(table, *manufacturer),
				'Average by {}'.format(*manufacturer)
			)
		elif user_choice == '0':
			break
		else:
			terminal_view.print_error_message("There is no such choice.")
