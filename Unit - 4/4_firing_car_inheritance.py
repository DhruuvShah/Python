"""Demonstrate a FiringCar subclass with inherited car details and a fire method."""

class Car:
    def __init__(self, model, speed, price):
        self.model = model
        self.speed = speed
        self.price = price

    def display(self): 
        print("Model:", self.model) 
        print("Speed:", self.speed) 
        print("Price:", self.price) 

class Firing_car(Car):
    def __init__(self, model, speed, price, bullets):
        super().__init__(model, speed, price)
        self.bullets = bullets

    def fire(self):
        if self.bullets > 0:
            self.bullets -= 1
            print("Firied! Bullets remainig:", self.bullets)
        else:
            print("No bullets remaing.")

car = Firing_car("XR-1", 220,250000,5)
car.display()
car.fire()

        
