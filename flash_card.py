import sys
import random
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDesktopWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QFont


from dictionary import words


class FlashCard(QWidget):

    def __init__(self):
        super().__init__()

        self.character_label = QLabel()
        self.answer_label = QLabel()
        self.pinyin_label = QLabel()

        self.initUI()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):

        self.character_label.setFont(QFont('Arial', 200, QFont.Bold))

        self.answer_label.hide()
        self.answer_label.setFont(QFont('Arial', 50, QFont.Bold))

        self.pinyin_label.hide()
        self.pinyin_label.setFont(QFont('Arial', 50, QFont.Bold))

        show_button = QPushButton('Show Answer', self)

        show_button.clicked.connect(self.show_answer)
        next_button = QPushButton('Next', self)
        next_button.clicked.connect(self.load_character)

        layout = QGridLayout()
        layout.addWidget(self.character_label, 0, 0)
        layout.addWidget(self.answer_label, 1, 0)
        layout.addWidget(self.pinyin_label, 2, 0)
        layout.addWidget(show_button, 3, 0)
        layout.addWidget(next_button, 4, 0)

        self.setLayout(layout)

        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('Flash Cards')

        self.center()
        self.load_character()

        self.show()

    def show_answer(self):
        self.answer_label.show()
        self.pinyin_label.show()

    def load_character(self):
        choice = random.choice(words)

        self.character_label.setText(choice['character'])
        self.answer_label.hide()
        self.answer_label.setText(choice['definition'])
        self.pinyin_label.hide()
        self.pinyin_label.setText(choice['pinyin'])


if __name__ == '__main__':

    app = QApplication(sys.argv)
    flash_card = FlashCard()
    sys.exit(app.exec_())
