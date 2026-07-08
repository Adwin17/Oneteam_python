class Students:
    institute="OneTeam"

    def __init__(self,name,pl,num):
        self.name=name
        self._place=pl
        self.__no=num
        
    
    
  

    def display(self):
        print(f"Hi {self.name} , Welcome to {self.institute} , you are from {self._place}")
        print(self.__no)

s1=Students("Adwin","Aluva",17)




s1.display()
