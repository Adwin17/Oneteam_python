from abc import abstractmethod,ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
        
    def horn(self):
        print("Beep Beep")

class Bike(Vehicle):
    def start(self):
        print("Starting Bike")

class Car(Vehicle):
    def start(self):
        print("Starting Car")

b1=Bike()
b1.start()
b1.horn()

c1=Car()
c1.start()