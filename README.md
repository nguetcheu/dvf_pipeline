# 🏡 Projet LDF - Pipeline Immobilier (DVF Open Data)

## 🎯 Objectif
Créer un pipeline de données complet pour analyser le marché immobilier français à partir des **données DVF** (Demandes de Valeurs Foncières) en **open data**.

## 🧱 Architecture
- **Scraping / Ingestion :** téléchargement automatique depuis data.gouv.fr
- **Nettoyage :** calcul du prix/m², filtrage, nettoyage CSV
- **Automatisation :** pipeline GitHub Actions (CI/CD)
- **Visualisation :** tableau de bord Streamlit interactif

## 📂 Structure du projet
```
src/
├─ ingestion/download_dvf.py
├─ cleaning/clean_dvf.py
└─ streamlit_app/app.py
.github/workflows/main.yml
data/
└─ dvf_clean.csv (généré automatiquement)
```

## 🚀 Exécution locale
```bash
python src/ingestion/download_dvf.py
python src/cleaning/clean_dvf.py
streamlit run src/streamlit_app/app.py
```

## 🔄 Automatisation GitHub Actions
Le workflow se déclenche chaque lundi à 6h, télécharge les données, les nettoie, et pousse la version mise à jour du CSV sur le dépôt.

## 🌐 Source officielle
[Données DVF - data.gouv.fr](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees-dvf/)
