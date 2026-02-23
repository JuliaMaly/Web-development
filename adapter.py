class PaymentProcessor:
    def pay(self, amount):
        pass


class OldPaymentSystem:
    def make_payment(self, value):
        return f"Paid {value} using old system"



class PaymentAdapter(PaymentProcessor):
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        return self.old_system.make_payment(amount)


if __name__ == "__main__":
    old_system = OldPaymentSystem()
    adapter = PaymentAdapter(old_system)

    print(adapter.pay(100))