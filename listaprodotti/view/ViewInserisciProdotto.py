from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QMessageBox
from prodotto.model.Prodotto import Prodotto
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini

# Inserimento di un nuovo dato all'interno del database

class ViewInserisciProdotto(QWidget):
    def __init__(self, controller_lista_prodotti, update_ui, inserimento_da_ordine, lista_prodotti_ordine,
                 lista_prodotti_filtrata, ordine):
        super(ViewInserisciProdotto, self).__init__()
        self.controller_lista_prodotti = controller_lista_prodotti
        self.controller_lista_ordini = ControllerListaOrdini()

        self.inserimento_da_ordine = inserimento_da_ordine
        self.lista_prodotti_ordine = lista_prodotti_ordine
        self.lista_prodotti_filtrata = lista_prodotti_filtrata
        self.update_ui = update_ui
        self.ordine = ordine


    # Parte Statica


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.setObjectName("Form")
        self.resize(370, 643)
        self.setStyleSheet("background-color: white;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -102, 331, 1012))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(300, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        if not self.inserimento_da_ordine:
            self.label_codice_fattura = QtWidgets.QLabel(self.widget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_codice_fattura.sizePolicy().hasHeightForWidth())
            self.label_codice_fattura.setSizePolicy(sizePolicy)
            self.label_codice_fattura.setMinimumSize(QtCore.QSize(0, 20))
            self.label_codice_fattura.setObjectName("label_codice_fattura")
            self.verticalLayout_3.addWidget(self.label_codice_fattura)
            self.lineEdit_codice_fattura = QtWidgets.QLineEdit(self.widget)
            self.lineEdit_codice_fattura.setMinimumSize(QtCore.QSize(0, 0))
            self.lineEdit_codice_fattura.setObjectName("lineEdit_codice_fattura")
            self.verticalLayout_3.addWidget(self.lineEdit_codice_fattura)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem)
            self.label_codice_fornitore = QtWidgets.QLabel(self.widget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_codice_fornitore.sizePolicy().hasHeightForWidth())
            self.label_codice_fornitore.setSizePolicy(sizePolicy)
            self.label_codice_fornitore.setMinimumSize(QtCore.QSize(0, 20))
            self.label_codice_fornitore.setObjectName("label_codice_fornitore")
            self.verticalLayout_3.addWidget(self.label_codice_fornitore)
            self.lineEdit_codice_fornitore = QtWidgets.QLineEdit(self.widget)
            self.lineEdit_codice_fornitore.setObjectName("lineEdit_codice_fornitore")
            self.verticalLayout_3.addWidget(self.lineEdit_codice_fornitore)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem1)
            self.label_data_ordine = QtWidgets.QLabel(self.widget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_data_ordine.sizePolicy().hasHeightForWidth())
            self.label_data_ordine.setSizePolicy(sizePolicy)
            self.label_data_ordine.setMinimumSize(QtCore.QSize(0, 20))
            self.label_data_ordine.setObjectName("label_data_ordine")
            self.verticalLayout_3.addWidget(self.label_data_ordine)
            self.dateEdit_ordine = QtWidgets.QDateEdit(self.widget)
            self.dateEdit_ordine.setObjectName("dateEdit_ordine")
            self.verticalLayout_3.addWidget(self.dateEdit_ordine)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_codice_prodotto = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_codice_prodotto.sizePolicy().hasHeightForWidth())
        self.label_codice_prodotto.setSizePolicy(sizePolicy)
        self.label_codice_prodotto.setMinimumSize(QtCore.QSize(0, 20))
        self.label_codice_prodotto.setObjectName("label_codice_prodotto")
        self.verticalLayout_3.addWidget(self.label_codice_prodotto)
        self.lineEdit_codice_prodotto = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_codice_prodotto.setObjectName("lineEdit_codice_prodotto")
        self.verticalLayout_3.addWidget(self.lineEdit_codice_prodotto)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)

        self.label_marca = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_codice_prodotto.sizePolicy().hasHeightForWidth())
        self.label_marca.setSizePolicy(sizePolicy)
        self.label_marca.setMinimumSize(QtCore.QSize(0, 20))
        self.label_marca.setObjectName("label_marca")
        self.verticalLayout_3.addWidget(self.label_marca)
        self.lineEdit_marca = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_marca.setObjectName("lineEdit_marca")
        self.verticalLayout_3.addWidget(self.lineEdit_marca)
        spacerItem_marca = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem_marca)

        self.label_nome = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome.sizePolicy().hasHeightForWidth())
        self.label_nome.setSizePolicy(sizePolicy)
        self.label_nome.setMinimumSize(QtCore.QSize(0, 20))
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout_3.addWidget(self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.verticalLayout_3.addWidget(self.lineEdit_nome)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_categoria = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_categoria.sizePolicy().hasHeightForWidth())
        self.label_categoria.setSizePolicy(sizePolicy)
        self.label_categoria.setMinimumSize(QtCore.QSize(0, 20))
        self.label_categoria.setObjectName("label_categoria")
        self.verticalLayout_3.addWidget(self.label_categoria)
        self.comboBox_categoria = QtWidgets.QComboBox(self.widget)
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_categoria)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_tipologia = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tipologia.sizePolicy().hasHeightForWidth())
        self.label_tipologia.setSizePolicy(sizePolicy)
        self.label_tipologia.setMinimumSize(QtCore.QSize(0, 20))
        self.label_tipologia.setObjectName("label_tipologia")
        self.verticalLayout_3.addWidget(self.label_tipologia)
        self.comboBox_tipologia = QtWidgets.QComboBox(self.widget)
        self.comboBox_tipologia.setObjectName("comboBox_tipologia")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.comboBox_tipologia.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_tipologia)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.label_materiale = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_materiale.sizePolicy().hasHeightForWidth())
        self.label_materiale.setSizePolicy(sizePolicy)
        self.label_materiale.setMinimumSize(QtCore.QSize(0, 20))
        self.label_materiale.setObjectName("label_materiale")
        self.verticalLayout_3.addWidget(self.label_materiale)
        self.lineEdit_materiale = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_materiale.setObjectName("lineEdit_materiale")
        self.verticalLayout_3.addWidget(self.lineEdit_materiale)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_colore = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_colore.sizePolicy().hasHeightForWidth())
        self.label_colore.setSizePolicy(sizePolicy)
        self.label_colore.setMinimumSize(QtCore.QSize(0, 20))
        self.label_colore.setObjectName("label_colore")
        self.verticalLayout_3.addWidget(self.label_colore)
        self.lineEdit_colore = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_colore.setObjectName("lineEdit_colore")
        self.verticalLayout_3.addWidget(self.lineEdit_colore)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.label_quantita = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_quantita.sizePolicy().hasHeightForWidth())
        self.label_quantita.setSizePolicy(sizePolicy)
        self.label_quantita.setMinimumSize(QtCore.QSize(0, 20))
        self.label_quantita.setObjectName("label_quantita")
        self.verticalLayout_3.addWidget(self.label_quantita)
        self.lineEdit_quantita = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_quantita.setObjectName("lineEdit_quantita")
        self.verticalLayout_3.addWidget(self.lineEdit_quantita)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.label_prezzo_acquisto = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prezzo_acquisto.sizePolicy().hasHeightForWidth())
        self.label_prezzo_acquisto.setSizePolicy(sizePolicy)
        self.label_prezzo_acquisto.setMinimumSize(QtCore.QSize(0, 20))
        self.label_prezzo_acquisto.setObjectName("label_prezzo_acquisto")
        self.verticalLayout_3.addWidget(self.label_prezzo_acquisto)
        self.lineEdit_prezzo_acquisto = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_prezzo_acquisto.setObjectName("lineEdit_prezzo_acquisto")
        self.verticalLayout_3.addWidget(self.lineEdit_prezzo_acquisto)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.label_prezzo_vendita = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prezzo_vendita.sizePolicy().hasHeightForWidth())
        self.label_prezzo_vendita.setSizePolicy(sizePolicy)
        self.label_prezzo_vendita.setMinimumSize(QtCore.QSize(0, 20))
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.verticalLayout_3.addWidget(self.label_prezzo_vendita)
        self.lineEdit_prezzo_vendita = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_prezzo_vendita.setObjectName("lineEdit_prezzo_vendita")
        self.verticalLayout_3.addWidget(self.lineEdit_prezzo_vendita)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)

        if not self.inserimento_da_ordine:
            self.label_stato = QtWidgets.QLabel(self.widget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_stato.sizePolicy().hasHeightForWidth())
            self.label_stato.setSizePolicy(sizePolicy)
            self.label_stato.setMinimumSize(QtCore.QSize(0, 20))
            self.label_stato.setObjectName("label_stato")
            self.verticalLayout_3.addWidget(self.label_stato)
            self.comboBox_stato = QtWidgets.QComboBox(self.widget)
            self.comboBox_stato.setObjectName("comboBox_stato")
            self.comboBox_stato.addItem("")
            self.comboBox_stato.addItem("")
            self.comboBox_stato.addItem("")
            self.comboBox_stato.addItem("")
            self.verticalLayout_3.addWidget(self.comboBox_stato)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.label_sconto_consigliato = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sconto_consigliato.sizePolicy().hasHeightForWidth())
        self.label_sconto_consigliato.setSizePolicy(sizePolicy)
        self.label_sconto_consigliato.setMinimumSize(QtCore.QSize(0, 20))
        self.label_sconto_consigliato.setObjectName("label_sconto_consigliato")
        self.verticalLayout_3.addWidget(self.label_sconto_consigliato)
        self.lineEdit_sconto_consigliato = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_sconto_consigliato.setObjectName("lineEdit_sconto_consigliato")
        self.verticalLayout_3.addWidget(self.lineEdit_sconto_consigliato)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.label_sconto = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sconto.sizePolicy().hasHeightForWidth())
        self.label_sconto.setSizePolicy(sizePolicy)
        self.label_sconto.setMinimumSize(QtCore.QSize(0, 20))
        self.label_sconto.setObjectName("label_sconto")
        self.verticalLayout_3.addWidget(self.label_sconto)
        self.lineEdit_sconto = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_sconto.setObjectName("lineEdit_sconto")
        self.verticalLayout_3.addWidget(self.lineEdit_sconto)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem15)
        self.pushButton_salva = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_salva.sizePolicy().hasHeightForWidth())
        self.pushButton_salva.setSizePolicy(sizePolicy)
        self.pushButton_salva.setMinimumSize(QtCore.QSize(350, 0))
        self.pushButton_salva.setObjectName("pushButton_salva")
        self.pushButton_salva.clicked.connect(self.controllo_click)
        self.verticalLayout.addWidget(self.pushButton_salva)
        self.pushButton_salva.setStyleSheet("QPushButton {\n"
                                               "   background-color: rgb(26, 218, 108);\n"
                                               "   border-width: 2px;\n"
                                               "   border-radius: 10px;\n"
                                               "   font: bold 12px;\n"
                                               "   padding: 6px;\n"
                                               "   color: black;\n"
                                               "}")
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi()
        self.setWindowTitle("Inserisci prodotto")
        QtCore.QMetaObject.connectSlotsByName(self)


    # Parte Dinamica


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_codice_prodotto.setText(_translate("Form", "Codice strumento"))
        self.label_marca.setText(_translate("Form", "Marca"))
        self.label_nome.setText(_translate("Form", "Nome"))
        self.label_categoria.setText(_translate("Form", "Categoria"))
        self.comboBox_categoria.setItemText(0, _translate("Form", "Aerofoni"))
        self.comboBox_categoria.setItemText(1, _translate("Form", "Cordofoni"))
        self.comboBox_categoria.setItemText(2, _translate("Form", "Membranofoni"))
        self.comboBox_categoria.setItemText(3, _translate("Form", "Idiofoni"))
        self.comboBox_categoria.setItemText(4, _translate("Form", "Elettrofoni"))
        self.label_tipologia.setText(_translate("Form", "Tipologia"))
        self.comboBox_tipologia.setItemText(0, _translate("Form", "Pianoforti acustici"))
        self.comboBox_tipologia.setItemText(1, _translate("Form", "Pianoforti digitali"))
        self.comboBox_tipologia.setItemText(2, _translate("Form", "Chitarre elettriche"))
        self.comboBox_tipologia.setItemText(3, _translate("Form", "Chitarre acustiche"))
        self.comboBox_tipologia.setItemText(4, _translate("Form", "Violini"))
        self.comboBox_tipologia.setItemText(5, _translate("Form", "Viole"))
        self.comboBox_tipologia.setItemText(6, _translate("Form", "Violoncelli"))
        self.comboBox_tipologia.setItemText(7, _translate("Form", "Bassi"))
        self.comboBox_tipologia.setItemText(8, _translate("Form", "Xilofoni"))
        self.comboBox_tipologia.setItemText(9, _translate("Form", "Maracas"))
        self.comboBox_tipologia.setItemText(10, _translate("Form", "Batterie"))
        self.comboBox_tipologia.setItemText(11, _translate("Form", "Flauti"))
        self.comboBox_tipologia.setItemText(12, _translate("Form", "Fiati ad ancia"))
        self.comboBox_tipologia.setItemText(13, _translate("Form", "Ottoni"))
        self.comboBox_tipologia.setItemText(14, _translate("Form", "Organi"))
        self.comboBox_tipologia.setItemText(15, _translate("Form", "Armoniche"))
        self.comboBox_tipologia.setItemText(16, _translate("Form", "Sintetizzatori"))
        self.label_materiale.setText(_translate("Form", "Materiale"))
        self.label_colore.setText(_translate("Form", "Colore"))
        self.label_quantita.setText(_translate("Form", "Quantità"))
        self.label_prezzo_acquisto.setText(_translate("Form", "Prezzo d\'acquisto"))
        self.label_prezzo_vendita.setText(_translate("Form", "Prezzo di vendita"))

        if not self.inserimento_da_ordine:
            self.label_codice_fattura.setText(_translate("Form", "Codice fattura"))
            self.label_codice_fornitore.setText(_translate("Form", "Codice fornitore"))
            self.label_data_ordine.setText(_translate("Form", "Data ordine"))
            self.label_stato.setText(_translate("Form", "Stato"))
            self.comboBox_stato.setItemText(0, _translate("Form", "In arrivo"))
            self.comboBox_stato.setItemText(1, _translate("Form", "In negozio"))
            self.comboBox_stato.setItemText(2, _translate("Form", "Venduto"))
            self.comboBox_stato.setItemText(3, _translate("Form", "Reso"))
        self.label_sconto_consigliato.setText(_translate("Form", "Sconto consigliato (%)"))
        self.label_sconto.setText(_translate("Form", "Sconto (%)"))
        self.pushButton_salva.setText(_translate("Form", "Salva"))

        # Controlli generali sui click

    def controllo_click(self):
        if False:
            self.popup_errore()
        elif str(self.lineEdit_quantita.text()).isalpha() or str(self.lineEdit_sconto.text()).isalpha() or str(self.lineEdit_sconto_consigliato.text()).isalpha()\
                or str(self.lineEdit_prezzo_vendita.text()).isalpha() or str(self.lineEdit_prezzo_acquisto.text()).isalpha():
            self.popup_errore()
        else:
            self.salva_modifiche_click()

    def salva_modifiche_click(self):
        if int(self.lineEdit_quantita.text()) == 0:
            QMessageBox.critical(self, 'Errore', 'Il campo quantità non può essere nullo.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        # il testo inserito dall'utente viene salvato in variabili in ciascuna lineEdit
        if not self.inserimento_da_ordine:
            cod_fattura = self.lineEdit_codice_fattura.text()
            cod_fornitore = self.lineEdit_codice_fornitore.text()
            aaaa = self.dateEdit_ordine.date().year()
            mm = self.dateEdit_ordine.date().month()
            gg = self.dateEdit_ordine.date().day()
            data_ordine = str(gg) + "/" + str(mm) + "/" + str(aaaa)
            cod_prodotto = self.lineEdit_codice_prodotto.text()
            marca = self.lineEdit_marca.text()
            nome = self.lineEdit_nome.text()
            categoria = str(self.comboBox_categoria.currentText())
            tipologia = str(self.comboBox_tipologia.currentText())
            '''if str(self.comboBox_tipologia.currentText()) == "Pianoforti acustici":
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
                tipologia = "TB"
            elif str(self.comboBox_tipologia.currentText()) == "Organi":
                tipologia = "OG"
            elif str(self.comboBox_tipologia.currentText()) == "Armoniche":
                tipologia = "AR"
            elif str(self.comboBox_tipologia.currentText()) == "Sintetizzatori":
                tipologia = "ST"'''
            materiale = self.lineEdit_materiale.text()
            colore = self.lineEdit_colore.text()
            quantita = self.lineEdit_quantita.text()
            prezzo_acquisto = self.lineEdit_prezzo_acquisto.text()
            prezzo_vendita = self.lineEdit_prezzo_vendita.text()
            stato = str(self.comboBox_stato.currentText())
            sconto_consigliato = self.lineEdit_sconto_consigliato.text()
            sconto = self.lineEdit_sconto.text()

            # aggiunta prodotto ad un ordine esistente
            prodotto = Prodotto(cod_fattura, cod_fornitore, data_ordine, cod_prodotto, marca, nome, categoria, tipologia,
                                materiale, colore, quantita,
                                prezzo_acquisto, prezzo_vendita, stato,
                                sconto_consigliato, sconto, "")

            self.controller_lista_prodotti.inserisci_prodotto(prodotto)
            self.lista_prodotti_filtrata.append(prodotto)
        else:
            cod_prodotto = self.lineEdit_codice_prodotto.text()
            marca = self.lineEdit_marca.text()
            nome = self.lineEdit_nome.text()
            categoria = str(self.comboBox_categoria.currentText())
            tipologia = str(self.comboBox_tipologia.currentText())
            '''if str(self.comboBox_tipologia.currentText()) == "Pianoforti acustici":
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
                tipologia = "TB"
            elif str(self.comboBox_tipologia.currentText()) == "Organi":
                tipologia = "OG"
            elif str(self.comboBox_tipologia.currentText()) == "Armoniche":
                tipologia = "AR"
            elif str(self.comboBox_tipologia.currentText()) == "Sintetizzatori":
                tipologia = "ST"'''
            materiale = self.lineEdit_materiale.text()
            colore = self.lineEdit_colore.text()
            quantita = self.lineEdit_quantita.text()
            prezzo_acquisto = self.lineEdit_prezzo_acquisto.text()
            prezzo_vendita = self.lineEdit_prezzo_vendita.text()
            sconto_consigliato = self.lineEdit_sconto_consigliato.text()
            sconto = self.lineEdit_sconto.text()

            prodotto = Prodotto(self.ordine.cod_fattura, self.ordine.cod_fornitore, None, cod_prodotto, marca, nome,
                                categoria, tipologia, materiale, colore, quantita, prezzo_acquisto, prezzo_vendita,
                                None, None, sconto_consigliato, sconto, "")
            self.lista_prodotti_ordine.append(prodotto)

        self.update_ui()
        self.close()

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("WARNING")
        msg.setText("Hai inserito dei dati non validi! \n\nInserire dati corretti.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()
