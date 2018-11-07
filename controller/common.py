""" Common functions for controllers
implement commonly used functions here
"""
from model.common import check_double_record
from view import terminal_view


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def check_if_empty(list):
	if not list:
		print("There is no such record.")
		return False
	return True


def make_crud(crud_module, list_labels, list_options, max_id, table, user_choice):
	list_labels_buff = []
	test = sum([1 for item in list_labels if item[1] in ['month', 'day', 'year']])
	# for item in list_labels:
	# 	if item[1] in ['month', 'day', 'year']:
	# 		test += 1
	
	if test == 3 and user_choice in ['2', '4']:
		for index, item in enumerate(list_labels):
			if item[1] == 'month':
				list_labels_buff.append(['Date', 'date'])
			elif item[1] in ['year', 'day']:
				continue
			else:
				list_labels_buff.append(item)
		list_labels = list_labels_buff
	if user_choice == '1':
		terminal_view.print_table(table, list_labels)
	elif user_choice == '2':
		add(list_labels, list_options, table, crud_module)
	elif user_choice == '3':
		remove(list_options, max_id, table, crud_module)
	elif user_choice == '4':
		update(list_labels, list_options, max_id, table, crud_module)


def update(list_labels, list_options, max_id, table, crud_module):
	index_list_options = 4
	title_for_id = list_options[index_list_options]
	title_for_edit = list_options[index_list_options] + ' (if you press enter you will not change your data)'
	id_to_edit = terminal_view.get_inputs(['Index to edit', 'id', max_id], title_for_id)
	inputs = terminal_view.get_inputs(list_labels, title_for_edit)
	write_records(crud_module.update, inputs, table, id_to_edit)


def remove(list_options, max_id, table, crud_module):
	index_list_options = 3
	title = list_options[index_list_options]
	id_to_remove = terminal_view.get_inputs(['Index to remove', 'id', max_id], title)
	crud_module.remove(table, id_to_remove)


def add(list_labels, list_options, table, crud_module):
	index_list_options = 2
	title = list_options[index_list_options]
	inputs = terminal_view.get_inputs(['must'] + list_labels, title)
	write_records(crud_module.add, inputs, table)


def write_records(*args):
	index_func = 0
	index_inputs = 1
	index_table = 2
	index_id = 3
	if 'add' in args[0].__name__:
		if check_double_record(args[index_table], args[index_inputs]):
			terminal_view.print_error_message('Record doublet')
		else:
			args[index_func](args[index_table], args[index_inputs])
	elif 'update' in args[0].__name__:
		if check_double_record(args[index_table], args[index_inputs]):
			terminal_view.print_error_message('Record doublet')
		else:
			args[index_func](args[index_table], args[index_id], args[index_inputs])

def index_sorted_list(spending_list, index):
	sorted_by_amount = sorted(spending_list, reverse = True, key = lambda x: x[index])
	return sorted_by_amount
	