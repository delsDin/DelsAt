from fpdf import FPDF
from pathlib import Path
import datetime

class WeatherReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Rapport d\'Analyse Climatique - Cotonou (65344)', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def export_to_pdf(df, stats, anomalies_count):
    """Génère un rapport PDF complet dans le dossier outputs/reports/."""
    
    # Configuration des chemins
    base_path = Path(__file__).resolve().parent.parent
    report_dir = base_path / "outputs" / "reports"
    figures_dir = base_path / "outputs" / "figures"
    report_dir.mkdir(parents=True, exist_ok=True)
    
    pdf = WeatherReport()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 1. Introduction et Résumé
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Résumé des données", 0, 1)
    pdf.set_font("Arial", size=11)
    date_str = datetime.datetime.now().strftime("%d/%m/%Y")
    pdf.multi_cell(0, 10, f"Rapport généré le : {date_str}\n"
                         f"Période couverte : 2015 - 2025\n"
                         f"Nombre total de jours analysés : {len(df)}\n"
                         f"Nombre d'anomalies thermiques détectées : {anomalies_count}")
    pdf.ln(5)

    # 2. Statistiques Descriptives
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Statistiques principales", 0, 1)
    pdf.set_font("Courier", size=10) # Police monospacée pour le tableau
    stats_text = stats.to_string()
    pdf.multi_cell(0, 5, stats_text)
    pdf.ln(10)

    # 3. Insertion des Graphiques
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "3. Visualisations clés", 0, 1)
    
    # Image 1 : Tendance
    if (figures_dir / "01_tendance_temp.png").exists():
        pdf.image(str(figures_dir / "01_tendance_temp.png"), x=10, w=180)
        pdf.ln(5)

    # Image 2 : Heatmap
    pdf.add_page()
    pdf.cell(0, 10, "4. Intensité et Saisonnalité", 0, 1)
    if (figures_dir / "03_heatmap.png").exists():
        pdf.image(str(figures_dir / "03_heatmap.png"), x=10, w=180)

    # Sauvegarde finale
    report_path = report_dir / "rapport_climatique_final.pdf"
    pdf.output(str(report_path))
    print(f"📄 Rapport PDF exporté avec succès : {report_path}")

if __name__ == "__main__":
    # Test rapide si lancé seul
    print("Test de l'export PDF...")