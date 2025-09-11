class BankAcc:
    def __init__(self, balance=0):
        self.__balance = balance  
    def withdraw(self, amnt):
        if amnt <= self.__balance:
            self.__balance -= amnt
            print(f"Withdrawn: {amnt}")
        else:
            print("Insufficient balance")
    def deposit(self, amnt):
        self.__balance += amnt
        print(f"Deposited: {amnt}")
    def get_balance(self):
        return self.__balance
a=BankAcc(2000)
a.deposit(5000)
a.withdraw(2000)
print(f"final balance:{a.get_balance()}")