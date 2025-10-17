class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit_money(self, money):
        if not isinstance(money, (int, float)):
            raise ValueError("Error, el valor debe ser un número")
        elif money < 0:
            raise ValueError("Error, el monto no puede ser negativo")
        self._balance += money
        print(f"Su balance es de: {self._balance}")
    
    def withdraw_money(self, money):
        if money > self._balance:
            raise ValueError("Saldo insuficiente")
        self._balance -= money
        print(f"Su balance es de: {self._balance}")
