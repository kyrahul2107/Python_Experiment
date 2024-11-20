class Car:
    def __init__(self,model, brand):
        self.model=model
        self.brand=brand
    
    def fullName(self):
        return f" Model name is :{self.model} and brand name is :{self.brand}"
    
class ElectricCar(Car):
    def __init__(self, model, brand, batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize


# my_car=Car("Toyota", "Fortunre")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())
# myElectricCar=ElectricCar("My Model","My Brand","230 kWh")
# print(myElectricCar.batterySize)
# print(myElectricCar.model)
# print(myElectricCar.brand)
# print(myElectricCar.fullName())
