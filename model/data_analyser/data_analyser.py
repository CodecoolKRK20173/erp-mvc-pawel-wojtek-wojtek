"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
from view import terminal_view
from model import common
from model import sales
from model import crm
from model.sales import sales
from model.crm import crm
from controller.common import index_sorted_list


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    return crm.get_name_by_id(get_the_last_buyer_id())


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    return sales.get_customer_id_by_sale_id(sales.get_item_id_sold_last())

def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    name_index = 0
    sum_index = 1
    customer = get_the_buyer_id_spent_most_and_the_money_spent()
    customer_name = crm.get_name_by_id(customer[name_index])
    return (customer_name, customer[sum_index])



def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    customers_sales_ids = sales.get_all_sales_ids_for_customer_ids()
    customers_spending = []
    sum_index = 1
    for customer, sales_ids in customers_sales_ids.items():
        sales_ids = sales.get_the_sum_of_prices(sales_ids)
        customers_spending.append((customer, sales_ids))
    customers_spending_sorted = index_sorted_list(customers_spending, sum_index)  
    return customers_spending_sorted[0]


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    number_of_items_bought = get_the_most_frequent_buyers_ids(num)
    names_of_the_most_frequent_buyers = []
    customer_id_index = 0
    for customer in number_of_items_bought:
        customer = list(customer)
        customer[customer_id_index] = crm.get_name_by_id(customer[customer_id_index])
        names_of_the_most_frequent_buyers.append(tuple(customer))
    return names_of_the_most_frequent_buyers



def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    number_of_items_bought = sales.get_num_of_sales_per_customer_ids()
    most_frequent_buyers = []
    sales_index = 1
    for key, value in number_of_items_bought.items():
        most_frequent_buyers.append((key, value))
    most_frequent_buyers_sorted = index_sorted_list(most_frequent_buyers, sales_index)
    if len(most_frequent_buyers_sorted) > num:
        return most_frequent_buyers_sorted[:num]
    return most_frequent_buyers_sorted

def get_customers_who_did_not_buy_anything():
    customers_who_bought_something = sales.get_all_customer_ids()
    all_customers = crm.get_all_customer_ids()
    customers_who_didnt_buy = []
    for customer in all_customers:
        if customer not in customers_who_bought_something:
            customers_who_didnt_buy.append(crm.get_name_by_id(customer))
    return customers_who_didnt_buy
