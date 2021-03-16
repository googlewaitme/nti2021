import re


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelReg = QtWidgets.QLabel(self.centralwidget)
        self.labelReg.setGeometry(QtCore.QRect(260, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelReg.setFont(font)
        self.labelReg.setObjectName("labelReg")
        self.editSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.editSurname.setGeometry(QtCore.QRect(260, 100, 271, 31))
        self.editSurname.setObjectName("editSurname")
        self.surname = QtWidgets.QLabel(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(260, 80, 51, 16))
        self.surname.setObjectName("surname")
        self.EditName = QtWidgets.QLineEdit(self.centralwidget)
        self.EditName.setGeometry(QtCore.QRect(260, 180, 271, 31))
        self.EditName.setObjectName("EditName")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(260, 160, 51, 16))
        self.name.setObjectName("name")
        self.EditSecond = QtWidgets.QLineEdit(self.centralwidget)
        self.EditSecond.setGeometry(QtCore.QRect(260, 260, 271, 31))
        self.EditSecond.setObjectName("EditSecond")
        self.secondName = QtWidgets.QLabel(self.centralwidget)
        self.secondName.setGeometry(QtCore.QRect(260, 240, 61, 16))
        self.secondName.setObjectName("secondName")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(260, 330, 31, 17))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.male = QtWidgets.QLabel(self.centralwidget)
        self.male.setGeometry(QtCore.QRect(290, 330, 61, 16))
        self.male.setObjectName("male")
        self.female = QtWidgets.QLabel(self.centralwidget)
        self.female.setGeometry(QtCore.QRect(350, 330, 51, 16))
        self.female.setObjectName("female")
        self.lableEmail = QtWidgets.QLabel(self.centralwidget)
        self.lableEmail.setGeometry(QtCore.QRect(260, 360, 61, 16))
        self.lableEmail.setObjectName("lableEmail")
        self.EditEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.EditEmail.setGeometry(QtCore.QRect(260, 380, 271, 31))
        self.EditEmail.setObjectName("EditEmail")
        self.EfitPass = QtWidgets.QLineEdit(self.centralwidget)
        self.EfitPass.setGeometry(QtCore.QRect(260, 460, 271, 31))
        self.EfitPass.setObjectName("EfitPass")
        self.labelPass = QtWidgets.QLabel(self.centralwidget)
        self.labelPass.setGeometry(QtCore.QRect(260, 440, 61, 16))
        self.labelPass.setObjectName("labelPass")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 530, 271, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: black;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 85, 85);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    text-decoration: underline;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.emailChek = QtWidgets.QLabel(self.centralwidget)
        self.emailChek.setGeometry(QtCore.QRect(260, 420, 271, 16))
        self.emailChek.setStyleSheet("color: red;")
        self.emailChek.setObjectName("emailChek")
        self.passChek = QtWidgets.QLabel(self.centralwidget)
        self.passChek.setGeometry(QtCore.QRect(260, 500, 271, 16))
        self.passChek.setStyleSheet("color: red;")
        self.passChek.setObjectName("passChek")
        self.secondChek = QtWidgets.QLabel(self.centralwidget)
        self.secondChek.setGeometry(QtCore.QRect(260, 300, 271, 16))
        self.secondChek.setStyleSheet("color: red;")
        self.secondChek.setObjectName("secondChek")
        self.surChek = QtWidgets.QLabel(self.centralwidget)
        self.surChek.setGeometry(QtCore.QRect(260, 140, 271, 16))
        self.surChek.setStyleSheet("color: red;")
        self.surChek.setObjectName("surChek")
        self.nameChek = QtWidgets.QLabel(self.centralwidget)
        self.nameChek.setGeometry(QtCore.QRect(260, 220, 271, 16))
        self.nameChek.setStyleSheet("color: red;")
        self.nameChek.setObjectName("nameChek")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelReg.setText(_translate("MainWindow", "Регистрация"))
        self.surname.setText(_translate("MainWindow", "Фамилия"))
        self.name.setText(_translate("MainWindow", "Имя"))
        self.secondName.setText(_translate("MainWindow", "Отчество"))
        self.male.setText(_translate("MainWindow", "Мужской"))
        self.female.setText(_translate("MainWindow", "Женский"))
        self.lableEmail.setText(_translate("MainWindow", "Email"))
        self.labelPass.setText(_translate("MainWindow", "Пароль"))
        self.pushButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        # self.emailChek.setText(_translate("MainWindow", ""))
        # self.passChek.setText(_translate("MainWindow", ""))
        # self.secondChek.setText(_translate("MainWindow", ""))
        # self.surChek.setText(_translate("MainWindow", ""))
        # self.nameChek.setText(_translate("MainWindow", ""))

    def checker(self, name, surn, second, email, password):
        _translate = QtCore.QCoreApplication.translate
        if name == "" or surn == '' or second == '' or email == '' or password == '':
            self.passChek.setText(_translate("MainWindow", "Есть незаполненные поля!"))
        else:
            self.passChek.setText(_translate("MainWindow", ""))
            return True

    def checkData(self, login):
        _translate = QtCore.QCoreApplication.translate
        message = ""

        flag = False
        bool_ = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", login))

        if login != "":
            if bool_ == False:
                message = "Неверный формат почты!"
            else:
                message = ""
                flag = True

        self.emailChek.setText(_translate("MainWindow", message))
        return flag

    def wrongMes(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.passChek.setText(_translate("MainWindow", text))

