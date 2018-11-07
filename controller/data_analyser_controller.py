
from model import data_manager
from model.data_analyser import data_analyser
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
        'Data Analyser',
        'Get the last buyer\'s name',
        'Get the last buyer\'s id',
        'Get the buyer\'s name who spent most an the money spent he spent',
        'Get the buyer id spent most and the money spent',
        'Get the most frequent buyers names',
        'Get the most frequent buyers ids',
        'Exit to main menu'

    ]
    list_labels = [
        ['Number', int],
        
    ]

    while True:
        user_choice = terminal_view.get_choice(list_options)
        if user_choice == '1':
            terminal_view.print_result(data_analyser.get_the_last_buyer_name(), 'Last buyer\'s name')
        elif user_choice == '2':
            terminal_view.print_result(data_analyser.get_the_last_buyer_id(), 'Last buyer\'s id')
        elif user_choice == '3':
            terminal_view.print_result(data_analyser.get_the_buyer_name_spent_most_and_the_money_spent(), 'Person who spent most money and amount of this money')
        elif user_choice == '4':
            terminal_view.print_result(data_analyser.get_the_buyer_id_spent_most_and_the_money_spent(), 'Person\'s id who spent most money and amount of this money')
        elif user_choice == '5':
            buyers = terminal_view.get_inputs([['Number of buyers', int], ], 'Number')
            terminal_view.print_result(dict(data_analyser.get_the_most_frequent_buyers_names()), 'Names of most frequent buyers')
        elif user_choice == '0':
            break
        else:
            terminal_view.print_error_message("There is no such choice.")



