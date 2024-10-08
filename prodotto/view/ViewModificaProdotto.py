from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

# Questa view serve per prendere in input un prodotto e ne permette di modificare i campi appositi, visualizzandone quelli già presenti

class ViewModificaProdotto(QWidget):
    def __init__(self, controller, update_ui, prodotto, parent=None):
        super(ViewModificaProdotto, self).__init__(parent)
        self.controller = controller
        self.update_ui = update_ui
        self.prodotto = prodotto
        self.setObjectName("MainWindow")
        self.resize(1071, 715)
        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(15)
        font.setWeight(75)


    # Parte Statica

    
        # Gestione icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_marca.setObjectName("label_marca")
        self.gridLayout.addWidget(self.label_marca, 7, 3, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        # Pulsanti che sono in fondo alla pagina
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        # annulla
        self.pushButton_annulla = QtWidgets.QPushButton(self.widget)
        self.pushButton_annulla.setObjectName("pushButton_annulla")
        self.horizontalLayout.addWidget(self.pushButton_annulla)
        self.pushButton_annulla.setStyleSheet("QPushButton {\n"
                                               "   background-color:white;\n"
                                               "   border-width: 2px;\n"
                                               "   border-radius: 10px;\n"
                                               "   border: 2px solid gray;\n"
                                               "   font: bold 12px;\n"
                                               "   padding: 6px;\n"
                                               "}")
        self.pushButton_annulla.clicked.connect(self.close)
        # salvataggio
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_salva = QtWidgets.QPushButton(self.widget)
        self.pushButton_salva.setFont(font)
        self.pushButton_salva.setObjectName("pushButton_salva")
        self.horizontalLayout.addWidget(self.pushButton_salva)
        self.pushButton_salva.setStyleSheet("QPushButton {\n"
                                               "   background-color: rgb(26, 218, 108);\n"
                                               "   border-width: 2px;\n"
                                               "   border-radius: 10px;\n"
                                               "   font: bold 12px;\n"
                                               "   padding: 6px;\n"
                                               "   color: black;\n"
                                               "}")
        self.pushButton_salva.clicked.connect(self.controllo_click)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        # Schermata centrale
        self.gridLayout.addWidget(self.widget, 25, 1, 1, 5)
        # SCONTO
        self.label_sconto = QtWidgets.QLabel(self.centralwidget)
        self.label_sconto.setObjectName("label_sconto")
        self.label_sconto.setFont(font)
        self.gridLayout.addWidget(self.label_sconto, 22, 5, 1, 1)

        self.lineEdit_sconto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sconto.setObjectName("lineEdit_sconto")
        self.gridLayout.addWidget(self.lineEdit_sconto, 23, 5, 1, 1)
        # QUANTITA
        self.label_quantita = QtWidgets.QLabel(self.centralwidget)
        self.label_quantita.setObjectName("label_quantita")
        self.label_quantita.setFont(font)
        self.gridLayout.addWidget(self.label_quantita, 16, 5, 1, 1)

        self.lineEdit_quantita = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_quantita.setObjectName("lineEdit_quantita")
        self.gridLayout.addWidget(self.lineEdit_quantita, 17, 5, 1, 1)
        # TIPOLOGIA
        self.label_tipologia = QtWidgets.QLabel(self.centralwidget)
        self.label_tipologia.setObjectName("label_tipologia")
        self.label_tipologia.setFont(font)
        self.gridLayout.addWidget(self.label_tipologia, 12, 3, 1, 1)

        self.comboBox_tipologia = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tipologia.setObjectName("comboBox_tipologia")
        self.comboBox_tipologia.addItem("Pianoforti acustici")
        self.comboBox_tipologia.addItem("Pianoforti digitali")
        self.comboBox_tipologia.addItem("Chitarre elettriche")
        self.comboBox_tipologia.addItem("Chitarre acustiche")
        self.comboBox_tipologia.addItem("Violini")
        self.comboBox_tipologia.addItem("Viole")
        self.comboBox_tipologia.addItem("Violoncelli")
        self.comboBox_tipologia.addItem("Bassi")
        self.comboBox_tipologia.addItem("Xilofoni")
        self.comboBox_tipologia.addItem("Maracas")
        self.comboBox_tipologia.addItem("Batterie")
        self.comboBox_tipologia.addItem("Flauti")
        self.comboBox_tipologia.addItem("Fiati ad ancia")
        self.comboBox_tipologia.addItem("Ottoni")
        self.comboBox_tipologia.addItem("Organi")
        self.comboBox_tipologia.addItem("Armoniche")
        self.comboBox_tipologia.addItem("Sintetizzatori")
        self.gridLayout.addWidget(self.comboBox_tipologia, 14, 3, 1, 1)
        # DATA ORDINE
        self.label_data_ordine = QtWidgets.QLabel(self.centralwidget)
        self.label_data_ordine.setFont(font)
        self.label_data_ordine.setObjectName("label_data_ordine")
        self.gridLayout.addWidget(self.label_data_ordine, 0, 5, 1, 1)

        self.dateEdit_data_ordine = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_data_ordine.setObjectName("dateEdit_data_ordine")
        self.gridLayout.addWidget(self.dateEdit_data_ordine, 1, 5, 1, 1)
        # CODICE FORNITORE
        self.label_cod_fornitore = QtWidgets.QLabel(self.centralwidget)
        self.label_cod_fornitore.setObjectName("label_cod_fornitore")
        self.label_cod_fornitore.setFont(font)
        self.gridLayout.addWidget(self.label_cod_fornitore, 0, 3, 1, 1)

        self.lineEdit_cod_fornitore = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cod_fornitore.setObjectName("lineEdit_cod_fornitore")
        self.gridLayout.addWidget(self.lineEdit_cod_fornitore, 1, 3, 1, 1)
        # CODICE FATTURA
        self.lineEdit_cod_fattura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cod_fattura.setObjectName("lineEdit_cod_fattura")
        self.gridLayout.addWidget(self.lineEdit_cod_fattura, 1, 1, 1, 1)

        self.label_cod_fattura = QtWidgets.QLabel(self.centralwidget)
        self.label_cod_fattura.setFont(font)
        self.label_cod_fattura.setTextFormat(QtCore.Qt.AutoText)
        self.label_cod_fattura.setObjectName("label_cod_fattura")
        self.gridLayout.addWidget(self.label_cod_fattura, 0, 1, 1, 1)
        # CODICE PRODOTTO
        self.label_cod_prodotto = QtWidgets.QLabel(self.centralwidget)
        self.label_cod_prodotto.setObjectName("label_cod_prodotto")
        self.label_cod_prodotto.setFont(font)
        self.gridLayout.addWidget(self.label_cod_prodotto, 7, 1, 1, 1)

        self.lineEdit_cod_prodotto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cod_prodotto.setObjectName("lineEdit_cod_prodotto")
        self.gridLayout.addWidget(self.lineEdit_cod_prodotto, 8, 1, 1, 1)
        # COLORE
        self.label_colore = QtWidgets.QLabel(self.centralwidget)
        self.label_colore.setObjectName("label_colore")
        self.label_colore.setFont(font)
        self.gridLayout.addWidget(self.label_colore, 16, 1, 1, 1)

        self.lineEdit_colore = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_colore.setObjectName("lineEdit_colore")
        self.gridLayout.addWidget(self.lineEdit_colore, 17, 1, 1, 1)
        # MATERIALE
        self.label_materiale = QtWidgets.QLabel(self.centralwidget)
        self.label_materiale.setObjectName("label_materiale")
        self.label_materiale.setFont(font)
        self.gridLayout.addWidget(self.label_materiale, 12, 5, 1, 1)

        self.lineEdit_materiale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_materiale.setObjectName("lineEdit_materiale")
        self.gridLayout.addWidget(self.lineEdit_materiale, 14, 5, 1, 1)
        # CATEGORIA
        self.label_categoria = QtWidgets.QLabel(self.centralwidget)
        self.label_categoria.setObjectName("label_categoria")
        self.label_categoria.setFont(font)
        self.gridLayout.addWidget(self.label_categoria, 12, 1, 1, 1)

        self.comboBox_categoria = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.comboBox_categoria.addItem("Aerofoni")
        self.comboBox_categoria.addItem("Cordofoni")
        self.comboBox_categoria.addItem("Membranofoni")
        self.comboBox_categoria.addItem("Idiofoni")
        self.comboBox_categoria.addItem("Elettrofoni")
        self.gridLayout.addWidget(self.comboBox_categoria, 14, 1, 1, 1)
        # PREZZO ACQUISTO
        self.lineEdit_prezzo_acquisto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prezzo_acquisto.setObjectName("lineEdit_prezzo_acquisto")
        self.gridLayout.addWidget(self.lineEdit_prezzo_acquisto, 20, 1, 1, 1)

        self.label_prezzo_acquisto = QtWidgets.QLabel(self.centralwidget)
        self.label_prezzo_acquisto.setObjectName("label_prezzo_acquisto")
        self.label_prezzo_acquisto.setFont(font)
        self.gridLayout.addWidget(self.label_prezzo_acquisto, 19, 1, 1, 1)
        # NOME
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.label_nome.setFont(font)
        self.gridLayout.addWidget(self.label_nome, 7, 5, 1, 1)

        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 8, 5, 1, 1)
        # STATO
        self.comboBox_stato = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_stato.setObjectName("comboBox_stato")
        self.comboBox_stato.addItem("In arrivo")
        self.comboBox_stato.addItem("In negozio")
        self.comboBox_stato.addItem("Venduto")
        self.comboBox_stato.addItem("Reso")
        self.gridLayout.addWidget(self.comboBox_stato, 23, 1, 1, 1)

        self.label_stato = QtWidgets.QLabel(self.centralwidget)
        self.label_stato.setObjectName("label_stato")
        self.label_stato.setFont(font)
        self.gridLayout.addWidget(self.label_stato, 22, 1, 1, 1)
        # SCONTO CONSIGLIATO
        self.label_sconto_consigliato = QtWidgets.QLabel(self.centralwidget)
        self.label_sconto_consigliato.setObjectName("label_sconto_consigliato")
        self.label_sconto_consigliato.setFont(font)
        self.gridLayout.addWidget(self.label_sconto_consigliato, 22, 3, 1, 1)

        self.lineEdit_sconto_consigliato = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sconto_consigliato.setObjectName("lineEdit_sconto_consigliato")
        self.gridLayout.addWidget(self.lineEdit_sconto_consigliato, 23, 3, 1, 1)
        # MARCA
        self.label_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_marca.setObjectName("label_marca")
        self.label_marca.setFont(font)
        self.gridLayout.addWidget(self.label_marca, 7, 3, 1, 1)

        self.lineEdit_marca = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_marca.setObjectName("lineEdit_marca")
        self.gridLayout.addWidget(self.lineEdit_marca, 8, 3, 1, 1)
        # PREZZO VENDITA
        self.label_prezzo_vendita = QtWidgets.QLabel(self.centralwidget)
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.label_prezzo_vendita.setFont(font)
        self.gridLayout.addWidget(self.label_prezzo_vendita, 19, 3, 1, 1)

        self.lineEdit_prezzo_vendita = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prezzo_vendita.setObjectName("lineEdit_prezzo_vendita")
        self.gridLayout.addWidget(self.lineEdit_prezzo_vendita, 20, 3, 1, 1)

        # SPACER
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 24, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 9, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 15, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 21, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 18, 1, 1, 1)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    # Parte Dinamica


    def retranslateUi(self, MainWindow):
        index = 0
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modifica prodotto"))
        self.label_marca.setText(_translate("MainWindow", "Marca"))
        self.lineEdit_marca.setText(_translate("Form", str(self.prodotto.marca)))
        self.label_sconto.setText(_translate("MainWindow", "Sconto  (%)"))
        self.lineEdit_sconto.setText(_translate("Form", str(self.prodotto.sconto)))
        self.label_tipologia.setText(_translate("MainWindow", "Tipologia"))
        if self.prodotto.tipologia == "PA":
            index = self.comboBox_tipologia.findText("Pianoforti acustici", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "PD":
            index = self.comboBox_tipologia.findText("Pianoforti digitali", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "CE":
            index = self.comboBox_tipologia.findText("Chitarre elettriche", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "CA":
            index = self.comboBox_tipologia.findText("Chitarre acustiche", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "VI":
            index = self.comboBox_tipologia.findText("Violini", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "VE":
            index = self.comboBox_tipologia.findText("Viole", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "VC":
            index = self.comboBox_tipologia.findText("Violoncelli", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "BS":
            index = self.comboBox_tipologia.findText("Bassi", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "XL":
            index = self.comboBox_tipologia.findText("Xilofoni", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "MC":
            index = self.comboBox_tipologia.findText("Maracas", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "FT":
            index = self.comboBox_tipologia.findText("Flauti", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "FA":
            index = self.comboBox_tipologia.findText("Fiati ad ancia", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "OT":
            index = self.comboBox_tipologia.findText("Ottoni", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "OG":
            index = self.comboBox_tipologia.findText("Organi", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "AR":
            index = self.comboBox_tipologia.findText("Armoniche", QtCore.Qt.MatchFixedString)
        elif self.prodotto.tipologia == "ST":
            index = self.comboBox_tipologia.findText("Sintetizzatori", QtCore.Qt.MatchFixedString)
        self.comboBox_tipologia.setCurrentIndex(index)
        self.label_data_ordine.setText(_translate("MainWindow", "Data ordine"))
        data = self.prodotto.data_ordine
        data_split = data.split("/")
        self.dateEdit_data_ordine.setDate(QDate(int(data_split[2]), int(data_split[1]), int(data_split[0])))
        self.label_cod_fornitore.setText(_translate("MainWindow", "Codice fornitore"))
        self.lineEdit_cod_fornitore.setText(_translate("Form", str(self.prodotto.cod_fornitore)))
        self.label_cod_prodotto.setText(_translate("MainWindow", "Codice prodotto"))
        self.lineEdit_cod_prodotto.setText(_translate("Form", str(self.prodotto.cod_prodotto)))
        self.label_colore.setText(_translate("MainWindow", "Colore"))
        self.lineEdit_colore.setText(_translate("Form", str(self.prodotto.colore)))
        self.label_materiale.setText(_translate("MainWindow", "Materiale"))
        self.lineEdit_materiale.setText(_translate("Form", str(self.prodotto.materiale)))
        self.label_categoria.setText(_translate("MainWindow", "Categoria"))
        if self.prodotto.categoria == "Aerofoni":
            index = self.comboBox_categoria.findText("Aerofoni", QtCore.Qt.MatchFixedString)
        elif self.prodotto.categoria == "Cordofoni":
            index = self.comboBox_categoria.findText("Cordofoni", QtCore.Qt.MatchFixedString)
        elif self.prodotto.categoria == "Membranofoni":
            index = self.comboBox_categoria.findText("Membranofoni", QtCore.Qt.MatchFixedString)
        elif self.prodotto.categoria == "Idiofoni":
            index = self.comboBox_categoria.findText("Idiofoni", QtCore.Qt.MatchFixedString)
        elif self.prodotto.categoria == "Elettrofoni":
            index = self.comboBox_categoria.findText("Elettrofoni", QtCore.Qt.MatchFixedString)
        self.comboBox_categoria.setCurrentIndex(index)
        self.label_prezzo_acquisto.setText(_translate("MainWindow", "Prezzo di acquisto  (€)"))
        self.lineEdit_prezzo_acquisto.setText(_translate("Form", str(self.prodotto.prezzo_acquisto)))
        self.label_nome.setText(_translate("MainWindow", "Nome"))
        self.lineEdit_nome.setText(_translate("Form",str(self.prodotto.nome)))
        self.label_sconto_consigliato.setText(_translate("MainWindow", "Sconto consigliato  (%)"))
        self.lineEdit_sconto_consigliato.setText(_translate("Form", str(self.prodotto.sconto_consigliato)))
        self.label_cod_fattura.setText(_translate("MainWindow", "Codice fattura"))
        self.lineEdit_cod_fattura.setText(_translate("Form", str(self.prodotto.cod_fattura)))
        self.label_prezzo_vendita.setText(_translate("MainWindow", "Prezzo di vendita  (€)"))
        self.lineEdit_prezzo_vendita.setText(_translate("Form", str(self.prodotto.prezzo_vendita)))
        self.label_quantita.setText(_translate("MainWindow", "Quantità"))
        self.lineEdit_quantita.setText(_translate("Form", str(self.prodotto.quantita)))
        self.label_stato.setText(_translate("MainWindow", "Stato"))
        if self.prodotto.stato == "In arrivo":
            index = self.comboBox_stato.findText("In arrivo", QtCore.Qt.MatchFixedString)
        elif self.prodotto.stato == "In negozio":
            index = self.comboBox_stato.findText("In negozio", QtCore.Qt.MatchFixedString)
        elif self.prodotto.stato == "Venduto":
            index = self.comboBox_stato.findText("Venduto", QtCore.Qt.MatchFixedString)
        elif self.prodotto.stato == "Reso":
            index = self.comboBox_stato.findText("Reso", QtCore.Qt.MatchFixedString)
        self.comboBox_stato.setCurrentIndex(index)
        self.pushButton_annulla.setText(_translate("MainWindow", "Annulla"))
        self.pushButton_salva.setText(_translate("MainWindow", "Salva"))


    def controllo_click(self):
        if str(self.lineEdit_quantita.text()).isalpha() or str(self.lineEdit_sconto.text()).isalpha() or str(self.lineEdit_sconto_consigliato.text()).isalpha()\
                or str(self.lineEdit_prezzo_vendita.text()).isalpha() or str(self.lineEdit_prezzo_acquisto.text()).isalpha():
            self.popup_errore()
        else:
            self.salva_modifiche_click()

    def salva_modifiche_click(self):
        # prendo il testo che l'utente inserisce in ciascuna lineEdit
        cod_fattura = self.lineEdit_cod_fattura.text()
        cod_fornitore = self.lineEdit_cod_fornitore.text()
        aaaa = self.dateEdit_data_ordine.date().year()
        mm = self.dateEdit_data_ordine.date().month()
        gg = self.dateEdit_data_ordine.date().day()
        data_ordine = str(gg) + "/" + str(mm) + "/" + str(aaaa)
        cod_prodotto = self.lineEdit_cod_prodotto.text()
        marca = self.lineEdit_marca.text()
        nome = self.lineEdit_nome.text()
        '''
        if str(self.comboBox_tipologia.currentText()) == "Pianoforti acustici":
            tipologia = "PA"
        elif str(self.comboBox_tipologia.currentText()) == "Pianoforti digitali":
            tipologia = "PD"
        elif str(self.comboBox_tipologia.currentText()) == "Chitarre elettriche":
            tipologia = "CE"
        elif str(self.comboBox_tipologia.currentText()) == "Chitarre acustiche":
            tipologia = "CA"
        elif str(self.comboBox_tipologia.currentText()) == "Violini":
            tipologia = "VI"
        elif str(self.comboBox_tipologia.currentText()) == "Viole":
            tipologia = "VE"
        elif str(self.comboBox_tipologia.currentText()) == "Violoncelli":
            tipologia = "VC"
        elif str(self.comboBox_tipologia.currentText()) == "Bassi":
            tipologia = "BS"
        elif str(self.comboBox_tipologia.currentText()) == "Xilofoni":
            tipologia = "XL"
        elif str(self.comboBox_tipologia.currentText()) == "Maracas":
            tipologia = "MC"
        elif str(self.comboBox_tipologia.currentText()) == "Batterie":
            tipologia = "BT"
        elif str(self.comboBox_tipologia.currentText()) == "Flauti":
            tipologia = "FT"
        elif str(self.comboBox_tipologia.currentText()) == "Fiati ad ancia":
            tipologia = "FA"
        elif str(self.comboBox_tipologia.currentText()) == "Ottoni":
            tipologia = "OT"
        elif str(self.comboBox_tipologia.currentText()) == "Organi":
            tipologia = "OG"
        elif str(self.comboBox_tipologia.currentText()) == "Armoniche":
            tipologia = "AR"
        elif str(self.comboBox_tipologia.currentText()) == "Sintetizzatori":
            tipologia = "ST"'''
        tipologia = str(self.comboBox_tipologia.currentText())
        categoria = str(self.comboBox_categoria.currentText())
        materiale = self.lineEdit_materiale.text()
        colore = self.lineEdit_colore.text()
        quantita = self.lineEdit_quantita.text()
        prezzo_acquisto = self.lineEdit_prezzo_acquisto.text()
        prezzo_vendita = self.lineEdit_prezzo_vendita.text()
        stato = str(self.comboBox_stato.currentText())
        sconto_consigliato = self.lineEdit_sconto_consigliato.text()
        sconto = self.lineEdit_sconto.text()

        # modifico gli attributi del fornitore in base al testo inserito
        self.prodotto.cod_fornitore = cod_fornitore
        self.prodotto.cod_fattura = cod_fattura
        self.prodotto.data_ordine = data_ordine
        self.prodotto.cod_prodotto = cod_prodotto
        self.prodotto.marca = marca
        self.prodotto.nome = nome
        self.prodotto.categoria = categoria
        self.prodotto.tipologia = tipologia
        self.prodotto.materiale = materiale
        self.prodotto.colore = colore
        self.prodotto.quantita = quantita
        self.prodotto.prezzo_acquisto = prezzo_acquisto
        self.prodotto.prezzo_vendita = prezzo_vendita
        self.prodotto.stato = stato
        self.prodotto.sconto_consigliato = sconto_consigliato
        self.prodotto.sconto = sconto

        self.update_ui()
        self.close()

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("WARNING")
        msg.setText("Hai inserito dei dati non validi.\n\nInserire i dati corretti.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

