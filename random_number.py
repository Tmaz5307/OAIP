from PyQt6.QtWidgets import *
import random


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.random_number = 0


    def initUI(self):
        self.resize(400, 50)
        self.setWindowTitle('Random number')
        button = QPushButton('Сгенерировать число')
        self.label = QLabel('Случайное число')
        main_l = QVBoxLayout()
        main_l.addStretch()
        main_l.addWidget(button)
        main_l.addWidget(self.label)
        self.setLayout(main_l)
        button.clicked.connect(self.number)

    def number(self):
        self.random_number = str(random.randrange(1, 100))
        self.label.setText(f'Случайное число: {self.random_number}')


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
