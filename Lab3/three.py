class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def increaseSalary(self):
       self.salary=self.salary+(0.2*self.salary)
       return self.salary
        
emp=Employee("ahmed",25,1000)
print("The increased salary is :", emp.increaseSalary())

        
        