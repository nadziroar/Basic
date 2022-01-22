"""A simple class of a car"""

class Car:
    def __init__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0 

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f" Year : {self.year} \n Made by : {self.make} \n Model : {self.model} \n"
        return long_name.title()

    def get_Mileage (self):
        mileage_message = f"The latest mileage is : {self.mileage}"
        return mileage_message

    def update_Mileage(self, new_mileage):
        """To update the odometer reading to the given value. Reject the chang if it attempts to roll data"""
        if new_mileage >= self.mileage:
            self.mileage = new_mileage 
        else: 
            print('You cant roll back the mileage')
    
    def increment_Mileage (self , increase_mileage):
        """Add the given amount to the odometer reading"""
        self.mileage = increase_mileage

car1 = Car('Audi'  , 'A4' , 2009)

print(car1.get_descriptive_name())
print(car1.get_Mileage())