'''TASK3. Create an interface for PaymentGateway and implement it in PayPal, Stripe.'''


from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod

    def process_payment(self):
        pass
    def refund_payment(self):
        pass

class PayPal(PaymentGateway):
    def process_payment(self,amount):
        print(f"{amount} is addded to your wallet")
        return True
    def refund_payment(self,transaction_id):
        print(f"{transaction_id} is the id for transaction")
        return True

class Stripe(PaymentGateway):
    def process_payment(self,amount):
        print(f"{amount} is addded to your wallet")
        return True

    def refund_payment(self,transaction_id):
        print(f"{transaction_id} is the id for transaction")
        return True

obj = [PayPal(),Stripe()]

for an in obj:
    an.process_payment(100)