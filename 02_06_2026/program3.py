class Payment:
    def pay(self,amount):
        print(f"Paying : {amount}")
class CreditCardPayment():
    def pay(self,amount):
        print(f"Processing of {amount} through the credit card")
class UPIPayment(Payment,CreditCardPayment):
    def pay(self,amount):
        print(f"Processing of {amount} through the UPI")


obj= UPIPayment()
obj.pay(1234)