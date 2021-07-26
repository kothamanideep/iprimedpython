class India:
    def alotnumber(self,number):
        print(number)

class Carmanufacture(India):
     def makeAcar(self,brand,color,price):
         print(brand,color,price)

class seller(Carmanufacture):
    def customerorder(self,name,mobno):
        print(name,mobno)

objseller=seller()
objseller.customerorder("manideep",9182281076)
objseller.makeAcar("benz","blue",1000000)
objseller.alotnumber("AP12C8999")

