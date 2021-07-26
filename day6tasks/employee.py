class Employee:
    name="mani"
    
    def printname(self):
        print(self.name)

Employee.printname=classmethod(Employee.printname)
Employee.printname()