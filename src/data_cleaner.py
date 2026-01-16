import pandas as pd
import numpy as np
from pathlib import Path
from src import data_loader as dl
def clean_weather_data(data):
    """
    Nettoie et enrichit les données météorologiques.
    """

    # Copie
    data_clean = data.copy()

    #Conversion de la colonne time en datetime (si ce n'est pas déjà fait)
    data_clean['time'] = pd.to_datetime(data_clean['time'])
    # --- ÉTAPE A : GESTION DES VALEURS HORS NORMES (OUTLIERS) ---
    # On définit des limites réalistes pour Cotonou (par exemple)
    # Si une valeur dépasse, on la remplace par NaN pour qu'elle soit interpolée plus tard
    if 'tmax' in data_clean.columns:
        data_clean.loc[data_clean['tmax'] > 50, 'tmax'] = np.nan
    if 'tmin' in data_clean.columns:
        data_clean.loc[data_clean['tmin'] < 10, 'tmin'] = np.nan

    # Suppression des colonnes totalement vides
    cols_to_drop = ['rhum', 'snwd', 'wspd', 'wpgt', 'pres', 'tsun', 'cldc']
    data_clean = data_clean.drop(columns = cols_to_drop)

    # Gestion des valeurs manquantes (NaN ou NA)
    # 1. Pour la temperature : interpolation linéaire pour combler les trous
    for i in ['tmin', 'tmax', 'temp']:
        data_clean[i] = data_clean[i].astype(float).interpolate(method = 'linear')
    
    # 2. Pour la précipitation  : remplacer NA par 0
    data_clean['prcp'] = data_clean['prcp'].fillna(0.0)

    # Création de nouvelles colonnes (utilisables prochainement)
    data_clean['year'] = data_clean['time'].dt.year
    data_clean['month'] = data_clean['time'].dt.month

    def get_season(month):
        if month in [11, 12, 1, 2, 3] : return 'Sèche longue'
        if month in [4, 5, 6, 7] : return 'Pluie longue'
        if month in [8, 9] : return 'Sèche courte'
        if month in [10] : return 'Pluie courte'
    
    data_clean['season'] = data_clean['month'].apply(get_season)

    data_clean = data_clean.sort_values('time')

    # Exporter les données nettoyées
    dl.save_raw_data(data_clean,65344, 1)
    
    return data_clean