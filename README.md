# erp-mvc-test-master

def get_choice(  options   ):
	
	options = [
		"Store manager",
		"Human resources manager",
		"Inventory manager",
		"Accounting manager",
		"Sales manager",
		"Customer Relationship Management (CRM)"
	]
	
	options <-- jeśli pierwsze jest inne niż 'Store manager' to działa tak że
	        pierwsza pozycja z listy to jest title np 'Add' 'Remowe' 'Edit' a 
	        ostatnia pozycja to komunikat przejścia menu wyżej np 'Exit to main menu'
	
	
	
	
	
	
def get_inputs(   list_labels,    title):

            list_labels = [
				['\tTitle: ', str],
				['\tManufacturer:', str],
				['\tPrice: ', float],
				['\tIn stock: ', int]
			]
			title = 'Add'
			
			list_labels <--- jeśli pierwsza pozycja na pierwszej liście to 'Please enter a number: ': to pobiera tylko 
			    jednego inta, natomiast głąbszą walidację robi w każdym innym przypadku 
			get_inputs([['\tTitle: ', str], ['\tManufacturer:', str], ['\tPrice: ', float], ['\tIn stock: ', int]])
		    get_inputs([["Please enter a number: ", int], ], "")


            możliwe typy danych do sprawdzenia:
            inputs = terminal_view.get_inputs([list_labels, title)
                         ||||| 
                         vvvvv            
            get_inputs(['must'] + list_labels, title) <--- jeśli tak to wprowadzane dane są konieczne i walidacja tak samo           
            
            str             <--- ponad 100 znaków i konvertuje na title
            int             <---    >= 0
            float           <---    >= 0  i zaokrągla do 2 miejsc po przecinku
            id max_index    <---   np    f'id {len(table)}    get_inputs([['Index to remove', f'id {len(table)}'],], title)
            year            <--- od 1900 do 2020 
            month           <--- od 1 do 12
            day             <--- od 1 do 31
            type   in  or   out
            email           <--- złamałem się i wziołem re do tego 
            subscription    <--- 1 albo 0
            name            <--- zawsze znaki bez cyfr  plus musi być odstep   
            
            return <---- zawsze stringi 
            
            
            
            

def print_menu(  title,   list_options,   exit_message  ):

    print_menu("Main menu", options, "Exit program")



