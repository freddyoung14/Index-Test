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




def add_items():
    OUTPUT_FILE = "items.csv"

    out_file = open(OUTPUT_FILE, "a")

    row = []

    item_add = (input('Item name: ')).capitalize()
    item_description = (input('Description: ')).capitalize()

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


    row.append(item_add)
    row.append(item_description)

    print(','.join(row), file=out_file, end=',')

    # printing item_cost separate because .join() method doesn't process integers/floats
    row.append(item_cost)

    print(item_cost, file=out_file, end=',')
    print('in', file=out_file)

    print('{} ({}), ${:.2f} now available for hire'.format(item_add, item_description, item_cost))


    out_file.close()


main()




































