import pandas as pd
from pathlib import Path

# Chemins
RAW_DIR = Path(__file__).resolve().parents[2] / "data/raw"
TXT_FILES = list(RAW_DIR.glob("*.txt"))
OUT_FILE = Path(__file__).resolve().parents[2] / "data/dvf_clean.csv"
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

if not TXT_FILES:
    print("Aucun fichier TXT trouvé dans data/raw. Lance download_dvf.py d'abord.")
    exit()

# Lecture et concaténation des fichiers TXT
dfs = [pd.read_csv(f, sep="|", low_memory=False) for f in TXT_FILES]
df = pd.concat(dfs, ignore_index=True)

# Colonnes utiles
cols = ["Date mutation","Valeur fonciere","Code postal","Commune","Type local","Surface reelle bati"]
df = df[[c for c in cols if c in df.columns]]

# Nettoyage des valeurs numériques
df["Valeur fonciere"] = pd.to_numeric(df["Valeur fonciere"].astype(str).str.replace(",", "").str.strip(), errors="coerce")
df["Surface reelle bati"] = pd.to_numeric(df["Surface reelle bati"].astype(str).str.replace(",", "").str.strip(), errors="coerce")

# Supprimer les lignes invalides
df = df.dropna(subset=["Valeur fonciere","Surface reelle bati"])
df = df[df["Surface reelle bati"] > 0]

# Calcul prix/m²
df["prix_m2"] = df["Valeur fonciere"] / df["Surface reelle bati"]

# Correction code postal : string 5 chiffres
df["Code postal"] = df["Code postal"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(5)

# Filtrage : types de bien, prix/m² et surfaces plausibles
df = df[df["Type local"].isin(["Maison","Appartement"])]
df = df[(df["prix_m2"] > 500) & (df["prix_m2"] < 20000)]
df = df[(df["Surface reelle bati"] > 10) & (df["Surface reelle bati"] < 1000)]

# Sauvegarde CSV
df.to_csv(OUT_FILE, index=False)
print(f"✅ Fichier nettoyé créé avec {len(df)} lignes : {OUT_FILE}")
