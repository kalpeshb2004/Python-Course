class engine:
    def start(self):
        return "engine has started"

class car:
    def __init__(self,brand):
        self.brand = brand
        self.engine = engine() # using as object

    def start(self):
        return f"brand : {self.brand}" , self.engine.start() #delegation its just forword the call 

c = car("toyota")
print(c.start())
    