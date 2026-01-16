from multiprocessing import Value
import pandas as pd
import numpy as np
from src.data_loader import save_raw_data

def get_descriptive_stats(data):
    """
    Calcule les statistiques de base pour le rapport.
    """
    stats = data[['temp', 'tmin', 'tmax', 'prcp']].describe()
    return stats

def calculate_trends(data, windows=30):
    """
    Calcule les moyennes mobiles pour identifier les tendances à long terme.
    L'argument 'window' définit le lissage (ex: 30 jours).
    """
    data_trends = data.copy()
    # Moyenne mobile sur 30 jours pour lisser les variations quotidiennes
    data_trends['temp_rolling_avg'] = data_trends['temp'].rolling(window=windows, center=True, min_periods=1).mean()
    save_raw_data(data_trends, 65344, 1)
    return data_trends

def analyze_anomalies(data):
    """
    Identifie les jours où les températures ont été exceptionnelles.
    """
    # Seuil : température supérieure à la moyenne + 2 écarts-types
    threshold = data['tmax'].mean() + (2 * data['tmax'].std())
    anomalies = data[data['tmax'] > threshold]
    return anomalies

def prepare_pivot_heatmap(data):
    """
    Prépare la matrice Mois/Année pour la Heatmap demandée.
    """
    # Pivot pour obtenir les années en colonnes et les mois en lignes
    pivot_table = data.pivot_table(values='temp', index='month', columns='year', aggfunc='mean')
    return pivot_table


if __name__ == "__main__":
    # Test du module
    from pathlib import Path
    
    # Chemin vers vos données nettoyées
    PROCESSED_DATA = Path(__file__).resolve().parent.parent / "data" / "processed" / "weather65344.csv"
    
    if PROCESSED_DATA.exists():
        df = pd.read_csv(PROCESSED_DATA)
        
        print("--- Statistiques Descriptives ---")
        print(get_descriptive_stats(df))
        
        print("\n--- Analyse des Anomalies (Records locaux) ---")
        anomalies = analyze_anomalies(df)
        print(f"Nombre de jours anormalement chauds : {len(anomalies)}")
    else:
        print("Fichier weather65344.csv non trouvé. Lancez d'abord data_cleaner.py")

    print(calculate_trends(df))