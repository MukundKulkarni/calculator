# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 360)
        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(40, 220, 94, 36))
        self.Add.setObjectName("Add")
        self.input_1 = QtWidgets.QLineEdit(Dialog)
        self.input_1.setGeometry(QtCore.QRect(30, 140, 141, 51))
        self.input_1.setText("")
        self.input_1.setObjectName("input_1")
        self.input_2 = QtWidgets.QLineEdit(Dialog)
        self.input_2.setGeometry(QtCore.QRect(270, 140, 141, 51))
        self.input_2.setText("")
        self.input_2.setObjectName("input_2")
        self.result = QtWidgets.QLineEdit(Dialog)
        self.result.setGeometry(QtCore.QRect(22, 40, 401, 51))
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setClearButtonEnabled(False)
        self.result.setObjectName("result")
        self.result.setReadOnly(True)
        self.Sub = QtWidgets.QPushButton(Dialog)
        self.Sub.setGeometry(QtCore.QRect(290, 220, 94, 36))
        self.Sub.setObjectName("Sub")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 110, 63, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(302, 110, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 63, 20))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.Mul = QtWidgets.QPushButton(Dialog)
        self.Mul.setGeometry(QtCore.QRect(40, 280, 94, 36))
        self.Mul.setObjectName("Mul")
        self.Div = QtWidgets.QPushButton(Dialog)
        self.Div.setGeometry(QtCore.QRect(290, 280, 94, 36))
        self.Div.setObjectName("Div")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Add.setText(_translate("Dialog", "Add"))
        self.Sub.setText(_translate("Dialog", "Sub"))
        self.label.setText(_translate("Dialog", "Number 1"))
        self.label_2.setText(_translate("Dialog", "Number 2"))
        self.label_3.setText(_translate("Dialog", "Result"))
        self.Mul.setText(_translate("Dialog", "Mul"))
        self.Div.setText(_translate("Dialog", "Div"))

