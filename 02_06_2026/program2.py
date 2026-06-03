'''
methods overriging is a type of runtime polymorphisms in which a child class (subclass) provide its own implementation of methods that is already define in its parent class (superclass/base)..
another words, methods which define in parent and redefine or update in child 
'''
class Payment:
    def pay(self,amount):
        print(f"Paying : {amount}")
class CreditCardPayment(Payment):
    def pay(self,amount,pin):
        print(f"Processing of {amount} through the credit card")
class UPIPayment(Payment):
    def pay(self,amount,pin):
        print(f"Processing of {amount} through the UPI")
class NetBankingPayment(Payment):
    def pay(self,amount,pin):
        print(f"Processing of {amount} through the NetBankingPayment")
lst = [CreditCardPayment(),UPIPayment(),NetBankingPayment()]

for x in lst:
    x.pay(100,1234)

