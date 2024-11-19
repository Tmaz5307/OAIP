from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Recipes(QWidget):
    def __init__(self):
        super().__init__()
        self.first_dish = QPushButton('Первое блюдо')
        QFontDatabase.addApplicationFont('path/to/Rondo Ancient Two.ttf')
        self.font = QFont('Rondo Ancient Two', 22)
        self.initUI()

    def initUI(self):
        self.setFont(self.font)
        self.setWindowTitle('Рецепты')
        self.setWindowIcon(QIcon('images/icon.ico'))
        main_l = QVBoxLayout()
        self.resize(400, 450)
        self.setFixedSize(self.width(), self.height())
        self.label = QLabel(self)
        pixmap = QPixmap('images/recipes.jpg')
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_l.addWidget(self.label)
        self.second_dish = QPushButton('Второе блюдо')
        self.oriental_cuisine = QPushButton('Восточная кухня')
        self.salads = QPushButton('Салаты')
        self.bake = QPushButton('Выпечка')
        self.close_button = QPushButton('Закрыть')
        main_l.addWidget(self.first_dish)
        main_l.addWidget(self.second_dish)
        main_l.addWidget(self.oriental_cuisine)
        main_l.addWidget(self.salads)
        main_l.addWidget(self.bake)
        main_l.addWidget(self.close_button)
        self.close_button.clicked.connect(self.go_back)
        self.setLayout(main_l)
        self.show()

    def show_first_dish(self):
        pass

    def show_second_dish(self):
        pass

    def show_oriental_cuisine(self):
        pass

    def show_salads(self):
        pass

    def show_bake(self):
        pass

    def go_back(self):
        self.close()

