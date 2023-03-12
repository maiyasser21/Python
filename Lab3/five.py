class Car:
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
    def drive(self):
        self.mileage=self.mileage+(0.2*self.mileage)
        return self.mileage

car=Car("mm","yy","1970",80)
print("Mileage is :",car.drive())