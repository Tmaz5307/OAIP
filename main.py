import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QFontDatabase, QIcon
from PyQt6.QtCore import Qt
from recipes import Recipes


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        QFontDatabase.addApplicationFont('path/to/Rondo Ancient Two.ttf')
        self.font = QFont('Rondo Ancient Two', 22)
        self.initUI()

    def initUI(self):
        self.setFont(self.font)
        self.setWindowTitle('Книга рецептов "Чиназес"')
        self.setWindowIcon(QIcon('images/icon.ico'))
        main_l = QVBoxLayout()
        main_l.setAlignment(Qt.AlignmentFlag.AlignCenter)
        wid = QWidget()
        wid.setLayout(main_l)
        self.setCentralWidget(wid)
        self.resize(600, 550)
        self.setFixedSize(self.width(), self.height())
        self.label = QLabel()
        pixmap = QPixmap('images/logo.jpg')
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_l.addWidget(self.label)
        self.recipes = QPushButton('Рецепты')
        self.favorites = QPushButton('Избранное(в разработке)')
        self.developers = QPushButton('О создателях')
        self.close = QPushButton('Выход')
        main_l.addWidget(self.recipes)
        main_l.addWidget(self.favorites)
        main_l.addWidget(self.developers)
        main_l.addWidget(self.close)
        self.recipes.clicked.connect(self.show_recipes)
        self.favorites.clicked.connect(self.show_favorites)
        self.developers.clicked.connect(self.show_developers)
        self.close.clicked.connect(QApplication.quit)
        self.show()

    def show_recipes(self):
        self.win_recipes = Recipes()
        self.win_recipes.show()

    def show_developers(self):
        self.win_developers = QMessageBox()
        self.win_developers.setWindowTitle('О создателях')
        self.win_developers.setText('Разработчики: Мажаров Артём и Плотников Дмитрий\nГруппа: 3СПИ')
        self.win_developers.show()

    def show_favorites(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWin()
    sys.exit(app.exec())
