import requests
import os

def download_dvf_data(output_dir="data/raw"):
    """Télécharge les fichiers DVF depuis data.gouv.fr"""
    os.makedirs(output_dir, exist_ok=True)
    url = "https://files.data.gouv.fr/dvf/latest/csv/valeursfoncieres-2023.txt"
    output_path = os.path.join(output_dir, "valeursfoncieres-2023.csv")

    print(f"Téléchargement du fichier DVF depuis {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Fichier téléchargé : {output_path}")
    else:
        print(f"❌ Erreur {response.status_code} lors du téléchargement.")

if __name__ == "__main__":
    download_dvf_data()
