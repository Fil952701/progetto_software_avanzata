from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale
from listadelpersonale.view.ViewInserisciUtente import ViewInserisciUtente
from utente.view.ViewUtente import ViewUtente


class ViewListaDelPersonale(QWidget):
    def __init__(self):
        super(ViewListaDelPersonale, self).__init__()

        self.controller_lista_del_personale = ControllerListaDelPersonale()
        # variabili flag che mi permettono di verificare se sto visualizzando lista utenti amministratori o dipendenti
        self.dipendente = False
        self.amministratore = False
        self.lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()

        # Lista: E' una copia della lista reale. Mi permette di manipolare i suoi elementi senza modificare la lista originale (lista di riferimento)
        self.lista_dinamica = self.lista_del_personale[:]


    # Parte Statica


        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        # Come già visto precedentemente, modalità per prendere le dimensioni dello schermo
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.setObjectName("Form")
        self.resize(1121, 576)
        self.setStyleSheet("background-color: white;")
        #Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_apri = QtWidgets.QPushButton(self)
        self.pushButton_apri.setObjectName("pushButton_apri")
        self.pushButton_apri.clicked.connect(self.show_utente)
        self.verticalLayout_2.addWidget(self.pushButton_apri)
        self.pushButton_apri.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 218, 108);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: black;\n""}")
        self.pushButton_nuovo = QtWidgets.QPushButton(self)
        self.pushButton_nuovo.setObjectName("pushButton_nuovo")
        self.pushButton_nuovo.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.pushButton_nuovo.clicked.connect(self.show_inserisci_utente)
        self.verticalLayout_2.addWidget(self.pushButton_nuovo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 7, 1, 1)
        self.lineEdit_cerca = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_cerca.sizePolicy().hasHeightForWidth())
        self.lineEdit_cerca.setSizePolicy(sizePolicy)
        self.lineEdit_cerca.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_cerca.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_cerca.setFont(font)
        self.lineEdit_cerca.setClearButtonEnabled(False)
        self.lineEdit_cerca.setObjectName("lineEdit_cerca")
        self.lineEdit_cerca.setPlaceholderText("Cerca per codice")
        self.lineEdit_cerca.returnPressed.connect(self.filter_cerca)
        self.gridLayout.addWidget(self.lineEdit_cerca, 2, 6, 1, 1)
        self.lineEdit_cerca.setStyleSheet("QLineEdit {\n"
                                 "   border-width: 2px;\n"
                                 "   border-radius: 10px;\n"
                                 "   border: 2px solid gray;\n"
                                 "   font: 12px;\n"
                                 "   padding: 6px;\n"
                                 "}")
        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setMinimumSize(QtCore.QSize(200, 0))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.jpg')
        self.label_logo.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_logo, 1, 4, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 3, 1)
        self.pushButton_indietro = QtWidgets.QPushButton(self)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.pushButton_indietro.clicked.connect(self.close)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_home.jpg'))
        self.pushButton_indietro.setIcon(icon)
        self.pushButton_indietro.setIconSize(QSize(50, 50))
        self.gridLayout.addWidget(self.pushButton_indietro, 1, 1, 1, 1)
        self.pushButton_indietro.setStyleSheet("QPushButton {\n"
                                               "   background-color:white;\n"
                                               "   border-width: 2px;\n"
                                               "   border-radius: 10px;\n"
                                               "   font: 12px;\n"
                                               "   padding: 6px;\n"
                                               "   color: black\n"
                                               "}")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 7, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setColumnWidth(0, int(self.width/10))
        self.tableWidget.setColumnWidth(1, int(self.width/6.8))
        self.tableWidget.setColumnWidth(2, int(self.width/6.8))
        self.tableWidget.setColumnWidth(3, int(self.width/6.8))
        self.tableWidget.setColumnWidth(4, int(self.width/6.8))
        self.tableWidget.setColumnWidth(5, int(self.width/6.8))
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 6)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 7)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        self.pushButton_stato1 = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setWeight(50)
        self.pushButton_stato1.setFont(font)
        self.pushButton_stato1.setObjectName("pushButton_stato1")
        self.pushButton_stato1.clicked.connect(self.filter_dipendente)
        self.gridLayout_3.addWidget(self.pushButton_stato1, 0, 1, 1, 1)
        self.pushButton_stato1.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""min-width: 80px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 2, 1, 1)
        self.pushButton_stato2 = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_stato2.setFont(font)
        self.pushButton_stato2.setObjectName("pushButton_stato2")
        self.pushButton_stato2.clicked.connect(self.filter_amministratore)
        self.gridLayout_3.addWidget(self.pushButton_stato2, 0, 3, 1, 1)
        self.pushButton_stato2.setStyleSheet("QPushButton {\n""   background-color: rgb(218, 108, 26);\n""   border-width: 2px;\n""min-width: 80px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: black;\n""}")
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 4, 1, 1)
        self.pushButton_all = QtWidgets.QPushButton(self)
        self.pushButton_all.setObjectName("pushButton_all")
        self.pushButton_all.clicked.connect(self.filter_all)
        self.gridLayout_3.addWidget(self.pushButton_all, 0, 5, 1, 1)
        self.pushButton_all.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""min-width: 80px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.gridLayout.addLayout(self.gridLayout_3, 3, 1, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 7)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 5, 3, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        self.setWindowTitle("Area del personale")


    # Parte Dinamica


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_apri.setText(_translate("Form", "Apri"))
        self.pushButton_nuovo.setText(_translate("Form", "Nuovo"))
        self.pushButton_stato1.setText(_translate("Form", "Dipendente"))
        self.pushButton_stato2.setText(_translate("Form", "Amministratore"))
        self.pushButton_all.setText(_translate("Form", "All"))

        # imposto le colonne della tabella contenente ogni record della lista del personale
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cognome"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ruolo"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Telefono"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Data scadenza contratto"))

        # inserisco gli elementi in tabella
        row=0
        self.tableWidget.setColumnCount(6)
        # chiamo il filtro generale prima di visualizzare gli elementi in tabella -> grazie ad A visualizzo amministratore
        if self.dipendente or self.amministratore:
            self.filter()
        self.tableWidget.setRowCount(len(self.lista_dinamica))
        for utente in self.lista_dinamica:
            item = QTableWidgetItem(str(utente.cod_utente))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(utente.nome))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(utente.cognome))
            if utente.ruolo=="A":
                ruolo= "Amministratore"
            else:
                ruolo= "Dipendente"

            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(ruolo))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(utente.telefono)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(utente.data_scadenza_contratto))

            row= row+1

    def show_inserisci_utente(self):
        self.view_inserisci_utente= ViewInserisciUtente(self.controller_lista_del_personale, self.retranslateUi, self.lista_dinamica)
        self.view_inserisci_utente.show()

    def show_utente(self):
        if (len(self.tableWidget.selectedIndexes()) > 0):
            selected = self.tableWidget.selectedIndexes()[0].row()
            utente_selezionato = self.lista_dinamica[selected]
            self.view_utente = ViewUtente(utente_selezionato, self.retranslateUi, self.controller_lista_del_personale, self.lista_dinamica)
            self.view_utente.show()

    # Filtro generale filter() per filtrare utenti amministratori
    def filter_amministratore(self):
        self.amministratore = True
        self.dipendente = False
        self.lista_del_personale= self.controller_lista_del_personale.get_lista_del_personale()
        self.lista_dinamica= self.lista_del_personale[:]
        self.filter()
        self.retranslateUi()

    # Filtro generale filter() per filtrare utenti dipendenti
    def filter_dipendente(self):
        self.amministratore= False
        self.dipendente= True
        self.lista_del_personale= self.controller_lista_del_personale.get_lista_del_personale()
        self.lista_dinamica = self.lista_del_personale[:]
        self.filter()
        self.retranslateUi()

    # Filtro generale filter() per visualizzare tutti gli utenti
    def filter_all(self):
        self.dipendente= False
        self.amministratore= False
        self.lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()
        self.lista_dinamica = self.lista_del_personale[:]
        self.filter()
        self.retranslateUi()

    # Filtra per tutti gli utenti con cod_utente contenente il testo immesso
    def filter_cerca(self):
        self.lista_del_personale = self.controller_lista_del_personale.get_lista_del_personale()
        self.lista_dinamica = self.lista_del_personale[:]
        codice_cerca= self.lineEdit_cerca.text()
        codice_cerca= codice_cerca.upper()
        elementi_da_rimuovere = []
        for utente in self.lista_dinamica:
            cod_utente= str(utente.cod_utente)
            cod_utente= cod_utente.upper()
            if not (codice_cerca in cod_utente):
                elementi_da_rimuovere.append(utente)
        for utente in elementi_da_rimuovere:
            if utente in self.lista_dinamica:
                self.lista_dinamica.remove(utente)
        self.retranslateUi()

    # Filtro generale, svolge più filtraggi tramite wrapping
    def filter(self):
        elementi_da_rimuovere = []

        if self.dipendente:
            for utente in self.lista_dinamica:
                if str(utente.ruolo) != "D":
                    elementi_da_rimuovere.append(utente)
            for utente in elementi_da_rimuovere:
                if utente in self.lista_dinamica:
                    self.lista_dinamica.remove(utente)
            return

        if self.amministratore:
            for utente in self.lista_dinamica:
                if str(utente.ruolo)!= "A":
                    elementi_da_rimuovere.append(utente)
            for utente in elementi_da_rimuovere:
                if utente in self.lista_dinamica:
                    self.lista_dinamica.remove(utente)
            return
        else:
            self.lista_del_personale= self.controller_lista_del_personale.get_lista_del_personale()
            self.lista_dinamica= self.lista_del_personale[:]
            return

    def closeEvent(self, event):
        self.controller_lista_del_personale.save_data()

