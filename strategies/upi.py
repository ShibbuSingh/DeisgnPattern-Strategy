from strategies.payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):
    
    def __init__(self, upiid: str):
        self.upiid = upiid
        
    
    def pay(self, amount: float) -> None:
        print(f"Processing UPI payment of amount {amount}")