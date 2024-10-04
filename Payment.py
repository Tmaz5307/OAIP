from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def perform_payment(self):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def perform_payment(self):
        print(f"Выполнение платежа по кредитной карте {self.card_number}")


class EWalletPayment(PaymentMethod):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def perform_payment(self):
        print(f"Выполнение платежа через электронный кошелек {self.wallet_id}")


class Platform:
    def __init__(self, platform_name):
        self.platform_name = platform_name

    def process_payment(self, payment_method):
        if not isinstance(payment_method, PaymentMethod):
            raise TypeError("Платежный метод должен быть экземпляром класса PaymentMethod.")

        payment_method.perform_payment()
        print(f"Платформа {self.platform_name} обработала платеж.")


def main():
    credit_card_payment = CreditCardPayment('1234', '01/2026', '123')
    ewallet_payment = EWalletPayment('abcde')
    mobile_app_platform = Platform("мобильное приложение")
    web_platform = Platform("веб платформа")

    methods = [credit_card_payment, ewallet_payment]
    platforms = [mobile_app_platform, web_platform]

    for method in methods:
        for platform in platforms:
            platform.process_payment(method)


if __name__ == "__main__":
    main()
