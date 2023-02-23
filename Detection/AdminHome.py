

from PyQt5 import QtCore, QtGui, QtWidgets
from IntrusionDetect import Ui_IntrusionDetect
import sys
from Classification import Ui_Classify

class Ui_AdminHome(object):

    def NIDetection(self):
        try:
            self.ni = QtWidgets.QDialog()
            self.ui = Ui_IntrusionDetect()
            self.ui.setupUi(self.ni)
            self.ni.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def classification(self):

        try:
            self.clf = QtWidgets.QDialog()
            self.ui = Ui_Classify()
            self.ui.setupUi(self.clf)
            self.clf.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(685, 390)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -40, 691, 471))
        self.label.setStyleSheet("image: url(../Detection/images/shutterstock.jpg);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 90, 261, 51))
        self.pushButton.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.NIDetection)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 210, 261, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(129, 86, 64);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.classification)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.label.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Network Intrusion Detection"))
        self.pushButton_2.setText(_translate("Dialog", "Classification Analysis"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
