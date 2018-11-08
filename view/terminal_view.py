""" Terminal view module """
import inspect
import re
import os
#from controller.common import bcolors


def print_table(table, title_list):

    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
        """
    os.system('clear')
    item_index = 0
    title_index = 0
    titles = []
    for title in title_list:
        titles.append(title[title_index])
    titles.insert(0, "Index")
    titles.insert(1, "ID")
    for i, item in enumerate(table, 1):
        item.insert(item_index, i)
    col_width = []
    for title in titles:
        col_width.append(len(title))
    for items in table:
        for i, item in enumerate(items):
            if col_width[i] < len(str(item)):
                col_width[i] = len(str(item))
    table_width = 0
    
    for width in col_width:
        table_width += width + 3
    print("-" * table_width)
    table.insert(item_index, titles)

    for items in table:
        print("|", end="")
        for i, item in enumerate(items):
            print(' {:^{width}} |'.format(item, width=col_width[i]), end="")
        print()
        print("-" * table_width)

        
def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    os.system('clear')
    print(bcolors.WARNING + bcolors.BOLD)
    if type(result) == dict:
        print(label + ' : ')
        max_len = 0
        for key, value in result.items():
            max_len = len(key) if len(key) > max_len else max_len
        for key, value in result.items():
            print(' ' * 2 + key + '-' * (max_len - len(key) + 1) + '> '  + str(value))
    elif 'hr_controller.py' in inspect.stack()[1][1]:
        print(label, ' and '.join(result))
    elif type(result) == list:
        result_key = []
        result_value = []
        index_key = 0
        index_value = 1
        for item in result:
            result_key.append(item.split(';')[index_key])
            result_value.append(item.split(';')[index_value])
        result = dict(zip(result_key, result_value))
        print(label + ' : ')
        max_len = 0
        for key, value in result.items():
            max_len = len(key) if len(key) > max_len else max_len
        for key, value in result.items():
            print(' ' * 2 + key + '-' * (max_len - len(key)) + '> ' + str(value))
    elif type(result) == tuple: # wykorzystywane tylko dla jednej funkcji jak jest tupla
        print("{}: {}, {}".format(label, result[0], result[1]))
    else:
        print(label + ': ' + str(result))
    print(bcolors.ENDC)


def print_list_result(result, label):
    os.system('clear')
    print(bcolors.WARNING + bcolors.BOLD)
    print(label)
    for item in result:
        print(item)
    print(bcolors.ENDC)

    
def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    print(title)
    for index, item in enumerate(list_options, 1):
        print(' ' * 4 + f'({index}) ' + item)
    print(' ' * 4 + '(0) ' + exit_message)

  
def get_choice(options):
    if options[0] == 'Store manager':
        print_menu("Main menu", options, "Exit program")
        inputs = get_inputs([["Please enter a number: ", int], ], "")
        return str(inputs)
    elif len(options) >= 3:
        index_title = 0
        index_exit = -1
        print_menu(options[index_title], options[1:-1], options[index_exit])  # TODO zapis 1:-1 wydaje sie czytelniejszy
        inputs = get_inputs([["Please enter a number: ", int], ], "")
        return str(inputs)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    print(title)
    inputs = []
    index_first_label = 0
    index_title_of_label = 0
    index_type_of_input = 1
    index_error_message = 2
    max_length_of_string = 100
    if list_labels[index_first_label][index_title_of_label] == 'Please enter a number: ':
        while True:
            try:
                inputs.append(int(input('Please enter a number: ')))
                return inputs[0]
            except ValueError:
                print_error_message("There is no such choice.")
    elif len(list_labels) >= 2 and list_labels[index_type_of_input] == 'id':
        max_id = (list_labels[index_error_message])
        while True:
            try:
                user_input_variable = int(input(f'\t{list_labels[index_title_of_label]}: '))
                if user_input_variable > max_id or user_input_variable < 1:
                    raise NameError(f'{list_labels[index_title_of_label]} must be between 1 and {max_id}')
                return str(user_input_variable)
            except NameError as message:
                print_error_message(message)
            except ValueError:
                print_error_message(f'{list_labels[index_title_of_label]} must be the number of index')
    else:
        inputs = []
        must = True if list_labels[0] == 'must' else False
        for label in list_labels:
            if label == 'must':
                continue
            while True:
                try:
                    if label[index_type_of_input] == str:
                        validate_string(index_title_of_label, inputs, label, must, max_length_of_string)
                    elif label[index_type_of_input] == int:
                        validate_integer(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == float:
                        validate_float(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'year':
                        validate_year(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'month':
                        validate_month(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'day':
                        validate_day(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'type':
                        validate_type(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'email':
                        validate_email(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'subscription':
                        validate_subscription(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'durability':
                        validate_durability(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'name':
                        validate_name(index_title_of_label, inputs, label, must)
                    elif label[index_type_of_input] == 'date':
                        validate_date(index_title_of_label, inputs, label, must)
                    else:
                        print('')
                    break
                except NameError as message:
                    print_error_message(str(message))
                except ValueError as message:
                    if str(message)[-2:] == "''":
                        print_error_message('You must select a record ')
                    else:
                        print_error_message('You must enter an integer ')
                except ErrorAdd as message:
                    message = str(message)
                    print_error_message(message + ' when add data must be')
        clear_inputs = []
        for item in inputs:
            if item.isprintable():
                clear_inputs.append(item.strip())
            else:
                clear_inputs.append(item)
        return clear_inputs


def validate_name(index_title_of_label, inputs, label, must):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable.title())
    else:
        test = 0
        user_input_variable = user_input_variable.strip()
        for item in user_input_variable:
            if item == ' ':
                test += 1
            if item.isdigit():
                raise NameError(f'{label[index_title_of_label]} must be surname')
        if test == 1:
            inputs.append(user_input_variable.title())
        else:
            raise NameError(f'{label[index_title_of_label]} must be surname')


def validate_durability(index_title_of_label, inputs, label, must):
    min_dur = 1
    max_dur = 50
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif (int(user_input_variable) < min_dur or int(user_input_variable) > max_dur):
        raise NameError(f'{label[index_title_of_label]} '
                        f'should be a number, between {min_dur} and {max_dur}.')
    inputs.append(user_input_variable)


def validate_subscription(index_title_of_label, inputs, label, must):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif user_input_variable != '0' and user_input_variable != '1':
        raise NameError(f'{label[index_title_of_label]} must be 1 for Yes or 0 for No')
    inputs.append(user_input_variable)


def validate_email(index_title_of_label, inputs, label, must):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", user_input_variable):
        raise NameError(f'{label[index_title_of_label]} must be email')
    inputs.append(user_input_variable)


def validate_type(index_title_of_label, inputs, label, must):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif (user_input_variable != 'in' and user_input_variable != 'out'):
        raise NameError(f'{label[index_title_of_label]} should be a \'in\' or \'out\'.')
    inputs.append(user_input_variable)


def validate_day(index_title_of_label, inputs, label, must):
    min_day = 1
    max_day = 31
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif (int(user_input_variable) < min_day or int(user_input_variable) > max_day):
        raise NameError(f'{label[index_title_of_label]} '
                        f'should be a number, between {min_day} and {max_day}.')
    inputs.append(user_input_variable)


def validate_month(index_title_of_label, inputs, label, must):
    min_month = 1
    max_month = 12
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif (int(user_input_variable) < min_month or int(user_input_variable) > max_month):
        raise NameError(f'{label[index_title_of_label]} '
                        f'should be a number, between {min_month} and {max_month}.')
    inputs.append(user_input_variable)


def validate_year(index_title_of_label, inputs, label, must):
    min_year = 1900
    max_year = 2020
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif (int(user_input_variable) < min_year or int(user_input_variable) > max_year):
        raise NameError(f'{label[index_title_of_label]} '
                        f'should be a number, between {min_year} and {max_year}.')
    inputs.append(user_input_variable)


def validate_float(index_title_of_label, inputs, label, must):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif len(user_input_variable) > 0:
        user_input_variable = float(user_input_variable)
        if user_input_variable < 0:
            raise NameError(f'{label[index_title_of_label]} must be positive or equal zero ')
        inputs.append(f'{user_input_variable:.2f}')


def validate_integer(index_title_of_label, inputs, label, must):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if must and user_input_variable == '':
        raise ErrorAdd(label[index_title_of_label])
    elif not must and user_input_variable == '':
        inputs.append(user_input_variable)
        return None
    elif len(user_input_variable) > 0:
        user_input_variable = int(user_input_variable)
        if user_input_variable < 0:
            raise NameError(f'{label[index_title_of_label]} must be positive or equal zero ')
        inputs.append(str(user_input_variable))


def validate_string(index_title_of_label, inputs, label, must, max_length_of_string):
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if len(user_input_variable) > 100:
        raise NameError(f'{label[index_title_of_label]} over {max_length_of_string} chars')
    if len(user_input_variable) == 0 and must:
        raise ErrorAdd(label[index_title_of_label])
    inputs.append(user_input_variable.title())


def validate_date(index_title_of_label, inputs, label, must):
    from datetime import datetime
    user_input_variable = input(f'\t{label[index_title_of_label]}: ')
    if not must and user_input_variable == '':
        inputs += ['', '', '']
        return None
    try:
        inputs += (str(datetime.strptime(user_input_variable, '%m-%d-%Y').date().strftime('%m-%d-%Y')).split('-'))
    except ValueError:
        raise NameError('Incorrect data format, should be MM-DD-YYYY')
    

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed


    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'{bcolors.FAIL}Error: {message}{bcolors.ENDC}')
    
    
class ErrorAdd(Exception):
    pass

