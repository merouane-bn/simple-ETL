# Projet ETL de Données de Voitures

## Description

Ce projet est un pipeline ETL (Extract, Transform, Load) conçu pour extraire des données de voitures de plusieurs fichiers CSV et JSON, transformer ces données pour inclure des informations calculées (comme l'âge de la voiture) et les charger dans un fichier CSV final. Le pipeline gère des valeurs manquantes, nettoie les doublons, et arrondit les valeurs de prix pour une meilleure précision.

## Structure du Projet

- `Raw_Data/`: Répertoire contenant les fichiers de données brutes (CSV et JSON) pour l'extraction.
- `Transformed_Data/`: Répertoire de destination pour le fichier CSV final transformé.
- `etl.py`: Script principal exécutant les étapes ETL (extraction, transformation, et chargement).
- `README.md`: Fichier de documentation du projet.

## Fonctionnalités

- **Extraction** : Lecture de tous les fichiers CSV et JSON dans le répertoire `Raw_Data`.
- **Transformation** : Nettoyage et enrichissement des données, y compris :
  - Suppression des valeurs manquantes et des doublons.
  - Arrondi des valeurs de prix à deux décimales.
  - Calcul de l'âge de chaque voiture en fonction de l'année de fabrication.
- **Chargement** : Enregistrement des données transformées dans un fichier CSV propre dans `Transformed_Data`.

## Prérequis

Assurez-vous d'avoir installé les packages Python suivants :
- **Python 3.7+**
- **pandas** : pour la gestion et transformation des données

Vous pouvez installer pandas en utilisant la commande suivante :

```bash
pip install pandas
```

## Installation et Configuration

1. Clonez ce dépôt sur votre machine locale.
2. Placez vos fichiers de données brutes (CSV et JSON) dans le répertoire `Raw_Data`.
3. Créez un répertoire `Transformed_Data` dans la racine du projet pour stocker le fichier transformé.

## Exemple de Fichiers de Données

Vous pouvez utiliser des fichiers JSON et CSV dans `Raw_Data` avec les colonnes suivantes :

- **car_model** : Modèle de la voiture (ex. : "Toyota Camry")
- **year_of_manufacture** : Année de fabrication de la voiture (ex. : 2020)
- **price** : Prix de la voiture, avec des décimales (ex. : 24000.99)
- **fuel** : Type de carburant (ex. : "Gasoline", "Electric", "Hybrid")

## Exécution du Projet

Pour exécuter le script ETL, lancez simplement la commande suivante :

```bash
python etl.py
```

Le script suit les étapes suivantes :

1. **Extraction** : Lit les fichiers JSON et CSV de `Raw_Data`.
2. **Transformation** : Nettoie, structure et transforme les données.
3. **Chargement** : Enregistre le fichier final dans `Transformed_Data/transformed_cars_data.csv`.

## Exemple de Résultat

Le fichier final `transformed_cars_data.csv` dans `Transformed_Data` contient les colonnes suivantes :

- `car_model` : Modèle de la voiture
- `year_of_manufacture` : Année de fabrication
- `price` : Prix arrondi à deux décimales
- `fuel` : Type de carburant
- `car_age` : Âge de la voiture calculé

## Auteurs

MEROUANE BENELABDY.

## Licence

Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus d'informations.

---
