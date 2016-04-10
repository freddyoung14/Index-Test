# 2nd .py file for testing
# loading_items() COMPLETE
# add_items() COMPLETE
# list_items() INCOMPLETE [currently working on]
# hire_items() INCOMPLETE [currently working on]


def hire_items():

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")

    item_list = in_file.readlines()

    mydictionary = {'ItemName':0, 'ItemDescription':1, 'ItemCost':2, 'ItemStockValue':3}
    # space = '' <--- variable for 'neat' alignment
    # list.split as alternative

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

    in_file1 = open(INPUT_FILE, "r+")

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

    count = -1

    for i, row in enumerate(item_list, 1):
        if i == item_num:
            break
    print(row)


    print(item_name in row, 'hired for', item_cost)



   # for row in item_list:
      #  for_hire = ','.join(list(row.splitlines()))
      #  print(for_hire)

    in_file1.close()





hire_items()





