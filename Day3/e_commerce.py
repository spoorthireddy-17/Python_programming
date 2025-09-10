
def add(prod): 
    cart.append(prod)
    print(f"{prod} added to cart")
def remove(rem):
    if rem in cart:
        cart.remove(rem)
    print(f"{rem} removed")
def search(check):
    if check in cart:
        print(f"{check} is available in cart")
def display():
    print(cart)
def count():
    count=0
    for items in cart:
        count+=1
    print(f"{count} products in cart")
def sorting():
    cart.sort()
    print(cart)
def clear():
    cart.clear()
cart=[]
while(True):
    print("e-commerce menu")
    print('1.add product')
    print('2.remove product')
    print('3.search product')
    print('4.display')
    print('5.count products')
    print('6.sort products')
    print('7.clear cart')
    print('8.Exit')
    ch=int(input('enter your choice:'))
    if(ch==1):
        prod=input('enter product to add:')
        add(prod)
    elif ch==2:
        rem=input('enter product to remove:')
        remove(rem)
    elif ch==3:
        check=input('enter product to search:')
        search(check)
    elif ch==4:
        display()
    elif ch==5:
        count()
    elif ch==6:
        sorting()
    elif ch==7:
        clear()
    elif ch==8:
        print('leaving cart')
        break
    else:
        print('invalid choice')