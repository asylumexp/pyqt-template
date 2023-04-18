#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from Ui_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.btn_go.clicked.connect(self.update_text)
        a = QTextEdit

    def show(self):
        self.main_win.show()

    def update_text(self):
        first = self.ui.firstNameInput.toPlainText()
        self.ui.lbl_output.setText(f"You are {first}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
