class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Processing credit card payment of ${amount} using card {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount} using email {self.email}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Processing Bitcoin payment of ${amount} using wallet {self.wallet_address}")

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    
    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)



credit_card_payment = CreditCardPayment("1234-5678-9876-5432")
paypal_payment = PayPalPayment("user@example.com")
bitcoin_payment = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    
processor = PaymentProcessor(credit_card_payment)
processor.process_payment(100)

processor.set_strategy(paypal_payment)
processor.process_payment(100)

processor.set_strategy(bitcoin_payment)
processor.process_payment(100)
