import sys
from pathlib import Path

# Ajout du dossier src au chemin de recherche pour l'import des modules
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from src.data_loader import fetch_from_meteostat, load_local_data, save_raw_data
from src.data_cleaner import clean_weather_data
from src.analysis import calculate_trends, get_descriptive_stats, analyze_anomalies
from src.visualization import save_all_figures
from src.report_generator import export_to_pdf

def run_pipeline(station_id):
    print(f"🚀 Démarrage du pipeline météo pour la station {station_id}...")

    # 1. CHARGEMENT
    # On tente de charger localement d'abord
    data = load_local_data(station_id, 0)
    
    if data is None:
        print("🌐 Données locales introuvables. Téléchargement depuis Meteostat...")
        data = fetch_from_meteostat(station_id)
        if data is not None:
            # Réinitialisation de l'index pour transformer la date en colonne 'time'
            data = data.reset_index()
            save_raw_data(data, station_id)
        else:
            print("❌ Échec de la récupération des données.")
            return

    # 2. NETTOYAGE
    print("🧹 Nettoyage et préparation des données...")
    df_clean = clean_weather_data(data)

    # 3. ANALYSE
    print("📊 Analyse statistique en cours...")
    # Calcul de la tendance avec moyenne mobile centrée (min_periods=1 pour éviter les NaN)
    df_analysis = calculate_trends(df_clean)
    
    stats = get_descriptive_stats(df_analysis)
    anomalies = analyze_anomalies(df_analysis)
    
    print(f"✅ Statistiques calculées sur {len(df_analysis)} jours.")
    print(f"🔥 {len(anomalies)} anomalies thermiques détectées.")

    # 4. VISUALISATION
    print("🎨 Génération des graphiques...")
    save_all_figures(df_analysis)
    export_to_pdf(df_analysis, stats, len(anomalies))
    print("\n✨ Pipeline terminé avec succès ! Consultez le dossier 'outputs/figures'.")

if __name__ == "__main__":
    # Utilisation de l'ID station Cotonou défini dans votre projet
    STATION_ID = '65344' 
    run_pipeline(STATION_ID)
    
