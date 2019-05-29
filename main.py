from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import calculator

class ExampleApp(QtWidgets.QMainWindow, calculator.Ui_Dialog):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Add.clicked.connect(self.add)
        
    def clear(self):
        self.input_1.setText("")
        self.input_2.setText("")
        
        
    def add(self):
       num1 =  float(self.input_1.text())
       num2 = float(self.input_2.text())
       sum = num1 + num2
       self.result.setText("%.2f" % sum)
       self.clear()
    
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
