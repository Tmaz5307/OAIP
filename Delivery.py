import random


class DeliveryStrategy:
    def deliver(self):
        pass


class CourierDelivery(DeliveryStrategy):
    def deliver(self):
        print("Способ доставки: Курьер")


class PostalDelivery(DeliveryStrategy):
    def deliver(self):
        print("Способ доставки: Почта")


class DroneDelivery(DeliveryStrategy):
    def deliver(self):
        print("Способ доставки: Дрон")


class DeliveryContext:
    def __init__(self, delivery: DeliveryStrategy):
        self.delivery = delivery

    def choose_delivery(self):
        self.delivery.deliver()


def main():
    strategies = [CourierDelivery(), PostalDelivery(), DroneDelivery()]
    context = DeliveryContext(random.choice(strategies))
    context.choose_delivery()


if __name__ == '__main__':
    main()
