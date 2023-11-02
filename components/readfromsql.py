import sqlite3
import pandas as pd

def readfromsql():
# Spécifiez le chemin de la base de données SQLite
    db_path = 'chemin_vers_votre_base_de_donnees.sqlite'

# Établissez une connexion avec la base de données
    conn = sqlite3.connect(db_path)

# Écrivez votre requête SQL pour extraire les données de la base de données
    sql_query = "SELECT * FROM nom_de_votre_table WHERE condition"

# Utilisez pd.read_sql_query pour exécuter la requête et stocker les résultats dans un DataFrame
    df = pd.read_sql_query(sql_query, conn)

    conn.close()