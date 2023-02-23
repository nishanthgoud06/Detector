

from PyQt5 import QtCore, QtGui, QtWidgets

from AdminHome import Ui_AdminHome
class Ui_Admin(object):

    def __init__(self, Dialog):
        self.dialog = Dialog

    def logincheck(self, event):

            try:

                unm = self.lineEdit.text()
                pwd = self.lineEdit_2.text()
                if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                    self.showMessageBox("Information", "Please fill out all fields")
                elif unm == "admin" and pwd == "admin":
                    self.home = QtWidgets.QDialog()
                    self.ui = Ui_AdminHome()
                    self.ui.setupUi(self.home)
                    self.home.show()
                    self.dialog.hide()
                else:
                    self.showMessageBox("Information", "Invalid Credentials..!")
            except Exception as e:
                print("Error=" + e.args[0])
                tb = sys.exc_info()[2]
                print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 480)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 70, 251, 51))
        self.label.setStyleSheet("font: 16pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 160, 151, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Vani\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 190, 221, 31))
        self.lineEdit.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 250, 221, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Vani\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 280, 221, 31))
        self.lineEdit_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(194, 340, 101, 41))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 75 14pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.logincheck)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(420, 150, 251, 241))
        self.label_4.setStyleSheet("image: url(../Detection/images/admin.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin"))
        self.label.setText(_translate("Dialog", "     Admin Login"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">ASASA</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Login"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
