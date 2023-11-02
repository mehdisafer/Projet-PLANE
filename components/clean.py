import pandas as pd


def clean():

    df = pd.read_csv("Airline_Dataset.csv")
    df.info()

# Conversion des noms de colonnes en minuscule
    df.columns = df.columns.str.lower()
# Suprimer les colonnes arrival delay in minutes et id
    df.drop(["departure delay in minutes"], axis=1, inplace=True)
    df.drop(["id"], axis=1, inplace=True)

# Créer une liste des colonnes catégorielles
    categorical_columns = ["gender", "customer type", "type of travel", "class", "satisfaction"]

# Créer des colonnes hot encoder pour chaque colonne catégorielle
    for column in categorical_columns:
        df = pd.get_dummies(df, columns=[column],dtype=int)

# Remplace dans le nom des colonnes les espaces et les slashs par des underscores
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('/', '_')

# Supprime les 393 lignes avec des valeurs nulles
    df.dropna(inplace=True)