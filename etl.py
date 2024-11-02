import glob as g
from datetime import datetime
import pandas as pd

def extract_from_csv(file):
    """Extrait les données d'un fichier CSV et les retourne dans un DataFrame Pandas."""
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV '{file}': {e}")
        return pd.DataFrame()

def extract_from_json(file):
    """Extrait les données d'un fichier JSON et les retourne dans un DataFrame Pandas."""
    try:
        df = pd.read_json(file)  # Pas de 'lines=True' car le JSON est en format tableau
        return df
    except ValueError as e:
        print(f"Erreur lors de la lecture du fichier JSON '{file}': {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur

def extract():
    """Extrait les données de tous les fichiers CSV et JSON dans un répertoire donné
    et les concatène dans un seul DataFrame Pandas."""
    extracted_data = []
    
    # Itère sur tous les fichiers CSV dans le répertoire "Raw_Data"
    for file in g.glob("Raw_Data/*.csv"):
        print(f"Extraction du fichier CSV: {file}")
        extracted_data.append(extract_from_csv(file))
    
    # Itère sur tous les fichiers JSON dans le répertoire "Raw_Data"
    for file in g.glob("Raw_Data/*.json"):
        print(f"Extraction du fichier JSON: {file}")
        extracted_data.append(extract_from_json(file))
    
    # Concatenate all DataFrames in the list into a single DataFrame
    if extracted_data:
        return pd.concat(extracted_data, ignore_index=True)
    else:
        print("Aucun fichier n'a été extrait.")
        return pd.DataFrame()

def transform(data): 
    """Transforme les données extraites en nettoyant et en structurant les informations."""
    data.dropna(inplace=True)  # Supprime les lignes avec des valeurs manquantes
    
    # S'assurer que la colonne "price" est numérique et arrondir à deux décimales
    data['price'] = pd.to_numeric(data['price'], errors='coerce').round(2)
    data.dropna(subset=['price'], inplace=True)  # Supprime les lignes où le prix est NaN
    
    # Calculer l'âge de la voiture
    data['car_age'] = datetime.today().year - data['year_of_manufacture']
    
    # Suppression des doublons
    data.drop_duplicates(inplace=True)
    
    return data

def load(targetfile, data_to_load):
    """Charge les données transformées dans un fichier CSV."""
    try:
        data_to_load.to_csv(targetfile, index=False)  # Sauvegarder sans index
        print(f"Les données ont été chargées dans le fichier {targetfile}.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement dans le fichier '{targetfile}': {e}")

# Exécution du ETL
if __name__ == "__main__":
    # Extraction
    extracted_df = extract()
    
    # Transformation
    if not extracted_df.empty:
        transformed_df = transform(extracted_df)
        
        # Load
        load(targetfile="Transformed_Data/transformed_cars_data.csv", data_to_load=transformed_df)
