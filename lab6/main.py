import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calc(QWidget):
    def __init__(self):
        super(Calc, self).__init__()
        self.setWindowTitle("Калькулятор")
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_sixth = QHBoxLayout()
        self.hbox_seventh = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_fifth)
        self.vbox.addLayout(self.hbox_sixth)
        self.vbox.addLayout(self.hbox_seventh)

        self.input = QLineEdit(self )
        self.input.setReadOnly(True)
        self.hbox_input.addWidget(self.input)
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)
        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_plus = QPushButton("+", self)
        self.b_plus.clicked.connect(lambda: self._operation("+"))

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)



        self.b_minus = QPushButton("-", self)
        self.b_multiply = QPushButton("x", self)
        self.b_divide = QPushButton("/", self)
        self.hbox_fourth.addWidget(self.b_plus)
        self.hbox_fourth.addWidget(self.b_minus)
        self.hbox_fifth.addWidget(self.b_multiply)
        self.hbox_fifth.addWidget(self.b_divide)
        self.b_c = QPushButton(".", self)
        self.hbox_fifth.addWidget(self.b_c)
        self.b_result = QPushButton("=", self)
        self.hbox_sixth.addWidget(self.b_result)
        self.b_clean = QPushButton("Очистить", self)
        self.hbox_seventh.addWidget(self.b_clean)

        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
        self.b_multiply.clicked.connect(lambda: self._operation("x"))
        self.b_result.clicked.connect(self._result)
        self.b_clean.clicked.connect(lambda: self._operation("clean"))
        self.b_c.clicked.connect(lambda: self._button("."))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        try:
            self.num_1 = (self.input.text())
        except ValueError:
            self.num_1 = 0
        self.op = op
        self.input.setText("")

    def _result(self):
        try:
            self.num_2 = (self.input.text())
        except ValueError:
            self.num_2 = 0

        try:
            if self.op == "+":
                self.input.setText(str(float(self.num_1) + float(self.num_2)))
            if self.op == "x":
                self.input.setText(str(float(self.num_1) * float(self.num_2)))
            if self.op == "/":
                self.input.setText(str(float(self.num_1) / float(self.num_2)))
            if self.op == "-":
                self.input.setText(str(float(self.num_1) - float(self.num_2)))
            if self.op == "clean":
                self.input.setText((str("")))
        except AttributeError:
            self.input.setText("Выбирете выражение правельно")
        except ZeroDivisionError:
            self.input.setText("Деление на 0 невозможно")


app = QApplication(sys.argv)
win = Calc()
win.show()
sys.exit(app.exec_())
