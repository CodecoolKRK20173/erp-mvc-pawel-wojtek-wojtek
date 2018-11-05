""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
from model import data_manager
from model import common
from model.common import convert_possible_item_in_list_into_int


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
    data_manager.write_table_to_file("model/inventory/inventory.csv", table)
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
    data_manager.write_table_to_file("model/inventory/inventory.csv", table)
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
    data_manager.write_table_to_file("model/inventory/inventory.csv", table)
    return table
    

# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    index_year = -2
    index_durability = - 1
    available_items = []
    for item in table:
        item[index_year] = int(item[index_year])
        item[index_durability] = int(item[index_durability])

        if (item[index_year] + item[index_durability]) >= 2017:  
            available_items.append(item)
    return available_items
    

def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    
    index_manufacturer = -3
    index_durability = -1
    list_of_manufacturer = set([item[index_manufacturer] for item in table])
    average_durability_by_manufacturers = {item: 0 for item in list_of_manufacturer}
    for item in table:
        average_durability_by_manufacturers[item[index_manufacturer]] += int(item[index_durability])
    for item in average_durability_by_manufacturers.keys():
        occur = 0
        for item_2 in table:
            if item_2[index_manufacturer] == item:
                occur += 1
        average_durability_by_manufacturers[item] /= occur
    return average_durability_by_manufacturers

