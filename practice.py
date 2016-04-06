# .py file for practicing/testing code.


"""
def list_items():
    print('All items on file (* indicates item is currently out):')

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()



    table = [item_list]

    count = -1

    for row in item_list:
        row = row.rstrip()
        table = row.split(',')
        count += 1

        print('{0} - {1} ({2}) = ${3:.2f}'.format(count, table[0], table[1], (float(table[2]))))

    in_file.close()

list_items()
"""

def list_items():
    print('All items on file (* indicates item is currently out):')

    INPUT_FILE = "items.csv"

    in_file = open(INPUT_FILE, "r")
    item_list = in_file.readlines()

    mydictionary = {'ColumnName1':0, 'ColumnName2':1, 'ColumnName3':2, 'ColumnName4':3}
    # space = ''.center(4).ljust(20).rjust(6) --------- testing alignment

    count = -1

    for row in item_list:
        row = row.rstrip()
        mydictionary = row.split(',')
        count += 1

        print('{0} - {1} ({2}) = ${3:.2f}'.format(count, mydictionary[0], mydictionary[1], (float(mydictionary[2]))), (mydictionary[3].replace('out', '*').replace('in', '')).strip())



    in_file.close()
list_items()





