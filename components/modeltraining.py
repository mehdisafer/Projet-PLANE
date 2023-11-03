import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os
import sys

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)

# Charger les données
df = pd.read_csv("data/Airline_Dataset.csv")

# conversion des noms de colonnes en minuscule
df.columns = df.columns.str.lower()
df.drop(["departure delay in minutes"], axis=1, inplace=True)
df.drop(["id"], axis=1, inplace=True)

# Créer une liste des colonnes catégorielles
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('/', '_')

# Filtrer les lignes avec des zéros dans les colonnes spécifiées
cols_to_filter = ['departure_arrival_time_convenient', 'ease_of_online_booking', 'gate_location', 'food_and_drink', 'online_boarding', 'seat_comfort', 'inflight_entertainment', 'on-board_service', 'leg_room_service', 'baggage_handling', 'checkin_service', 'inflight_service', 'cleanliness']
df = df.loc[(df[cols_to_filter] != 0).any(axis=1)]

# Créer une liste des colonnes catégorielles
categorical_columns = ["gender", "customer_type", "type_of_travel", "class"]

# Créer des colonnes hot encoder pour chaque colonne catégorielle
for column in categorical_columns:
    df = pd.get_dummies(df, columns=[column],dtype=int)
df.columns = df.columns.str.replace(' ', '_')
df.dropna(inplace=True)
X = df.drop(columns=['satisfaction'])
y = df['satisfaction']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner un modèle CatBoost
model = CatBoostClassifier(iterations=500, learning_rate=0.1, depth=6, loss_function='Logloss')
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision : {:.2f}%".format(accuracy * 100))

# Matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrice de confusion :\n", conf_matrix)

# Rapport de classification
class_report = classification_report(y_test, y_pred)
print("Rapport de classification :\n", class_report)