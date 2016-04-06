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
    # space = '' ---- couldn't figure out how to align cost in neat column...

    count = -1

    for row in item_list:
        row = row.rstrip()
        mydictionary = row.split(',')
        count += 1

        print('{0} - {1} ({2}) = ${3:.2f}'.format(count, mydictionary[0], mydictionary[1],
                                                 (float(mydictionary[2]))),(mydictionary[3].replace('out', '*').replace('in', '')).strip())



    in_file.close()





    in_file.close()
list_items()