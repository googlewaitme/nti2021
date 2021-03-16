from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 150, 351, 261))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login = QtWidgets.QLineEdit(self.frame)
        self.login.setGeometry(QtCore.QRect(30, 40, 291, 41))
        self.login.setStyleSheet("backdround-color: white;\n"
"border-color: black;\n"
"\n"
"")
        self.login.setInputMask("")
        self.login.setText("")
        self.login.setMaxLength(32767)
        self.login.setFrame(True)
        self.login.setCursorPosition(0)
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(30, 100, 291, 41))
        self.password.setStyleSheet("backdround-color: white;\n"
"border-color: black;\n"
"\n"
"")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setMaxLength(32767)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.createNewUser = QtWidgets.QPushButton(self.frame)
        self.createNewUser.setGeometry(QtCore.QRect(20, 150, 151, 23))
        self.createNewUser.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    text-decoration: underline;\n"
"}")
        self.createNewUser.setObjectName("createNewUser")
        self.Enter = QtWidgets.QPushButton(self.frame)
        self.Enter.setGeometry(QtCore.QRect(30, 200, 291, 31))
        self.Enter.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: black;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(63, 63, 63);\n"
"}\n"
"")
        self.Enter.setObjectName("Enter")
        self.laabelName = QtWidgets.QLabel(self.frame)
        self.laabelName.setGeometry(QtCore.QRect(30, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.laabelName.setFont(font)
        self.laabelName.setObjectName("laabelName")
        self.WrongMessage = QtWidgets.QLabel(self.frame)
        self.WrongMessage.setEnabled(False)
        self.WrongMessage.setGeometry(QtCore.QRect(30, 170, 291, 16))
        self.WrongMessage.setStyleSheet("color: red;")
        self.WrongMessage.setOpenExternalLinks(False)
        self.WrongMessage.setObjectName("WrongMessage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBU"))
        self.createNewUser.setText(_translate("MainWindow", "Вы новый пользователь?"))
        self.Enter.setText(_translate("MainWindow", "Войти в систему"))
        self.laabelName.setText(_translate("MainWindow", "Авторизация"))

    def checkData(self, login, password):
        _translate = QtCore.QCoreApplication.translate
        message = ""

        flag = False
        bool_ = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", login))

        if login == "" or password == "":
            message = "Есть незаполненные поля!"
        elif login != "":
            if bool_ == False:
                message = "Неверный формат почты!"
            else:
                message = ""
                flag = True

        self.WrongMessage.setText(_translate("MainWindow", message))
        return flag

    def wrongMes(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.WrongMessage.setText(_translate("MainWindow", text))
