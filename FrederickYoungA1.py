"""	CP1404 Assignment 1 - 2016
	Items for Hire
	Frederick Michael Young
	29/03/2016


	GITHUB LINK - ....................




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
            hire_items()
        elif choice == 'R':
            return_item()
        elif choice == 'A':
            add_items()
        else:
            print('Invalid menu choice')
        print(Menu)
        choice = input('>>> ').upper()

    saving_items()
    print('Have a nice day :)')



"""
Pseudocode for loading items
.....................................

function loading_items()
    INPUT_FILE = "items.csv

    open "items.csv as in_file for reading
    readlines in in_file as item_list
    num_items = 0

    for row in item_list:
        words_list = row split string
        num_items = num_items + 1
    display num_items & message to user
    close in_file
"""
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


def saving_items():
    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()

    num_items = 0

    for row in item_list:
        words_list = row.split()
        num_items += 1
    print(num_items, 'items saved to items.csv')

    in_file.close()


def list_items():
    print('All items on file (* indicates item is currently out):')

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()

    mydictionary = {'ItemName':0, 'ItemDescription':1, 'ItemCost':2, 'ItemStockValue':3}
    # space = '' <--- variable for 'neat' alignment

    items = list(mydictionary)
    count = 0

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

"""
Pseudocode for hiring an item
.....................................

function loading_items()
    INPUT_FILE = "items.csv

    open "items.csv" as in_file for reading
    readlines in in_file as item_list

    mydictionary = empty map
    count = 0

    no_items = no items message

    for line in item_list
        row = row strip whitespace
        mydictionary = row split string
        set item: name, description, cost & stock value to mydictionary index'
        replace 'out' with * & replace 'in' with empty string
        count = count + 1

    if row ends with 'in'
        display mydictionary
    else if row doesn't end with 'in' and ends with 'out'
        display no items message
    close in_file

    OUTPUT_FILE = 'items.csv'

    open "items.csv" as out_file for editing and reading
    readlings in out_file as items_list_out

    display enter number of an item message

    valid_input = False
    repeat while not valid_input
        try
            get item_num
            if item_num < 0
                display invalid number
            else
                valid_input = True
        except ValueError
            display invalid input message

    for i, row in enumerate (item_list_out, 1)
        if i == item_num
            stop loop(break)

    hired_item = row.replace string, 'in' with 'out'

    initially seek 0 at out_file
    for line in item_list_out:
        if 1 != i:
            write (i) to out_file
    write (hired_item) to out_file

    hired_item = list(hired_item) split string

    display item name, hire message and item cost

    close out_file
"""
def hire_items():

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")

    item_list = in_file.readlines()

    mydictionary = {'ItemName':0, 'ItemDescription':1, 'ItemCost':2, 'ItemStockValue':3}

    count = 0

    no_items = 'No items are currently on hire'

    for row in item_list:

            row = row.rstrip()
            mydictionary = row.split(',')
            item_name = mydictionary[0]
            item_description = mydictionary[1]
            item_cost = float(mydictionary[2])
            item_stock_value = mydictionary[3].replace('out', ' *').replace('in', ' ')
            count += 1

            if row.endswith('in'):

                print('{} - {} ({}) = ${:.2f}{}'.format(count, item_name, item_description, item_cost,
                                                         item_stock_value))

            elif 'in' not in row and 'out' not in row:
                print(no_items)
    in_file.close()

    OUTPUT_FILE = 'items.csv'
    out_file = open(OUTPUT_FILE, "r+")

    item_list_out = out_file.readlines()

    print('Enter the number of an item to hire')


    valid_input = False
    while not valid_input:
        try:
            item_num = int(input('>>> '))
            if item_num < 0:
                print('Invalid number')
            else:
                valid_input = True
        except ValueError:
            print("Invalid Input/ enter a  number")


    for i, row in enumerate (item_list_out, 1):
        if i == item_num:
            break

    hired_item = (row.replace('in', 'out'))

    out_file.seek(0)
    for line in item_list_out:
        if 1 != i:
            out_file.write(i)
    out_file.write(hired_item)

    hired_item = list(hired_item.split())

    print(hired_item[0] in row, 'hired for', hired_item[5])

    out_file.close()

def return_item():
    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")

    item_list = in_file.readlines()

    mydictionary = {'ItemName':0, 'ItemDescription':1, 'ItemCost':2, 'ItemStockValue':3}


    count = 0

    no_items = 'No items are currently on hire'

    for row in item_list:
        row = row.rstrip()
        mydictionary = row.split(',')
        item_name = mydictionary[0]
        item_description = mydictionary[1]
        item_cost = float(mydictionary[2])
        item_stock_value = mydictionary[3].replace('out', ' *').replace('in', ' ')
        count += 1

        if row.endswith('out'):

            print('{} - {} ({}) = ${:.2f}{}'.format(count, item_name, item_description, item_cost,
                                                         item_stock_value))

        elif 'in' not in row and 'out' not in row:
            print(no_items)
    in_file.close()

    OUTPUT_FILE = 'items.csv'
    out_file = open(OUTPUT_FILE, "r+")

    item_list_out = out_file.readlines()

    print('Enter the number of an item to hire')


    valid_input = False
    while not valid_input:
        try:
            item_num = int(input('>>> '))
            if item_num < 0:
                print('Invalid number')
            else:
                valid_input = True
        except ValueError:
            print("Invalid Input/ enter a  number")


    for i, row in enumerate (item_list_out, 1):
        if i == item_num:
            break

    return_item = (row.replace('out', 'in'))

    out_file.seek(0)
    for line in item_list_out:
        if 1 != i:
            out_file.write(i)
    out_file.write(return_item)

    hired_item = list(return_item.split())

    print(hired_item[0] in row, 'hired for', hired_item[5])

    out_file.close()



main()





































