import requests
import os
import zipfile
from pathlib import Path

def download_and_extract_dvf(output_dir="data/raw"):
    os.makedirs(output_dir, exist_ok=True)
    url = "https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20250406-003043/valeursfoncieres-2024.txt.zip"
    zip_path = os.path.join(output_dir, "valeursfoncieres-2024.txt.zip")

    # Télécharger si le fichier n'existe pas
    if not os.path.exists(zip_path):
        print(f"Téléchargement du fichier DVF depuis {url}...")
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            with open(zip_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Fichier téléchargé : {zip_path}")
        else:
            print(f"❌ Erreur {response.status_code} lors du téléchargement.")
            return
    else:
        print(f"⚠️ Le fichier existe déjà : {zip_path}")

    # Extraction du ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"✅ Fichier TXT extrait dans {output_dir}")

    # Vérifier qu'il y a bien un TXT
    txt_files = list(Path(output_dir).glob("*.txt"))
    if txt_files:
        print(f"✅ {len(txt_files)} fichier(s) TXT prêt(s) pour le nettoyage :")
        for f in txt_files:
            print(f" - {f}")
    else:
        print("❌ Aucun fichier TXT trouvé après extraction.")

if __name__ == "__main__":
    download_and_extract_dvf()
