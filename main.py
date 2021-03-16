import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from enterance import Ui_MainWindow
from reg import Ui_MainWindow_
from bd import RegistrationApi


def getLoginPassword():
    login = ui.login.text()
    password = ui.password.text()
    checker = ui.checkData(login, password)

    if checker:
        usersData = bdR.user_is_exist(password, login)
        if not usersData:
            ui.wrongMes("Неверная почта или пароль!")
        else:
            bdR.user_get_session(password, login)


bdR = RegistrationApi()
# start app
application = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def regNewUserPage():
    global otherWindow
    otherWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_()
    ui.setupUi(otherWindow)
    MainWindow.close()
    otherWindow.show()

    def returnToMain():
        otherWindow.close()
        MainWindow.show()

    def newDataUser():
        surname = ui.editSurname.text()
        name = ui.EditName.text()
        secondName = ui.EditSecond.text()
        male = 'M'
        email = ui.EditEmail.text()
        password = ui.EfitPass.text()
        print(name)
        chek1 = ui.checker(name, surname, secondName, email, password)
        chek2 = ui.checkData(email)
        chek3 = bdR.check_email_is_unique(email)
        if not chek3:
            ui.wrongMes("Такой пользователь существует!!!")
        if chek1 and chek2 and chek3:
            bdR.register_user(name=name, surname=surname, father_name=secondName,
                              email=email, sex=male, password=password)
            returnToMain()

    ui.pushButton.clicked.connect(newDataUser)
    ui.pushButton_2.clicked.connect(returnToMain)


ui.createNewUser.clicked.connect(regNewUserPage)
ui.Enter.clicked.connect(getLoginPassword)

sys.exit(application.exec_())
