import os

def trouver_fichiers_logs(dossier, extension=".log"):
    """
    Parcourt un dossier et renvoie une liste de fichiers de logs avec l'extension spécifié
    """
    fichiers_logs = []

    try: 
        # Parcourt le dossier et récupère tous les fichiers avec l'extension donnée
        for fichier in os.listdir(dossier):
            if fichier.endswith(extension):
                fichiers_logs.append(os.path.join(dossier,fichier))
        return fichiers_logs
    except FileNotFoundError:
        print(f"Erreur : le dossier {dossier} n'a pas été trouvé.")
        return[]
    
def lire_logs(fichier_log):
    """
    Lit un fichier de logs et renvoie son contenu sous forme de liste de lignes.
    """
    try:
        with open(fichier_log, 'r') as f:
            logs = f.readlines()
        return logs
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_log} n'a pas été trouvé.")
        return []