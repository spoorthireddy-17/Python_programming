def apply_discount(price, dis_per):
    discount = (dis_per / 100) * price
    after_dis = price - discount
    return after_dis

def add_gst(price, gst_per=18):
    gst = (gst_per / 100) * price
    after_gst = price + gst
    return after_gst

def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print('---- INVOICE ----')
    subtotal = 0
    final_total = 0
    
    for item, price in cart.items():
        print(f"{item}\t: {price:.2f}")
        subtotal += price

    print('-----------------')
    print(f"Subtotal: {subtotal:.2f}")
    final_disc=0
    final_gst=0
    for item, price in cart.items():
        discounted = apply_discount(price, discount_percent)
        with_gst = add_gst(discounted, gst_percent)
        final_disc+=discounted
        final_gst += with_gst
    print(f"After {discount_percent}% discount: {final_disc}")
    print(f"After {gst_percent}% GST: {final_gst}")
    print('-----------------')    
    print("thankyou for shopping with us!")
