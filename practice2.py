# 2nd .py file for testing
# loading_items() COMPLETE
# add_items() COMPLETE
# list_items() INCOMPLETE [currently working on]
# hire_items() INCOMPLETE [currently working on]


def list_items():
    print('All items on file (* indicates item is currently out):')

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()

    mydictionary = {'ColumnName1':0, 'ColumnName2':1, 'ColumnName3':2, 'ColumnName4':3}

    count = -1

    for row in item_list:
        row = row.rstrip()
        mydictionary = row.split(',')
        count += 1

        print('{} - {} ({}) = ${:.2f}'.format(count, mydictionary[0], mydictionary[1], (float(mydictionary[2]))).strip())



    # print(''.join(item_list))





    in_file.close()
list_items()