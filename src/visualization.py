from operator import index
from turtle import color
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

# Configuration du style pour un rendu "pro"
sns.set_theme(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

def plot_temperature_trend(data):
    """1. Courbe temporelle avec la moyenne mobile centrée."""
    plt.figure()
    # Données réelles en arrière-plan (transparentes)
    plt.plot(data['time'], data['temp'], alpha=0.3, label='Température journalière', color='skyblue')

    # Tendance lissée
    if 'temp_rolling_avg' in data.columns:
        plt.plot(data['time'], data['temp_rolling_avg'], color='red', lw=2, label='Tendance (Moyenne 30j)')
    
    plt.title("Évolution des températures sur 10 ans")
    plt.xlabel('Années')
    plt.ylabel("Température (°C)")
    plt.legend()
    return plt.gcf()

def plot_precipitation_bar(df):
    """2. Précipitations mensuelles moyennes avec noms des mois et hue."""
    plt.figure()
    
    # 1. Préparation des données
    monthly_precip = df.groupby('month')['prcp'].mean().reset_index()
    
    # 2. Dictionnaire de conversion
    month_names = {
        1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr', 
        5: 'Mai', 6: 'Juin', 7: 'Juil', 8: 'Août', 
        9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Déc'
    }
    
    # 3. Remplacement des numéros par les noms
    monthly_precip['month_name'] = monthly_precip['month'].map(month_names)
    
    # 4. Création du graphique avec hue
    # On utilise 'month_name' pour l'axe X et pour la couleur (hue)
    sns.barplot(
        data=monthly_precip, 
        x='month_name', 
        y='prcp', 
        hue='month_name', 
        legend=False, 
        palette='Blues_d'
    )
    
    plt.title("Moyenne des précipitations par mois")
    plt.xlabel("Mois")
    plt.ylabel("Précipitations (mm)")
    
    return plt.gcf()

def plot_temperature_heatmap(data):
    """3. Heatmap température mois / année."""
    plt.figure(figsize=(10,8))
    # On utilise la pivot_table préparée dans analysis.py
    pivot = data.pivot_table(values='temp', index='month', columns='year', aggfunc='mean')
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlOrRd')
    plt.title("Intensité thermique mensuelle (Moyennes)")
    plt.xlabel('Années')
    plt.ylabel('Mois')
    return plt.gcf()

def plot_seasonal_boxplot(data):
    """4. Distribution des températures par saison."""
    plt.figure()
    sns.boxplot(data=data, x='season', y='temp', hue='season', palette='Set2')
    plt.title("Variabilité des températures par saison")
    plt.ylabel("Température (°C)")
    plt.xlabel('Saison')
    return plt.gcf()

def save_all_figures(data, output_dir="outputs/figures"):
    """Sauvegarde automatique des graphiques."""
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    # Dictionnaire {Nom du fichier : Fonction}
    viz_list = {
        "01_tendance_temp.png": plot_temperature_trend,
        "02_precipitation.png": plot_precipitation_bar,
        "03_heatmap.png": plot_temperature_heatmap,
        "04_boxplot_saison_temp.png": plot_seasonal_boxplot
    }

    for filename, func in viz_list.items():
        fig = func(data)
        fig.savefig(path / filename, bbox_inches='tight')
        plt.close(fig)
    print(f"✅ Graphiques exportés dans : {output_dir}")
    

if __name__ == "__main__":
    # Test local
    PROCESSED_FILE = Path(__file__).resolve().parent.parent / "data" / "processed" / "weather65344.csv"
    if PROCESSED_FILE.exists():
        data = pd.read_csv(PROCESSED_FILE, parse_dates=['time'])
        # On simule l'appel à analysis pour avoir les colonnes de tendance
        from analysis import calculate_trends
        data = calculate_trends(data)
        save_all_figures(data)