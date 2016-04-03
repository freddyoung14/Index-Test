# 2nd .py file for testing
# slicing for optional use?

def add_items():
    OUTPUT_FILE = "items.csv"

    out_file = open(OUTPUT_FILE, "a")
    valid_input = False
    while valid_input:
        try:
            item_add = str(input('Item name: ')).capitalize()
            valid_input = True
        except ValueError:
            print("Invalid Input")
    print(item_add, file=out_file) #UnboundLocalError??????!!!!!!!

    out_file.close()


add_items()