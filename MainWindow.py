#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow
from DataStore import data_store


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.datastore = data_store()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.BMR_btn.clicked.connect(self.showBMR)
        self.ui.BMI_btn.clicked.connect(self.showBMI)

        self.ui.bmr_calculate.clicked.connect(self.calcBMR)
        self.ui.bmi_calculate.clicked.connect(self.calcBMI)

    def show(self):
        self.main_win.show()

    def showBMI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmi)

    def showBMR(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmr)

    def calcBMR(self):
        # get input values from ui
        height = int(self.ui.bmr_height_input.text())
        weight = int(self.ui.bmr_weight_input.text())
        age = int(self.ui.bmr_age_input.text())
        if self.ui.bmr_radio_male.isChecked():
            sex = "male"
        else:
            sex = "female"
        # pass these values to data store
        if self.ui.bmr_radio_sed.isChecked():
            activity = "sedentary"
        elif self.ui.bmr_radio_lightly.isChecked():
            activity = "lightly active"
        elif self.ui.bmr_radio_moder.isChecked():
            activity = "moderately active"
        elif self.ui.bmr_radio_very.isChecked():
            activity = "very active"
        elif self.ui.bmr_radio_extreme.isChecked():
            activity = "extremely active"
            
        result = self.datastore.calc_bmr(height, weight, age, sex, activity)
        # format output
        output = f"The calorie intake for a {age} year old, who is {height}cm tall and weighs {weight}kg, who is {activity} is: {result} calories."
        # output to ui
        self.ui.bmr_output.setText(output)

    def calcBMI(self):
        # get input values from ui
        height = int(self.ui.height_input.text())
        weight = int(self.ui.weight_input.text())
        # pass these values to data store
        result = self.datastore.calc_bmi(height, weight)
        # format output
        output = f"You entered the following information for BMI: Height {height}cm, Weight: {weight}kg, This means your BMI is {result}"
        # output to ui
        self.ui.bmi_output.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
