import random

list_words = ['Шагай веселей!', 'Шагай на раслабоне)', 'Грустно шагай(', 'Шагай по обычному']


class FitnessTrackerFacade:
    def __init__(self):
        self.stepmeter = Stepmeter()
        self.heartbeat = Heartbeat()
        self.sleep = Sleep()

    def start_step(self):
        print('Балдёжный шагомер™ \n--------------------')
        while True:
            enter = int(input(f'Чтобы сделать шаг введите "1"\nЧтобы прекратить шагать введите '
                              f'"2"\nВвод: '))
            if enter == 1:
                print('--------------------')
                self.stepmeter.do_step()
                print('--------------------')
            if enter == 2:
                print('--------------------')
                self.stepmeter.stop_step()
                print('--------------------')
                break

    def show_heartbeat(self):
        print('Чекни, че там по сердечку™ \n--------------------')
        print('Нормальное сердцебиение: 60-75 ударов в минуту')
        enter = int(input('Чтобы проверить сердцебиение введите "1"\nВвод: '))
        if enter == 1:
            self.heartbeat.check_heartbeat()

    def show_sleep_quality(self):
        print('Как спалось?™ \n--------------------')
        print('Нормальные показатели : | Пульс: 18-20 ударов/мин | Нормальная частота движений')
        enter = int(input('Чтобы проверить качество сна введите "1"\nВвод: '))
        if enter == 1:
            self.sleep.check_sleep()
        else:
            print('Неверный ввод')
            return enter


class Stepmeter:
    def __init__(self):
        self.steps = 0

    def do_step(self):
        self.steps += 1
        print(random.choice(list_words))

    def stop_step(self):
        print("Пройдено шагов: ", self.steps)


class Heartbeat:
    def __init__(self):
        self.beat = random.randrange(40, 120)

    def check_heartbeat(self):
        if 90 >= self.beat >= 60:
            print('Нормальное сердцебиение', '|', self.beat, "Ударов в минуту")
        else:
            print('Сердце: "Моя остановочка"', '|', self.beat, "Ударов в минуту")


class Sleep:
    def __init__(self):
        self.pulse = random.randrange(15, 25)
        self.frequency_of_movements = random.randrange(58, 61)

    def check_sleep(self):
        if 22 >= self.pulse >= 18:
            print('Выспался', '|', self.pulse, "Пульс", '|', 'Нормальная частота движений')
        else:
            print('Еще пять минуточек...', '|', self.pulse, "ударов/мин ", '|', 'Плохая частота движений')


fitness_tracker = FitnessTrackerFacade()
fitness_tracker.show_heartbeat()
fitness_tracker.show_sleep_quality()
fitness_tracker.start_step()
