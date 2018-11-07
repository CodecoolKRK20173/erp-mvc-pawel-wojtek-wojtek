""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common
from model.common import sort_my


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    index_id = 0
    record.insert(index_id, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file("model/crm/customers.csv", table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    
    for i, record in enumerate(table, 1):
        if str(i) == id_:
            del table[i - 1]
    data_manager.write_table_to_file("model/crm/customers.csv", table)
    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """
    
    for i, item in enumerate(table, 1):
        if str(i) == id_:
            index = 1
            for item_from_table, item_from_new_record in zip(table[i - 1][1:], record):  # TODO [1:] pomijam zchaszowany index
                if item_from_new_record != '':
                    table[i - 1][index] = item_from_new_record
                index += 1
    data_manager.write_table_to_file("model/crm/customers.csv", table)
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    index_name = 1
    index_index = 0
    index_first_user = 0
    max_len_name = len(table[index_first_user][index_name])
    for item in table:
        if len(item[index_name]) > max_len_name:
            max_len_name = len(item[index_name])
    list_of_longest_names = []
    for item in table:
        if len(item[index_name]) == max_len_name:
            list_of_longest_names.append(item)
    longest_and_last_name = sort_my([item[index_name] for item in list_of_longest_names])[-1]
    for item in table:
        if item[index_name] == longest_and_last_name:
            return item[index_index]


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    
    index_email = -2
    index_name = 1
    index_subscribed = -1
    list_emails = []
    for item in table:
        if '@' in item[index_email] and int(item[index_subscribed]):
            list_emails.append(';'.join([item[index_email], item[index_name]]))
    return list_emails


# functions supports data analyser
# --------------------------------

def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code
    table = data_manager.get_table_from_file("model/crm/customers.csv")
    id_index = 0
    name_index = 1
    for item in table:
        if id == item[id_index]:
            return item[name_index]
    return None

def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    id_index = 0
    name_index = 1
    for item in table:
        if id == item[id_index]:
            return item[name_index]
    return None

def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    table = data_manager.get_table_from_file("model/crm/customers.csv")
    return set(item[0] for item in table)