from abc import abstractmethod
import random

phone_list = ['+7 909-818-65-29', '+7 914-566-27-82', '+7 909-224-65-91', '+7 924-667-90-90', '+7 931-393-69-18']
email_list = ['Stas2020@gmail.com', 'KeKdr@mail.ru', 'Cringeman@gmail.com', 'Crossoverfan@yandex.ru',
              'mpupkin063@.gmail.com', 'vv9192127@gmail.com', 'petrenkoigor976@gmail.com']
push_list = ['Галя', 'Начальник', 'Жора', 'Брат', 'Никита', 'МАМА', 'ГОООООООООООЛ', ]


class Notification:
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self):
        pass


class SMSNotification(Notification):
    def send(self):
        print('На номер телефона {} отправленно'.format(random.choice(phone_list)))
        print("SMS с сообщением: {}".format(self.message))


class EmailNotification(Notification):
    def send(self):
        print('На Электронную почту {} отправленно'.format(random.choice(email_list)))
        print("письмо с сообщением: {}".format(self.message))


class PushNotification(Notification):
    def send(self):
        print('Контакту "{}" отправленно'.format(random.choice(push_list)))
        print("push-уведомление с сообщением: {}".format(self.message))


class NotificationFactory:
    @staticmethod
    def create_notification(type_of_message):
        if type_of_message == 'sms':
            return SMSNotification(input('Введите сообщение: '))
        elif type_of_message == 'email':
            return EmailNotification(input('Введите сообщение: '))
        elif type_of_message == 'push':
            return PushNotification(input('Введите сообщение: '))
        else:
            raise ValueError("Неизвестный тип уведомления")


if __name__ == "__main__":
    print('Сообщалкин™\nПишите как угодно и неизвестно кому!\n-----------------------')
    notif = NotificationFactory.create_notification(input('Введите тип сообщения(sms, email, push) '
                                                          'и нажмите кнопку Enter для продолжения: '))
    print('-----------------------')
    notif.send()
