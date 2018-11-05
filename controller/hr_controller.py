# everything you'll need is imported:
from controller.common import make_crud
from model import data_manager
from model.hr import hr
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
		'Human resources',
		'Show all people',
		'Add',
		'Remove',
		'Update',
		'Get oldest person',
		'Get persons closest to average',
		'Exit to main menu'
	]
	list_labels = [
		['Name', 'name'],
		['Birth year', 'year']
	]
	data_file = "model/hr/persons.csv"
	crud_module = hr
	while True:
		table = data_manager.get_table_from_file(data_file)
		max_id = len(table)
		user_choice = terminal_view.get_choice(list_options)
		if user_choice in ['1', '2', '3', '4']:
			make_crud(crud_module, list_labels, list_options, max_id, table, user_choice)
		elif user_choice == '5':
			terminal_view.print_result(hr.get_oldest_person(table), 'Get oldest person:')
		elif user_choice == '6':
			terminal_view.print_result(hr.get_persons_closest_to_average(table), 'Get persons closest to average:')
		elif user_choice == '0':
			break
		else:
			terminal_view.print_error_message("There is no such choice.")
