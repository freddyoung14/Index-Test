# .py file used for testing/practicing code



Menu = '\nMENU: \n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit'

print(Menu)
print('\n')


INPUT_FILE = "items.csv"

items = open(INPUT_FILE, "r")

print(items.read())

items.close()






