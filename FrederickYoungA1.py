"""	CP1404 Assignment 1 - 2016
	Items for Hire
	Frederick Michael Young
	29/03/2016


	GITHUB LINK - ....................

Pseudocode: (ONLY FOR loading_items & hiring_items) !!


"""




Menu = 'MENU: \n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit'

def main():
    print('\n\nItems for Hire - by Frederick Michael Young')

    loading_items()
    print(Menu)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            list_items()
        elif choice == 'H':
            hire_item()
        elif choice == 'R':
            return_item()
        elif choice == 'A':
            add_items()
        else:
            print('Invalid menu choice')
        print(Menu)
        choice = input('>>> ').upper()

    print('Have a nice day :)')






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


def list_items():
    print('All items on file (* indicates item is currently out):')

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()

    mydictionary = {'ItemName':0, 'ItemDescription':1, 'ItemCost':2, 'ItemStockValue':3}
    # space = '' <--- variable for 'neat' alignment

    items = list(mydictionary)
    count = -1

    for row in item_list:
        row = row.rstrip()
        mydictionary = row.split(',')
        item_name = mydictionary[0]
        item_description = mydictionary[1]
        item_cost = float(mydictionary[2])
        item_stock_value = mydictionary[3].replace('out', ' *').replace('in', ' ')
        count += 1

        print('{} - {} ({}) = ${:.2f}{}'.format(count, item_name, item_description, item_cost,
                                                     item_stock_value))



    in_file.close()



def add_items():
    item_name = input("Item Name: ").capitalize()
    item_description = input("Description: ").capitalize()

    valid_input = False
    while not valid_input:
        try:
            item_cost = float(input('Price per day: $'))
            if item_cost < 0:
                print('Price must be >= $0')
            else:
                valid_input = True
        except ValueError:
            print("Invalid Input/ enter a valid number")


    OUTPUT_FILE = open("items.csv", "a")

    print('{0},{1},{2},in'.format(item_name, item_description, item_cost),file=OUTPUT_FILE)
    print('{0} ({1}), ${2:.2f} now available for hire'.format(item_name, item_description, item_cost))

    OUTPUT_FILE.close()



main()





































