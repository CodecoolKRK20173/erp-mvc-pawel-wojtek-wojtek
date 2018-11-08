# everything you'll need is imported:
import os

from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
<<<<<<< HEAD
from controller import data_analyser_controller


def run():
    os.system('clear')
    options = [
        "Store manager",
        "Human resources manager",
        "Inventory manager",
        "Accounting manager",
        "Sales manager",
        "Customer Relationship Management (CRM)",
        "Data Analyser"

    ]
    choice = None
    while choice != "0":
        os.system('clear')
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "7":
            data_analyser_controller.run()
        elif choice == "0":
            os.system('clear')
        else:
            terminal_view.print_error_message("There is no such choice.")
=======
from controller import data_analyser

def run():
	os.system('clear')
	options = [
		"Store manager",
		"Human resources manager",
		"Inventory manager",
		"Accounting manager",
		"Sales manager",
		"Customer Relationship Management (CRM)",
		"Data analyser"
	]
	choice = None
	while choice != "0":
		os.system('clear')
		choice = terminal_view.get_choice(options)
		if choice == "1":
			store_controller.run()
		elif choice == "2":
			hr_controller.run()
		elif choice == "3":
			inventory_controller.run()
		elif choice == "4":
			accounting_controller.run()
		elif choice == "5":
			sales_controller.run()
		elif choice == "6":
			crm_controller.run()
		elif choice == "7":
			data_analyser.run()
		elif choice == "0":
			os.system('clear')
		else:
			terminal_view.print_error_message("There is no such choice.")
>>>>>>> wojtekg
