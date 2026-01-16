<p align="center">
  <img src="Docs/DelsAt.png" alt="DelsAt Logo" width="200">
</p>


<p align="center">
  Analyse Climatique
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

# Weather Dashboard 🌤️

Un tableau de bord interactif pour l'analyse et la visualisation de données météorologiques. Ce projet permet de charger, nettoyer, analyser et visualiser des données météo à travers une interface complète basée sur Python.

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Technologies utilisées](#-technologies-utilisées)
- [Notebooks](#-notebooks)
- [Contribution](#-contribution)
- [Licence](#-licence)

## 🎯 Aperçu

Ce projet propose une solution complète d'analyse de données météorologiques, incluant le chargement de données brutes (CSV/JSON), leur nettoyage avec Pandas, des analyses statistiques approfondies avec NumPy, et des visualisations interactives créées avec Matplotlib et Seaborn.

## ✨ Fonctionnalités

- **Chargement de données** : Import de fichiers CSV et JSON contenant des données météorologiques
- **Nettoyage des données** : Traitement des valeurs manquantes, normalisation et validation
- **Analyses statistiques** : Calculs de tendances, moyennes, écarts-types et corrélations
- **Visualisations** : Graphiques interactifs et tableaux de bord détaillés
- **Rapports automatisés** : Génération de rapports au format PDF et texte
- **Export de graphiques** : Sauvegarde des visualisations en PNG et SVG

## 📁 Structure du projet

```
weather_dashboard/
│
├── data/
│   ├── raw/                    # Données brutes (CSV/JSON)
│   └── processed/              # Données nettoyées
│
├── notebooks/
│   ├── report.ipynb           # Rapport final
│   ├── exploration.ipynb      # Analyse exploratoire (EDA)
│   └── dashboard.ipynb        # Visualisations finales
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Chargement et récupération des données
│   ├── data_cleaner.py        # Nettoyage des données (Pandas)
│   ├── analysis.py            # Analyses statistiques (NumPy, Pandas)
│   ├── visualization.py       # Graphiques (Matplotlib, Seaborn)
│
├── outputs/
│   ├── figures/               # Graphiques exportés (PNG, SVG)
│   └── reports/               # Rapports (texte, PDF)
│
├── requirements.txt           # Dépendances du projet
├── README.md                  # Documentation du projet
└── main.py                    # Point d'entrée du programme
```

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. Clonez le dépôt :
```bash
delsDingit clone https://github.com/delsDin/Delsat.git
cd weather_dashboard
```

2. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Exécution du programme principal

```bash
python main.py
```

### Utilisation des notebooks

Lancez Jupyter Notebook pour accéder aux analyses interactives :

```bash
jupyter notebook
```

Ouvrez ensuite les notebooks dans l'ordre suivant :
1. `exploration.ipynb` - Pour l'analyse exploratoire des données
2. `dashboard.ipynb` - Pour les visualisations finales
3. `report.ipynb` - Pour générer le rapport complet

### Exemple d'utilisation programmatique

```python
from src.data_loader import load_local_data
from src.data_cleaner import clean_weather_data
from src.analysis import get_descriptive_stats
from src.visualization import plot_temperature_trend

# Charger les données
data = load_local_data(Station_id, option)

# Nettoyer les données
clean_df = clean_weather_data(data)

# Analyser
get_descriptive_stats(clean_df)

# Visualiser
plot_temperature_trend(clean_df)
```

## 🛠️ Technologies utilisées

- **Python 3.8+** - Langage de programmation
- **Pandas** - Manipulation et nettoyage des données
- **NumPy** - Calculs numériques et analyses statistiques
- **Matplotlib** - Création de graphiques
- **Seaborn** - Visualisations statistiques avancées
- **Jupyter** - Notebooks interactifs pour l'exploration

## 📊 Notebooks

### exploration.ipynb
Analyse exploratoire des données (EDA) incluant :
- Statistiques descriptives
- Détection des valeurs aberrantes
- Distribution des variables

### dashboard.ipynb
Visualisations finales présentant :
- Évolution temporelle des températures
- Précipitations mensuelles
- Comparaisons saisonnières
- Indicateurs clés de performance

### report.ipynb
Rapport complet avec :
- Synthèse des analyses
- Conclusions et recommandations

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/NewAt`)
3. Committez vos changements (`git commit -m 'Add some NewAt'`)
4. Pushez vers la branche (`git push origin feature/NewAt`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

<p align="center">
  <img src="Docs/Dels.jpg" alt="Dels Dinla Marcel" width="200">
</p>
<p align="center">
<b>Dels Dinla Marcel</b>
</p>
<p align="center" style="color : #00ccff">
Data Scientist & AI en Licence 1 à l'Institut de Formation et de Recherche en Informatique (IFRI Bénin)
</p>

## 🙏 Remerciements

- Merci aux contributeurs de données météorologiques ouvertes
- Inspiration tirée de la communauté data science
- Documentation Python et bibliothèques scientifiques

---