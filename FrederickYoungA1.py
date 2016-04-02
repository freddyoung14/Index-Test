"""	CP1404 Assignment 1 - 2016
	Items for Hire
	Frederick Michael Young
	29/03/2016

Pseudocode:

...
...
...

function main()
	display welcome message
	display menu
	get user choice

	while choice is not 'Q'
	    if choice is 'L'
	        display all items

	...
	... <-- [finish after all other functions are complete.]

function loading_items()
    import csv







function hiring_item():





"""




Menu = 'MENU: \n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit'

def main():
    print('\n\nItems for Hire - by Frederick Michael Young')

    loading_items()
    print(Menu)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            listing_items()






def loading_items():
    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()

    num_items = 0

    for row in item_list:
        words_list = row.split()
        num_items += 1
    print(num_items, 'items loaded from items.csv')

    in_file.close()






main()




































