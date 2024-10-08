import os
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap

from prodotto.view.ViewModificaProdotto import ViewModificaProdotto


# Parametri gestiti dalla vista del prodotto


class ViewProdotto(QWidget):
    def __init__(self, prodotto, update_ui, controller, lista_prodotti, parent=None):
        super(ViewProdotto, self).__init__(parent)
        self.controller_lista_prodotti = controller
        self.update_ui = update_ui
        self.prodotto = prodotto
        self.lista_prodotti_filtrata = lista_prodotti
        self.setObjectName("MainWindow")
        self.resize(1173, 700)
        self.setStyleSheet("background-color: white;")

        # Gestione del font
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(22)
        font.setWeight(75)


    # Parte Statica


        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_dettagli_prodotto = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_dettagli_prodotto.setObjectName("groupBox_dettagli_prodotto")
        self.groupBox_dettagli_prodotto.setFont(font)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_dettagli_prodotto)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_data_ordine = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_data_ordine.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_ordine.setObjectName("label_data_ordine")
        self.label_data_ordine.setFont(font)
        self.gridLayout_3.addWidget(self.label_data_ordine, 0, 0, 1, 1)
        self.label_marca = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.label_marca.setObjectName("label_marca")
        self.label_marca.setFont(font)
        self.gridLayout_3.addWidget(self.label_marca, 0, 1, 1, 1)
        self.label_nome = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nome.setObjectName("label_nome")
        self.label_nome.setFont(font)
        self.gridLayout_3.addWidget(self.label_nome, 1, 0, 1, 1)
        self.label_categoria = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_categoria.setAlignment(QtCore.Qt.AlignCenter)
        self.label_categoria.setObjectName("label_categoria")
        self.label_categoria.setFont(font)
        self.gridLayout_3.addWidget(self.label_categoria, 1, 1, 1, 1)
        self.label_tipologia = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_tipologia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipologia.setObjectName("label_tipologia")
        self.label_tipologia.setFont(font)
        self.gridLayout_3.addWidget(self.label_tipologia, 2, 0, 1, 1)
        self.label_materiale = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_materiale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_materiale.setObjectName("label_materiale")
        self.label_materiale.setFont(font)
        self.gridLayout_3.addWidget(self.label_materiale, 2, 1, 1, 1)
        self.label_colore = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_colore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_colore.setObjectName("label_colore")
        self.label_colore.setFont(font)
        self.gridLayout_3.addWidget(self.label_colore, 3, 0, 1, 1)
        self.label_quantita = QtWidgets.QLabel(self.groupBox_dettagli_prodotto)
        self.label_quantita.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quantita.setObjectName("label_quantita")
        self.label_quantita.setFont(font)
        self.gridLayout_3.addWidget(self.label_quantita, 4, 0, 1, 1)
        
        self.gridLayout.addWidget(self.groupBox_dettagli_prodotto, 2, 1, 2, 2)
        # modifica button
        self.pushButton_modifica = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_modifica.setObjectName("pushButton_modifica")
        self.gridLayout.addWidget(self.pushButton_modifica, 5, 2, 1, 1)
        self.pushButton_modifica.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: black;\n""}")
        self.pushButton_modifica.clicked.connect(self.show_modifica_prodotto)
        # elimina button
        self.pushButton_elimina = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_elimina.setObjectName("pushButton_elimina")
        self.pushButton_elimina.setStyleSheet("QPushButton {\n"
                                              "    background-color:rgb(255, 0, 0);\n"
                                              "    color:white;\n"
                                              "}")
        self.gridLayout.addWidget(self.pushButton_elimina, 5, 1, 1, 1)
        self.pushButton_elimina.setStyleSheet("QPushButton {\n""   background-color: red;\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: black;\n""}")
        self.pushButton_elimina.clicked.connect(self.elimina_prodotto_click)
        # indetro button
        self.pushButton_indietro = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.gridLayout.addWidget(self.pushButton_indietro, 0, 0, 1, 1)
        self.pushButton_indietro.setStyleSheet("QPushButton {\n" "   background-color:white;\n" "   border-width: 2px;\n""   border-radius: 10px;\n""   border: 2px solid gray;\n""   font: bold 12px;\n""   padding: 6px;\n""}")
        self.pushButton_indietro.clicked.connect(self.close)
        # groupbox prezzi e sconti
        self.groupBox_prezzi_sconti = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_prezzi_sconti.setObjectName("groupBox_prezzi_sconti")
        self.groupBox_prezzi_sconti.setFont(font)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_prezzi_sconti)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_prezzo_acquisto = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_prezzo_acquisto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prezzo_acquisto.setObjectName("label_prezzo_acquisto")
        self.label_prezzo_acquisto.setFont(font)
        self.gridLayout_4.addWidget(self.label_prezzo_acquisto, 0, 0, 1, 1)
        self.label_prezzo_vendita = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_prezzo_vendita.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.label_prezzo_vendita.setFont(font)
        self.gridLayout_4.addWidget(self.label_prezzo_vendita, 0, 1, 1, 1)
        self.label_sconto = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_sconto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sconto.setObjectName("label_sconto")
        self.label_sconto.setFont(font)
        self.gridLayout_4.addWidget(self.label_sconto, 1, 0, 1, 1)
        self.label_sconto_consigliato = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_sconto_consigliato.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sconto_consigliato.setObjectName("label_sconto_consigliato")
        self.label_sconto_consigliato.setFont(font)
        self.gridLayout_4.addWidget(self.label_sconto_consigliato, 1, 1, 1, 1)
        self.label_stato = QtWidgets.QLabel(self.groupBox_prezzi_sconti)
        self.label_stato.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stato.setObjectName("label_stato")
        self.label_stato.setFont(font)
        self.gridLayout_4.addWidget(self.label_stato, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_prezzi_sconti, 4, 1, 1, 2)
        # groupbox codici prodotto
        self.groupBox_codici_prodotto = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_codici_prodotto.setObjectName("groupBox_codici_prodotto")
        self.groupBox_codici_prodotto.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_codici_prodotto)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_cod_fattura = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_fattura.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_fattura.setObjectName("label_cod_fattura")
        self.label_cod_fattura.setFont(font)
        self.gridLayout_2.addWidget(self.label_cod_fattura, 0, 0, 1, 1)
        self.label_cod_fornitore = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_fornitore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_fornitore.setObjectName("label_cod_fornitore")
        self.label_cod_fornitore.setFont(font)
        self.gridLayout_2.addWidget(self.label_cod_fornitore, 0, 1, 1, 1)
        self.label_cod_prodotto = QtWidgets.QLabel(self.groupBox_codici_prodotto)
        self.label_cod_prodotto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cod_prodotto.setObjectName("label_cod_prodotto")
        self.label_cod_prodotto.setFont(font)
        self.gridLayout_2.addWidget(self.label_cod_prodotto, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_codici_prodotto, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        # immagine prodotto
        self.immagine = QtWidgets.QWidget(self.widget_2)
        self.immagine.setObjectName("immagine")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.immagine)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.immagine)
        self.label.setObjectName("label_icon")
        if os.path.isfile('listaprodotti/data/images/' + str(self.prodotto.cod_prodotto) + '.jpg'):
            pixmap = QPixmap('listaprodotti/data/images/' + str(self.prodotto.cod_prodotto) + '.jpg')
        else:
            pixmap = QPixmap('listaprodotti/data/images/noimage.jpg')
        pixmap_scaled = pixmap.scaled(1100, 850, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap_scaled)
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout.addWidget(self.immagine, 1, 0, 4, 1)
        self.verticalLayout.addWidget(self.widget_2)

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


