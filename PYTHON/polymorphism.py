from abc import ABC,abstractmethod

class Student(ABC):
    @abstractmethod
    def greet(self):
        print("Print Welcome!")

class Boys(Student):
    def greet(self):
        return super().greet()

class Girl(Student):
    def greet(self):
        print("Welcome Girl")

b1=Boys()
b1.greet()
g1=Girl()
g1.greet()