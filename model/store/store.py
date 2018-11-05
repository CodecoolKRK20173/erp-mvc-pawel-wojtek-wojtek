""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
from controller.common import bcolors
from model import data_manager
from model import common


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
    data_manager.write_table_to_file("model/store/games.csv", table)
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
    data_manager.write_table_to_file("model/store/games.csv", table)
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
    data_manager.write_table_to_file("model/store/games.csv", table)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    counts_by_manufactures = {}
    index_manufacturer = 2
    for manufacturer in table:
        if manufacturer[index_manufacturer] in counts_by_manufactures:
            counts_by_manufactures[manufacturer[index_manufacturer]] += 1
        else:
            counts_by_manufactures[manufacturer[index_manufacturer]] = 1
    return counts_by_manufactures


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    index_manufacturer = 2
    index_stock = 4
    sum_amount = 0
    number_of_games = 0
    for item in table:
        if item[index_manufacturer] == manufacturer:
            number_of_games += 1
            sum_amount += int(item[index_stock])
    if number_of_games != 0:
        return sum_amount / number_of_games
    else:
        return str(f'{bcolors.WARNING}not find{bcolors.ENDC}')
