# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appCompras.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 640)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.numCriancas = QtWidgets.QLineEdit(self.centralwidget)
        self.numCriancas.setGeometry(QtCore.QRect(160, 160, 21, 21))
        self.numCriancas.setObjectName("numCriancas")
        self.topRefeicao = QtWidgets.QLabel(self.centralwidget)
        self.topRefeicao.setGeometry(QtCore.QRect(30, 370, 161, 31))
        self.topRefeicao.setObjectName("topRefeicao")
        self.numAdultos = QtWidgets.QLineEdit(self.centralwidget)
        self.numAdultos.setGeometry(QtCore.QRect(160, 130, 21, 21))
        self.numAdultos.setObjectName("numAdultos")
        self.topPessoas = QtWidgets.QLabel(self.centralwidget)
        self.topPessoas.setGeometry(QtCore.QRect(30, 90, 151, 41))
        self.topPessoas.setObjectName("topPessoas")
        self.numCafem = QtWidgets.QLineEdit(self.centralwidget)
        self.numCafem.setGeometry(QtCore.QRect(160, 410, 21, 21))
        self.numCafem.setObjectName("numCafem")
        self.numAlmoco = QtWidgets.QLineEdit(self.centralwidget)
        self.numAlmoco.setGeometry(QtCore.QRect(160, 440, 21, 21))
        self.numAlmoco.setObjectName("numAlmoco")
        self.numCafet = QtWidgets.QLineEdit(self.centralwidget)
        self.numCafet.setGeometry(QtCore.QRect(160, 470, 21, 21))
        self.numCafet.setObjectName("numCafet")
        self.numJanta = QtWidgets.QLineEdit(self.centralwidget)
        self.numJanta.setGeometry(QtCore.QRect(160, 500, 21, 21))
        self.numJanta.setObjectName("numJanta")
        self.btnCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(30, 540, 181, 71))
        self.btnCalcular.setObjectName("btnCalcular")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 210, 171, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../../../home/nataniel/Documents/imagem.bmp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.topLista = QtWidgets.QLabel(self.centralwidget)
        self.topLista.setGeometry(QtCore.QRect(260, 90, 171, 41))
        self.topLista.setObjectName("topLista")
        self.btnReiniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btnReiniciar.setGeometry(QtCore.QRect(260, 540, 231, 71))
        self.btnReiniciar.setObjectName("btnReiniciar")
        self.btnFaq = QtWidgets.QPushButton(self.centralwidget)
        self.btnFaq.setGeometry(QtCore.QRect(540, 540, 221, 71))
        self.btnFaq.setObjectName("btnFaq")
        self.topPessoas_2 = QtWidgets.QLabel(self.centralwidget)
        self.topPessoas_2.setGeometry(QtCore.QRect(10, 20, 761, 41))
        self.topPessoas_2.setObjectName("topPessoas_2")
        self.checkAdultos = QtWidgets.QLabel(self.centralwidget)
        self.checkAdultos.setGeometry(QtCore.QRect(30, 130, 54, 17))
        self.checkAdultos.setObjectName("checkAdultos")
        self.checkCriancas = QtWidgets.QLabel(self.centralwidget)
        self.checkCriancas.setGeometry(QtCore.QRect(30, 160, 54, 17))
        self.checkCriancas.setObjectName("checkCriancas")
        self.checkCafem = QtWidgets.QLabel(self.centralwidget)
        self.checkCafem.setGeometry(QtCore.QRect(30, 410, 111, 17))
        self.checkCafem.setObjectName("checkCafem")
        self.checkAlmoco = QtWidgets.QLabel(self.centralwidget)
        self.checkAlmoco.setGeometry(QtCore.QRect(30, 440, 54, 17))
        self.checkAlmoco.setObjectName("checkAlmoco")
        self.checkCafet = QtWidgets.QLabel(self.centralwidget)
        self.checkCafet.setGeometry(QtCore.QRect(30, 470, 91, 17))
        self.checkCafet.setObjectName("checkCafet")
        self.checkJanta = QtWidgets.QLabel(self.centralwidget)
        self.checkJanta.setGeometry(QtCore.QRect(30, 500, 54, 17))
        self.checkJanta.setObjectName("checkJanta")
        self.topQuantidade = QtWidgets.QLabel(self.centralwidget)
        self.topQuantidade.setGeometry(QtCore.QRect(670, 90, 91, 41))
        self.topQuantidade.setObjectName("topQuantidade")
        self.lista = QtWidgets.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(260, 130, 401, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lista.setFont(font)
        self.lista.setObjectName("lista")
        self.quantidades = QtWidgets.QListWidget(self.centralwidget)
        self.quantidades.setGeometry(QtCore.QRect(670, 130, 91, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quantidades.setFont(font)
        self.quantidades.setObjectName("quantidades")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topRefeicao.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Refeições / dia:</span></p></body></html>"))
        self.topPessoas.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Nº de pessoas:</span></p></body></html>"))
        self.btnCalcular.setStatusTip(_translate("MainWindow", "Calcula as quantidades necessárias para compras do mês."))
        self.btnCalcular.setText(_translate("MainWindow", "Calcular"))
        self.topLista.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">O que comprar:</span></p></body></html>"))
        self.btnReiniciar.setStatusTip(_translate("MainWindow", "Calcula as quantidades necessárias para compras do mês."))
        self.btnReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.btnFaq.setStatusTip(_translate("MainWindow", "Calcula as quantidades necessárias para compras do mês."))
        self.btnFaq.setText(_translate("MainWindow", "Calculo considerado"))
        self.topPessoas_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">LISTA BÁSICA PARA O SUPERMERCADO</span></p></body></html>"))
        self.checkAdultos.setText(_translate("MainWindow", "Adultos"))
        self.checkCriancas.setText(_translate("MainWindow", "Crianças"))
        self.checkCafem.setText(_translate("MainWindow", "Cafe da Manha"))
        self.checkAlmoco.setText(_translate("MainWindow", "Almoço"))
        self.checkCafet.setText(_translate("MainWindow", "Cafe da Tarde"))
        self.checkJanta.setText(_translate("MainWindow", "Janta"))
        self.topQuantidade.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Kg:</span></p></body></html>"))