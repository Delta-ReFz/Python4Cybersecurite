import argparse
from modules.log_reader import LogReader

def main():
    parser = argparse.ArgumentParser(description = "Script d'analyse de log")
    parser.add_argument(
        "repertoire" , help="Chemin vers le répertoire contenant les fichiers de logs à analyser", type = str
    )
    args = parser.parse_args()

    lecteur = LogReader(args.repertoire)

    fichiers_logs = lecteur.trouver_fichiers_logs()

    if fichiers_logs:
        for fichier_log in fichiers_logs:
            print(f"\nLecture du fichier : {fichier_log}")
            lecteur.lire_logs(fichier_log)

    print(f"Chemin des logs à analyser : {args.logpath} ")

if __name__ == "__main__":
    main()