# Parte Dinamica


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prodotto"))
        self.groupBox_dettagli_prodotto.setTitle(_translate("MainWindow", "Dettagli prodotto"))
        self.label_data_ordine.setText(_translate("MainWindow", "Data dell\'ordine: " + str(self.prodotto.data_ordine)))
        self.label_marca.setText(_translate("MainWindow", "Marca: " + str(self.prodotto.marca)))
        self.label_nome.setText(_translate("MainWindow", "Nome: " + str(self.prodotto.nome)))
        self.label_categoria.setText(_translate("MainWindow", "Categoria: " + str(self.prodotto.categoria)))
        if str(self.prodotto.tipologia) == "PA":
            tipologia = "Pianoforti acustici"
        elif str(self.prodotto.tipologia) == "PD":
            tipologia = "Pianoforti digitali"
        elif str(self.prodotto.tipologia) == "CE":
            tipologia = "Chitarre elettriche"
        elif str(self.prodotto.tipologia) == "CA":
            tipologia = "Chitarre acustiche"
        elif str(self.prodotto.tipologia) == "VI":
            tipologia = "Violini"
        elif str(self.prodotto.tipologia) == "VE":
            tipologia = "Viole"
        elif str(self.prodotto.tipologia) == "VC":
            tipologia = "Violoncelli"
        elif str(self.prodotto.tipologia) == "BS":
            tipologia = "Bassi"
        elif str(self.prodotto.tipologia) == "XL":
            tipologia = "Xilofoni"
        elif str(self.prodotto.tipologia) == "MC":
            tipologia = "Maracas"
        elif str(self.prodotto.tipologia) == "BT":
            tipologia = "Batterie"
        elif str(self.prodotto.tipologia) == "FT":
            tipologia = "Flauti"
        elif str(self.prodotto.tipologia) == "FA":
            tipologia = "Fiati ad ancia"
        elif str(self.prodotto.tipologia) == "OT":
            tipologia = "Ottoni"
        elif str(self.prodotto.tipologia) == "OG":
            tipologia = "Organi"
        elif str(self.prodotto.tipologia) == "AR":
            tipologia = "Armoniche"
        elif str(self.prodotto.tipologia) == "ST":
            tipologia = "Sintetizzatori"
        self.label_tipologia.setText(_translate("MainWindow", "Tipologia: " + str(self.prodotto.tipologia)))
        self.label_materiale.setText(_translate("MainWindow", "Materiale: " + str(self.prodotto.materiale)))
        self.label_colore.setText(_translate("MainWindow", "Colore: " + str(self.prodotto.colore)))
        self.label_quantita.setText(_translate("MainWindow", "Quantità: " + str(self.prodotto.quantita)))
        self.pushButton_modifica.setText(_translate("MainWindow", "Modifica"))
        self.pushButton_indietro.setText(_translate("MainWindow", "< Indietro"))
        self.groupBox_prezzi_sconti.setTitle(_translate("MainWindow", "Prezzi e sconti"))
        self.label_prezzo_acquisto.setText(_translate("MainWindow", "Prezzo di acquisto: " + str(self.prodotto.prezzo_acquisto)))
        self.label_prezzo_vendita.setText(_translate("MainWindow", "Prezzo di vendita: " + str(self.prodotto.prezzo_vendita)))
        self.label_sconto.setText(_translate("MainWindow", "Sconto: " + str(self.prodotto.sconto)))
        self.label_sconto_consigliato.setText(_translate("MainWindow", "Sconto consigliato: " + str(self.prodotto.sconto_consigliato)))
        self.label_stato.setText(_translate("MainWindow", "Stato: " + str(self.prodotto.stato)))
        self.pushButton_elimina.setText(_translate("MainWindow", "Elimina"))
        self.groupBox_codici_prodotto.setTitle(_translate("MainWindow", "Codici prodotto"))
        self.label_cod_fattura.setText(_translate("MainWindow", "Codice fattura: " + str(self.prodotto.cod_fattura)))
        self.label_cod_fornitore.setText(_translate("MainWindow", "Codice fornitore: " + str(self.prodotto.cod_fornitore)))
        self.label_cod_prodotto.setText(_translate("MainWindow", "Codice prodotto: " + str(self.prodotto.cod_prodotto)))

   # Eventi per gestire i click dei vari bottoni

    def elimina_prodotto_click(self):
        print("QUI")
        self.controller_lista_prodotti.elimina_prodotto_by_codice(self.prodotto.cod_prodotto, self.lista_prodotti_filtrata)
        self.update_ui()
        self.close()

    def show_modifica_prodotto(self):
        self.view_modifica_prodotto = ViewModificaProdotto(self.controller_lista_prodotti, self.update_ui, self.prodotto)
        self.view_modifica_prodotto.showMaximized()
        time.sleep(0.3)
        self.close()