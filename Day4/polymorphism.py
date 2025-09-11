class Payment():
    def pay(self,amount):
        print(f"paid {amount}")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"paid {amount} by cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"paid {amount} by credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"paid {amount} by UPI")
        
payments=[CardPayment(),CashPayment(),UPIPayment()]
amnt=int(input('enter amount:'))
for p in payments:
    p.pay(amnt)