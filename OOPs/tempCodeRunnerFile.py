from abc import ABC , abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    @abstractmethod
    def validate(self):
        pass

class creditcard(payment):
    def pay(self,amount):
        print(f'credit card se {amount} pay hua')
    
    def validate(self):
        print("creditcard validate hua")

class upi(payment):
    def pay(self,amount):
        print(f'UPI se {amount} pay hua')
    
    def validate(self):
        print("UPI validate hua")

class cash(payment):
    def pay(self,amount):
        print(f'cash se {amount} pay hua')
    
    def validate(self):
        print("cash validate hua")

def process_payment(payment, amount):
    payment.pay(amount)
    payment.validate()

process_payment(creditcard(), 5000)
process_payment(upi(), 1000)
process_payment(cash(), 3000)