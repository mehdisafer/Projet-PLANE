import pandas as pd
from catboost import CatBoostClassifier

# Charger le modèle depuis le fichier
model = CatBoostClassifier()
model.load_model('modele_catboost.cbm')

# transformation des données manuelles
manual_data = {
    'age': 30,
    'flight_distance': 1000,
    'inflight_wifi_service': 5,
    'departure_arrival_time_convenient': 4,
    'ease_of_online_booking': 5,
    'gate_location': 3,
    'food_and_drink': 4,
    'online_boarding': 5,
    'seat_comfort': 4,
    'inflight_entertainment': 5,
    'on-board_service': 4,
    'leg_room_service': 3,
    'baggage_handling': 5,
    'checkin_service': 4,
    'inflight_service': 5,
    'cleanliness': 4,
    'arrival_delay_in_minutes': 15,
    'gender_Female': 0,
    'gender_Male': 1,
    'customer_type_Loyal_Customer': 1,
    'customer_type_disloyal_Customer': 0,
    'type_of_travel_Business_travel': 1,
    'type_of_travel_Personal_Travel': 0,
    'class_Business': 1,
    'class_Eco': 0,
    'class_Eco_Plus': 0
}
manual_df = pd.DataFrame([manual_data])

# Faire des prédictions
y_manual_pred = model.predict(manual_df)