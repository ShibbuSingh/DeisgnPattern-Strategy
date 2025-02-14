from strategies.upi import UPIPayment
from strategies.paypal import PayPalPayment
from strategies.credit_card import CreditCardPayment
from context.payment_processor import PaymentProcessor

def main():
    
    credit_card = CreditCardPayment("123456", "Shibbu")
    paypal = PayPalPayment("shibbu@gmail.com")
    upi = UPIPayment("123456")
    
    
    processor = PaymentProcessor(credit_card)
    
    print("Paying with Credit card:-")
    processor.process_payment(100)
    
    print("Paying with PayPal:-")
    processor.set_strategy(paypal)
    processor.process_payment(101)
    
    print("Paying with UPI:-")
    processor.set_strategy(upi)
    processor.process_payment(102)
    
if __name__ == "__main__":
    main()
        

    
    