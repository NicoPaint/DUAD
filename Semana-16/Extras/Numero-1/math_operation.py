class MathOperations:

    def __init__(self, Number1 = 0, Number2 = 0):
        self._Number1 = Number1
        self._Number2 = Number2
    
    @property
    def Number1(self):
        return self._Number1
    
    @Number1.setter
    def Number1(self, newNumber):
        self._Number1 = newNumber
    
    @property
    def Number2(self):
        return self._Number2
    
    @Number2.setter
    def Number2(self, newNumber):
        self._Number2 = newNumber

    def sum(self):
        return self.Number1 + self.Number2
    
    def multiply(self):
        return self.Number1 * self.Number2
    
    def division(self):
        if self.Number2 == 0:
            raise ZeroDivisionError("The divisor is zero")
        return self.Number1 / self.Number2