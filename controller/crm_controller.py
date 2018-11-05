# everything you'll need is imported:
from controller.common import make_crud
from model import data_manager
from model.crm import crm
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
			'Customer Relations Management',
			'Show all customers',
			'Add',
			'Remove',
			'Update',
			'Get ID of the customer with the longest name',
			'Get customers subscribed to newsletter',
			'Exit to main menu'
		]
	data_file = "model/crm/customers.csv"
	crud_module = crm
	while True:
		table = data_manager.get_table_from_file(data_file)
		max_id = len(table)
		list_labels = [
			['Name', 'name'],
			['Email', 'email'],
			['Subscription', 'subscription']
		]
		user_choice = terminal_view.get_choice(list_options)
		if user_choice in ['1', '2', '3', '4']:
			make_crud(crud_module, list_labels, list_options, max_id, table, user_choice)
		elif user_choice == '5':
			result = crm.get_longest_name_id(table)
			terminal_view.print_result(result, "ID of the customer with the longest name")
		elif user_choice == '6':
			result = crm.get_subscribed_emails(table)
			terminal_view.print_result(result, "Customers subscribed to the newsletter")
		elif user_choice == '0':
			break
		else:
			terminal_view.print_error_message("There is no such choice.")
