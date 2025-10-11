from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.__min_balance = min_balance
        self.deposit_money(min_balance)
    

    def withdraw_money(self, money):
        if money <= (self._balance - self.__min_balance):
            self._balance -= money
            print(f"Su balance es de: {self._balance}")
        else:
            print(f"Saldo insuficiente. El retiro no puede dejar su cuenta por debajo de su saldo minimo de: {self.__min_balance}")
            print(f"Dinero disponible para retirar: {self._balance - self.__min_balance}")


my_savings = SavingsAccount(500)
my_savings.deposit_money(300)
my_savings.withdraw_money(100)
my_savings.withdraw_money(400)
