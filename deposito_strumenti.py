from csv import reader

# classe dedicata allo strumento
class Strumento:
    def __init__(self, codice, tipo, marca,anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)

    # restituisce una stringa formattata quando si utilizza print(strumento)
    def __str__(self):
        return f"[{self.codice}] {self.tipo} - {self.marca} - {self.anno_acquisto} - {self.valore}"

    # l'oggetto (strumento) presenta la stessa rappresentazione quando si trova dentro una lista
    def __repr__(self):
        return self.__str__()


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = [] # creo una lista di strumenti


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            filein = open(file_path, "r") # apertura file
            file_read = reader(filein)

            for riga in file_read:
                # si utilizza la classe che abbiamo creato per lo strumento
                nuovo_strumento = Strumento(riga[0],riga[1],riga[2],riga[3],riga[4])
                # letto una strumento per volta, lo si aggiunge alla lista che abbiamo definto nella funzione __init__()
                self.strumenti.append(nuovo_strumento)

            filein.close() # chiusura file

        except FileNotFoundError: # eccezione
            print("File non trovato!")

#  il metodo aggiungi_strumento(tipo, marca, anno_acquisto, valore),
    #  che riceve come parametri il tipo dello strumento, la marca,
    #  l'anno di acquisto e il valore. Il metodo crea e inserisce un
    #  nuovo oggetto strumento nel sistema (assegnandogli automaticamente
    #  un . Il metodo deve restituire il riferimento
    #  allo strumento aggiunto.

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        # codice univoco formato dalla lettera S seguita da un numero intero progressivo,
        #  calcolato a partire dall'ultimo identificativo già presente nel sistema)

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
