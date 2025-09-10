mydict = {}

def add():
    key = int(input('Enter book id: '))
    value = input('Enter book title: ')
    mydict[key] = value
    print(mydict)

def remove(rem):
    if rem in mydict:
        mydict.pop(rem)
        print("Book removed:", mydict)
    else:
        print("Book ID not found")

def search(sea):
    if sea in mydict:
        print(f"Book ID {sea} is present: {mydict[sea]}")
    else:
        print(f"Book ID {sea} is not present")

def update(upd):
    if upd in mydict:
        value = input('Enter new title: ')
        mydict[upd] = value
        print("Updated library:", mydict)
    else:
        print(f"Book ID {upd} not found")

def display():
    print("Library:", mydict)

def count():
    count=0
    for items in mydict:
        count+=1
    print(f"{count} books are present in library")

def check(title):
    found = False
    for k, v in mydict.items():
        if v == title:
            print(f"Book '{title}' found with ID {k}")
            found = True
            break
    if not found:
        print(f"Book '{title}' not found")

while True:
    print("\nLibrary Management Menu")
    print('1. Add book')
    print('2. Remove book')
    print('3. Search book by ID')
    print('4. Update title')
    print('5. Display')
    print('6. Count books')
    print('7. Check by title')
    print('8. Exit')
    
    ch = int(input('Enter your choice: '))
    
    if ch == 1:
        add()
    elif ch == 2:
        rem = int(input('Enter book ID to remove: '))
        remove(rem)
    elif ch == 3:
        sea = int(input('Enter book ID to search: '))
        search(sea)
    elif ch == 4:
        upd = int(input('Enter book ID to update the title: '))
        update(upd)
    elif ch == 5:
        display()
    elif ch == 6:
        count()
    elif ch == 7:
        che = input('Enter book title to search: ')
        check(che)
    elif ch == 8:
        print('Exiting library system...')
        break
    else:
        print('Invalid choice')
