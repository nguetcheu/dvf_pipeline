import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[2] / "data/dvf_clean.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

st.title("🏡 Analyse du marché immobilier (DVF)")

if CSV_PATH.exists():
    df = load_data(CSV_PATH)
    st.success(f"{len(df)} lignes chargées.")

    dept_list = sorted(df["Code postal"].dropna().unique())
    dept = st.selectbox("Choisir un code postal", dept_list)
    df_f = df[df["Code postal"] == dept]

    st.write("### Distribution du prix au m²")
    fig = px.histogram(df_f, x="prix_m2", nbins=50)
    st.plotly_chart(fig)

    st.write("### Prix par type de bien")
    fig2 = px.box(df_f, x="Type local", y="prix_m2")
    st.plotly_chart(fig2)
else:
    st.warning("Le fichier dvf_clean.csv est introuvable. Lance d'abord le pipeline d'ingestion et nettoyage.")
