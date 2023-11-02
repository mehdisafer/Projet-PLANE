import pandas as pd
from catboost import CatBoostClassifier

# Charger le modèle depuis le fichier
model = CatBoostClassifier()
model.load_model('modele_catboost.cbm')

# transformation des données manuelles
manual_data = {"nom_colonne1": "data1", "nom_colonne2": "data2", "nom_colonne1": "data3", "nom_colonne4": "data3", ...}
manual_df = pd.DataFrame([manual_data])

# Faire des prédictions
y_manual_pred = model.predict(manual_df)