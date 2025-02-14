from strategies.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    
    def __init__(self, card_number: str, card_holder: str):
        self.card_number = card_number
        self.card_holder = card_holder
        
    
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of amount {amount}")