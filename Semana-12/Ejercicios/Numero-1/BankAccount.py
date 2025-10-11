class BankAccount:
    _balance = 0

    def deposit_money(self, money):
        self._balance += money
        print(f"Su balance es de: {self._balance}")
    
    def withdraw_money(self, money):
        if money <= self._balance:
            self._balance -= money
            print(f"Su balance es de: {self._balance}")
        else:
            print("Saldo insuficiente")
