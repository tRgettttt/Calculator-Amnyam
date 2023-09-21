import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QPixmap, QMovie


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.memory = 0
        self.current_value = ""

        self.calcu()

    def calcu(self):
        self.setWindowTitle('Calculator Amnyam')
        self.setGeometry(0, 0, 1920, 1080)

        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 1920, 1080)
        pixmap = QPixmap("amnyam.jpg")
        background_label.setPixmap(pixmap)

        animation = QLabel(self)
        animation.setGeometry(1430, -350, 1000, 1000)
        gif_path = "amnyam17.gif"
        movie = QMovie(gif_path)
        animation.setMovie(movie)
        movie.start()

        self.display = QLineEdit(self)
        self.display.setGeometry(153, 100, 650, 120)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-style: oblique; font-size: 42px; padding: 5px; "
    "border: 3px solid pink; border-radius: 20px; font-weight: bold; background-color: transparent; color: #FFFFFF;"
)

        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '^', '=', '+',
            'C', 'M+', 'MR'
        ]

        delete_button = QPushButton('Del', self)
        delete_button.setGeometry(620, 800, 130, 130)
        delete_button.setStyleSheet("background-color: transparent; font-style: oblique;"
        "font-weight: bold; color: #FFFFFF; font-size: 42px;border: 3px solid pink; border-radius: 30px;")
        delete_button.clicked.connect(self.delete)

        x, y = 200, 240
        button_width, button_height = 130, 130

        for text in button_texts:
            button = QPushButton(text, self)
            button.setGeometry(x, y, button_width, button_height)
            button.setStyleSheet("background-color: transparent; font-style: oblique;"
        "font-weight: bold; color: #FFFFFF; font-size: 42px;border: 3px solid pink; border-radius: 30px;"
)
            button.clicked.connect(self.button_click)
            x += button_width + 10
            if x >= 700:
                x = 200
                y += button_height + 10

    def button_click(self):
        clicked_button = self.sender()
        clicked_text = clicked_button.text()

        if clicked_text == '=':
            try:
                result = eval(self.current_value)
                self.display.setText(str(result))
                self.current_value = str(result)
            except Exception as e:
                self.display.setText("Ам ням выдал ошибку")
                self.current_value = ""
        elif clicked_text == 'C':
            self.current_value = ""
            self.display.clear()
        elif clicked_text == '^':
            self.current_value += '**'
            self.display.setText(self.current_value)

        elif clicked_text == 'M+':
            try:
                self.memory = float(self.current_value)
                self.display.clear()
                self.current_value = ""
            except ValueError:
                self.display.setText("Ам ням выдал ошибку")
        elif clicked_text == 'MR':
            self.current_value = str(self.memory)
            self.display.setText(self.current_value)
        else:
            self.current_value += clicked_text
            self.display.setText(self.current_value)

    def delete(self):
        self.current_value = self.current_value[:-1]
        self.display.setText(self.current_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())