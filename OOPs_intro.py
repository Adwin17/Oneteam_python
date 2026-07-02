'''
class Students:
    institute="OneTeam"

    def __init__(self,name,place):
        self.name=name
        self.place=place
        
    
        def get_details(self,name,place):
            self.name=name
            self.place=place
    
  

    def display(self):
        print(f"Hi {self.name} , Welcome to {self.institute} , you are from {self.place}")

s1=Students("Adwin","Aluva")

"""s1.get_details("Adwin","Aluva")"""


s1.display()
'''

class Animals():
      def __init__(self,n):
            self.name=n
            
    #   def get_name(self,n):
    #         self.name=n
        

class Dog(Animals):
      def __init__(self, n):
            super().__init__(n)
            print(self.name)

    
d1=Dog("Ricky")
# d1.get_name("Ricky")
# d1.info()