from datetime import datetime
from meteostat import daily
import pandas as pd
from pathlib import Path
import config as cf
STATION_ID = '65344'
START_DATE = datetime(2015, 1, 1)
END_DATE = datetime(2025, 12, 31)

def fetch_from_meteostat(station_id, start, end) :
    """Récupère les données depuis l'API Meteostat."""
    try:
        data = daily(station_id, start, end)
        df = data.fetch()

        if df.empty:
            print(cf.Couleurs.ROUGE_CLAIR,f"⚠️ Aucune donnée trouvée pour la station {station_id}.", cf.Couleurs.RESET)
            return None

        # On remet la date en colonne pour avoir un CSV propre
        return df.reset_index()
    except Exception as e:
        print(cf.Couleurs.ROUGE,f"Erreur lors de la récupération API : {e}", cf.Couleurs.RESET)
        return None
    
def save_raw_data(df, station_id, type):
    """Sauvegarde les données brutes au format CSV."""

    if type in ['nettoyer', 'gerer', 'clean', 'propre', 'cl', 1] : type = 'processed'
    else : type = 'raw' 

    output_dir = Path(__file__).resolve().parent.parent / "data" / f"{type}"
    
    # Créer le dossier s'il n'existe pas (parents=True crée data ET raw)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = output_dir / f"weather{station_id}.csv"
    try:
        df.to_csv(file_path, index=False)
        print(cf.Couleurs.VERT,f"Données sauvegardées dans : {file_path}", cf.Couleurs.RESET)
        return True
    
    except Exception as e :
        print(cf.Couleurs.ROUGE,f"Erreur lors d'exportation des données : {e}", cf.Couleurs.RESET)
        return False

def load_local_data(station_id, type) :
    """Charge les données depuis le fichier local s'il existe."""
    # Au début de data_loader.py
    if type in ['nettoyer', 'gerer', 'clean', 'propre', 'cl', 1] : type = 'processed'
    else : type = 'raw' 
    file_path = Path(__file__).resolve().parent.parent / "data" / f"{type}" / f"weather{station_id}.csv"

    if file_path.is_file():
        print(f"Chargement des données locales ({station_id})...")
        return pd.read_csv(file_path)
    else:
        return None

if __name__ == '__main__':
    print(load_local_data(65344, 1))