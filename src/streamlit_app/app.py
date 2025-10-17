import streamlit as st
import pandas as pd
import plotly.express as px

# Titre
st.title("🏡 Analyse du marché immobilier (DVF)")

# Charger les données
df = pd.read_csv("data/dvf_clean.csv")

if df.empty:
    st.warning("Le fichier CSV est vide. Lancez d'abord le pipeline pour générer dvf_clean.csv.")
    st.stop()

# Filtre : code postal
codes_postaux = df["Code postal"].sort_values().unique()
selected_cp = st.selectbox("Choisir un code postal", options=codes_postaux)

# Filtrer les données
filtered_df = df[df["Code postal"] == selected_cp]

st.write(f"Nombre de biens pour le code postal {selected_cp} : {len(filtered_df)}")

# Histogramme du prix au m²
fig_hist = px.histogram(
    filtered_df,
    x="prix_m2",
    nbins=50,
    labels={"prix_m2": "Prix au m² (€)"},
    title="Distribution du prix au m²"
)
fig_hist.update_layout(
    xaxis_title="Prix au m² (€)",
    yaxis_title="Nombre de biens"
)
st.plotly_chart(fig_hist)

# Répartition du prix par type de bien
fig_type = px.box(
    filtered_df,
    x="Type local",
    y="prix_m2",
    points="all",
    labels={"prix_m2": "Prix au m² (€)", "Type local": "Type de bien"},
    title="Prix au m² par type de bien"
)
st.plotly_chart(fig_type)

st.markdown("Made with Streamlit")