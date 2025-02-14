from strategies.payment_strategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    
    def __init__(self, email: str):
        self.email = email
        
    
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of amount {amount}")