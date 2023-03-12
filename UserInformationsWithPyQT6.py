from PyQt6 import QtWidgets
from UI import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBoxCountry.addItems(["Turkey","Azerbaijan","Kazakhistan","Turkmenistan"])
        self.ui.pushButtonSave.clicked.connect(self.ButtonSave)

    def ButtonSave(self):
        for i in self.ui.groupBox.findChildren(QtWidgets.QRadioButton):
            if i.isChecked():
                self.sex = i.text()
        
        self.hobbys = []
        for i in self.ui.groupBox_2.findChildren(QtWidgets.QCheckBox):
            if i.isChecked():
                self.hobbys.append(i.text())
        
        # print(self.ui.comboBoxCountry.currentText())
        # print(self.ui.dateEditBirthday.text())

        self.informations = f"""
        
        Name: {self.ui.lineEditName.text()}
        Surname: {self.ui.lineEditSurname.text()}
        Sex: {self.sex}
        Hobbies: {self.hobbys}
        Birthday: {self.ui.dateEditBirthday.text()}
        """
        
        self.ui.resultLabel.setText(self.informations)


def run():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

run()