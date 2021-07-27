class animals:
    def eat(self,meat):
        self.meat=meat
        print(self.meat)

class cat(animals):
    def sound (self,meow):
        self.meow=meow
        print(self.meow)

obj1=animals()
obj2=cat()


obj2.eat("meat")
obj2.sound("meow")