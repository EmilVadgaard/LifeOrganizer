from table_manager import *

running = True
while running:
    print('press 1 to add entry to items')
    print('press 2 to delete entry from items')
    print('press 3 to show table')
    print('press 9 to add entry to items with ID')
    print('press any to quit')
    temp = input()
    if temp == '1':
        name = input('What item are you adding?')
        price = int(input('What does it cost?'))
        insert_items(name,price)
    elif temp == '2':
        name = input('What item do you want to delete?')
        delete_items(name)
    elif temp == '3':
        show_items()
    elif temp == '9':
        id = int(input('What is the ID'))
        name = input('What item are you adding?')
        price = int(input('What does it cost?'))
        insert_items_ID(id,name,price)
    else:
        running = False