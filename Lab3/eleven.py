class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary
        
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
        
    def display(self):
        print(f'Name is {self.name} Salary is {self.salary} department is {self.department}')
        

mg=Manager("Ahmed",2000,"finance")
mg.display()