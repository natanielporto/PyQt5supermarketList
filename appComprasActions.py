import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from appCompras import Ui_MainWindow

refeicao = {'Arroz': 90, 'Feijão': 60, 'Massa': 100, 'Carne': 140,
            'Ovo': 130, 'Legumes': 60, 'Verduras': 60, 'Vegetais': 80}

lanche = {'Pão': 100, 'Manteiga': 15, 'Geléia': 20, 'Leite': 250, 'Frutas': 80}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalcular.clicked.connect(self.calcular)
        self.ui.btnReiniciar.clicked.connect(self.reiniciar)
        self.ui.btnFaq.clicked.connect(self.listar)

        self.ui.numAdultos.setFocus()

    def calcular(self):
        self.ui.lista.clear()
        self.ui.quantidades.clear()

        if self.ui.numAdultos.text():
            quantAdulto = int(self.ui.numAdultos.text())
        else:
            quantAdulto = 0

        if self.ui.numCriancas.text():
            quantCrianca = int(self.ui.numCriancas.text())
        else:
            quantCrianca = 0

        if self.ui.numCafem.text():
            quantManha = int(self.ui.numCafem.text())
        else:
            quantManha = 0

        if self.ui.numAlmoco.text():
            quantAlmoco = int(self.ui.numAlmoco.text())
        else:
            quantAlmoco = 0

        if self.ui.numCafet.text():
            quantTarde = int(self.ui.numCafet.text())
        else:
            quantTarde = 0

        if self.ui.numJanta.text():
            quantJanta = int(self.ui.numJanta.text())
        else:
            quantJanta = 0

        if not quantAdulto and not quantCrianca:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText('Informe pelo menos um adulto ou uma criança.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            self.ui.numAdultos.setFocus()
            return
        elif not quantManha and not quantAlmoco and not quantTarde and not quantJanta:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Informe a quantidade de pelo menos uma das quatro refeições.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            self.ui.numCafem.setFocus()
            return
        else:
            if quantAdulto and (quantAlmoco or quantJanta):
                self.ui.lista.addItem('Refeições para adultos:')
                self.ui.quantidades.addItem('')
                for k, v in refeicao.items():
                    self.ui.lista.addItem(k)
                    total = ((v * quantAlmoco) + (v * quantJanta)) * \
                        quantAdulto
                    self.ui.quantidades.addItem(str(total/1000))
                self.ui.lista.addItem('-'*70)
                self.ui.quantidades.addItem('-'*10)

            if quantCrianca and (quantAlmoco or quantJanta):
                self.ui.lista.addItem('Refeições para crianças:')
                self.ui.quantidades.addItem('')
                for k, v in refeicao.items():
                    self.ui.lista.addItem(k)
                    total = ((v * (quantAlmoco/2)) +
                             (v * (quantJanta/2))) * quantCrianca
                    self.ui.quantidades.addItem(str(total/1000))
                self.ui.lista.addItem('-'*70)
                self.ui.quantidades.addItem('-'*10)

            if quantAdulto and (quantManha or quantTarde):
                self.ui.lista.addItem('Lanche para adultos:')
                self.ui.quantidades.addItem('')
                for k, v in lanche.items():
                    self.ui.lista.addItem(k)
                    total = ((v * quantManha) + (v * quantTarde)) * quantAdulto
                    self.ui.quantidades.addItem(str(total/1000))
                self.ui.lista.addItem('-'*70)
                self.ui.quantidades.addItem('-'*10)

            if quantCrianca and (quantManha or quantTarde):
                self.ui.lista.addItem('Lanches para crianças:')
                self.ui.quantidades.addItem('')
                for k, v in lanche.items():
                    self.ui.lista.addItem(k)
                    total = ((v * (quantManha/2)) +
                             (v * (quantTarde/2))) * quantCrianca
                    self.ui.quantidades.addItem(str(total/1000))
                self.ui.lista.addItem('-'*70)
                self.ui.quantidades.addItem('-'*10)

    def reiniciar(self):
        self.ui.numAdultos.setText('')
        self.ui.numCriancas.setText('')
        self.ui.numCafem.setText('')
        self.ui.numAlmoco.setText('')
        self.ui.numCafet.setText('')
        self.ui.numJanta.setText('')
        self.ui.lista.clear()
        self.ui.quantidades.clear()

    def listar(self):
        self.ui.lista.clear()
        self.ui.quantidades.clear()

        self.ui.lista.addItem('Itens considerados para refeições:')
        self.ui.quantidades.addItem('')
        for k, v in refeicao.items():
            self.ui.lista.addItem(k)
            self.ui.quantidades.addItem(f'{str(v)}g')

        self.ui.lista.addItem('-'*70)
        self.ui.quantidades.addItem('-'*10)
        self.ui.lista.addItem('Itens considerados para cafés:')
        self.ui.quantidades.addItem('')
        for k, v in lanche.items():
            self.ui.lista.addItem(k)
            self.ui.quantidades.addItem(f'{str(v)}g')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
