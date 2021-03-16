import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from enterance import Ui_MainWindow
from bd import RegistrationApi

def getLoginPassword():
    login = ui.login.text()
    password = ui.password.text()
    checker = ui.checkData(login, password)

    if checker:
        usersData = bdR.user_is_exist(login, password)
        if not usersData:
            ui.wrongMes("Неверная почта или пароль!")
        else:
            bdR.user_get_session(password, login)


# start app
application = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
bdR = RegistrationApi()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# logic
ui.Enter.clicked.connect(getLoginPassword)


# exit
sys.exit(application.exec_())
