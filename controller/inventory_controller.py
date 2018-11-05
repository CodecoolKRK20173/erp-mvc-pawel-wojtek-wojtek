# everything you'll need is imported:
from view import terminal_view
from model import data_manager
from model.inventory import inventory
from controller.common import bcolors, make_crud


def run():
	"""
	Starts this module and displays its menu.
	* User can access default special features from here.
	* User can go back to main menu from here.

	Returns:
		None
	"""

	list_options = [
		'Inventory',
		'Show all data',
		'Add',
		'Remove',
		'Update',
		'Get available items',
		'Get average durability by manufacturers',
		'Exit to main menu'
	]
	list_labels = [
		['Name of console', str],
		['Manufacturer', str],
		['Purchase year', "year"],
		['Durability', "durability"]
	]
	data_file = "model/inventory/inventory.csv"
	crud_module = inventory
	while True:
		table = data_manager.get_table_from_file(data_file)
		max_id = len(table)
		user_choice = terminal_view.get_choice(list_options)
		if user_choice in ['1', '2', '3', '4']:
			make_crud(crud_module, list_labels, list_options, max_id, table, user_choice)
		elif user_choice == '5':
			print(bcolors.WARNING + bcolors.BOLD)
			terminal_view.print_table(inventory.get_available_items(table), list_labels)
			print(bcolors.ENDC)
		elif user_choice == '6':
			terminal_view.print_result(
				inventory.get_average_durability_by_manufacturers(table),
				'Average durability by manufactures'
			)
		elif user_choice == '0':
			break
		else:
			terminal_view.print_error_message("There is no such choice.")
