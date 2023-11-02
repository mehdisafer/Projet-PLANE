import sqlite3
import pandas as pd

def writetosql():
# Spécifiez le chemin de la base de données SQLite
    db_path = 'chemin_vers_votre_base_de_donnees.sqlite'

# Établissez une connexion avec la base de données
    conn = sqlite3.connect(db_path)

# Supposons que df est le DataFrame que vous souhaitez écrire dans la base de données
    table_name = 'nom_de_votre_table'

# Utilisez to_sql() pour écrire le DataFrame dans la table spécifiée
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()