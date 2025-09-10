import ecommerce_utils
mydict={}
n=int(input('enter number of items in shopping cart:'))
for i in range(n):
    key=input('enter product name:')
    value=int(input('enter price:'))
    mydict[key]=value
    
discount = int(input("Enter discount percentage: "))
gst = int(input("Enter GST percentage: "))

ecommerce_utils.generate_invoice(mydict, discount_percent=discount, gst_percent=gst)