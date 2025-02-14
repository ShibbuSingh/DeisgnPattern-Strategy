from strategies.payment_strategy import PaymentStrategy

class PaymentProcessor:
    
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
         
    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy
        
    def process_payment(self, amount: float) -> None:
        
        if not self._strategy:
            print("No payment method selected.")
            return
        self._strategy.pay(amount)