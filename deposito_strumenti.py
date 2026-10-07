from csv import reader

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        # TODO

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            filein = open(file_path, "r")
            file_read = reader(filein)

            for line in file_read:
                codice = line[0]
                tipo = line[1]
                marca = line[2]
                anno = line[3]
                valore = line[4]

            filein.close()

        except FileNotFoundError:
            print("File non trovato!")





    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
