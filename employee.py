class Employee:
    n = 0 #n = numbrer of employees
    raise_percent = 10
    def __init__(self,name,lastname,age,income,tax=10):
        self.name = name
        self.lastname = lastname
        self.age = int(age)
        self.income = int(income)
        self.tax = int(tax)

        Employee.n += 1
        
    def fullname(self):
        return f"{self.name} {self.lastname}"
    def payment(self):
        return int(self.income) - int(self.income) * int(self.tax) / 100
    def increace_income(self):
       return (self.income) + (self.income * self.raise_percent / 100)
    
e1 = Employee("homayoun","jafari",15,12300)
print(e1.increace_income())




print(e1.n)