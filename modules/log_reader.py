import os


class LogReader:
    def __init__(self, repertoire):
        """
        Initialise un lecteur de logs avec une liste vide pour stocker les lignes lues.
        """
        self.repertoire = repertoire
        self.lignes_lues = []

    def trouver_fichiers_logs(self, extension=".log"):
    
        """
        Parcourt le repertoire et renvoie une liste de fichiers de logs
        avec l'extension spécifiée.
        """
        fichiers_logs = []

        try:
            # Parcourt le dossier et récupère tous les fichiers avec l'extension donnée
            for fichier in os.listdir(self.repertoire):
                if fichier.endswith(extension):
                    fichiers_logs.append(os.path.join(self.repertoire, fichier))

            return fichiers_logs

        except FileNotFoundError:
            print(f"Erreur : le repertoire {self.repertoire} n'a pas été trouvé.")
            return []

    def lire_logs(self, fichier_log):
        """
        Lit un fichier de logs et renvoie son contenu sous forme de liste de lignes.
        """
        try:
            with open(fichier_log, "r") as f:
                logs = f.readlines()
            return logs

        except FileNotFoundError:
            print(f"Erreur : Le fichier {fichier_log} n'a pas été trouvé.")
            return []