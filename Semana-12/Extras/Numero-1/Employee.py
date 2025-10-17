class Employee:
    def __init__(self, name, salary):
        self._name = name
        if salary < 0:
            raise ValueError("El salario debe ser positivo")
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, money):
        if money < 0:
            raise ValueError("El salario debe ser positivo")
        self._salary = money
    
    def promote(self, new_raise):
        self.salary += self.salary * new_raise

try:
    new_employee = Employee("Alejandro", 2500)
    print(new_employee.salary)
    new_employee.promote(0.77)
    print(new_employee.salary)
except ValueError as error:
    print(error)