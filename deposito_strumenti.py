from csv import reader
from operator import attrgetter

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
        self.prestiti = {} # dizionario dove vengono salvati i prestiti attivi
        self.contatore_prestiti = 0 # tiene conto del numero di prestiti effettuati


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


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        # controllo che ci sia almeno uno strumento nella lista
        if len(self.strumenti) > 0:
            # prende l'ultimo codice --> contiene per esempio: S10 (ultimo codice del file csv)
            ultimo_codice = self.strumenti[-1].codice
            ultimo_numero = int(ultimo_codice[1:]) # prende l'ultimo numero --> esempio: 10
            nuovo_numero = ultimo_numero + 1
        else:
            # se la lista è vuoto e aggiungiamo il primo strumento
            nuovo_numero = 1

        nuovo_codice = f"S{nuovo_numero}"

        # aggiungiamo il nuovo strumento nella lista di strumenti con il rispettivo codice
        nuovo_strumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo_strumento)

        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        strumenti_oridinati = sorted(self.strumenti, key = attrgetter("marca"))

        return strumenti_oridinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        # verifica dell' esistenza dello strumento nel sistema
        codici_strumenti = []
        for strumento in self.strumenti:
            codici_strumenti.append(strumento.codice) # creo lista dei codici di tutti gli strumenti
        if id_strumento not in codici_strumenti:
            raise Exception("Strumento non presente nel sistema!")

        # verifica che lo strumento non sia gia in presitito
        for p in self.prestiti:
            if p["id_strumento"] == id_strumento:
                raise Exception("Strumento gia' in prestito!")

        # creazione del codice del prestito
        id_prestito = f"P{self.contatore_prestiti}"
        self.contatore_prestiti += 1

        prestito = {"codice": id_prestito, "data": data, "id_strumento": id_strumento, "cognome_allievo": cognome_allievo}

        # aggiungiamo il prestito nel dizionario con come chiave il codice ("P1") e come
        # valore il prestito
        # dunque avro' un disizionario del tipo: {"P1": {prestito}, "P2": {prestito}...}
        self.prestiti[id_prestito] = prestito

        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        # controllo se il codice del prestito sia tra le chiavi del dizionario
        if id_prestito not in self.prestiti:
            raise Exception("Il prestito non esite!")

        # rimuove e restituisce il prestito dal dizionario
        return self.prestiti.pop(id_prestito)
