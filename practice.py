# .py file for practicing/testing code.

def item_add():

    name = input("Item Name: ")
    description = input("Description: ")
    price = input("Price per day: ")

    OUTPUT_FILE = open("items.csv", "a")



    print('{},{},{},in'.format(name, description, price), file=OUTPUT_FILE)

    OUTPUT_FILE.close()
item_add()


"""OUTPUT_FILE.write(name)
    OUTPUT_FILE.write(description)
    OUTPUT_FILE.write(price)
    OUTPUT_FILE.close()

    print(name)


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
"""





