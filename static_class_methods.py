'''
class Student:
    course="Java"

    def __init__(self,name):
        self.name=name

    def year(self,year):
        self.year=year

    @classmethod
    def change(cls):
        cls.course="Python"

    @staticmethod
    def show():
        print("Thank you")


Student.change() #class method
s=Student("Adwin")
s.year(2008)
print(s.name,s.year,s.course)
Student.show() #static method
'''

