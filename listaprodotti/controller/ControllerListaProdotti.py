from listaprodotti.model.ListaProdotti import ListaProdotti


    # CONTROLLER DELLA LISTA DEI PRODOTTI
    
    # Tale file serve per gestire le funzionalità e i metodi principali del programma per quanto riguarda la gestione dei prodotti

class ControllerListaProdotti:
    def __init__(self):
        super(ControllerListaProdotti, self).__init__()
        self.model = ListaProdotti()

    def get_lista_prodotti(self):
        return self.model.get_lista_prodotti()

    def get_lista_marche(self):
        return self.model.get_lista_marche()
    
    def get_lista_nome(self):
        return self.model.get_lista_nome()
    
    def get_lista_categoria(self):
        return self.model.get_lista_categoria()
    
    def get_lista_tipologia(self):
        return self.model.get_lista_tipologia()

    def inserisci_prodotto(self, prodotto):
        self.model.inserisci_prodotto(prodotto)

    def get_prodotto_by_code(self, code):
        return self.model.get_prodotto_by_code(code)

    def get_nome_prodotto_by_code(self, codice):
        return self.model.get_nome_prodotto_by_code(codice)

    def elimina_prodotto_by_codice(self, codice_prodotto, lista_prodotti):
        self.model.elimina_prodotto_by_code(codice_prodotto, lista_prodotti)

    def elimina_prodotto(self, prodotto):
        self.model.elimina_prodotto(prodotto)

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()

    def save_data_specialized(self, lista_prodotti):
        self.model.save_data_specialized(lista_prodotti)