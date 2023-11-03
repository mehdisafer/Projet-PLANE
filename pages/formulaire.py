# import streamlit as st
# from components.readfromsql import get_gender, get_class_type, get_customer_type, get_travel_type


# def evaluation():
#     return range(6)


# st.selectbox("Genre", [gender[0] for gender in get_gender()])
# st.selectbox("Type de Client", [customer_type[0]
#              for customer_type in get_customer_type()])
# st.selectbox("Classe", [class_type[0] for class_type in get_class_type()])
# st.selectbox("Type de Voyage", [travel_type[0]
#              for travel_type in get_travel_type()])


# st.text_input("L'âge:")
# st.text_input("Distance de vol:")
# st.text_input("Retard de départ en minutes:")
# st.text_input("Retard d'arrivée en minutes:")

# st.radio('Service Wifi en Vol:', evaluation(), horizontal=True)
# st.radio('Heure de départ/arrivée pratique:', evaluation(), horizontal=True)
# st.radio('Facilité de réservation en ligne:', evaluation(), horizontal=True)
# st.radio('Emplacement de la porte:', evaluation(), horizontal=True)
# st.radio('Nourriture et boissons:', evaluation(), horizontal=True)
# st.radio('Embarquement en ligne:', evaluation(), horizontal=True)
# st.radio('Confort du siège:', evaluation(), horizontal=True)
# st.radio('Divertissement à bord:', evaluation(), horizontal=True)
# st.radio('Service à board:', evaluation(), horizontal=True)
# st.radio('Service de chambre pour le jamble:', evaluation(), horizontal=True)
# st.radio('Gestion des bagages:', evaluation(), horizontal=True)
# st.radio('Service d\'enregistrement:', evaluation(), horizontal=True)
# st.radio('Service en vol:', evaluation(), horizontal=True)
# st.radio('Propreté:', evaluation(), horizontal=True)
import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier

def evaluation():
    return range(6)
# Collectez les données à partir des widgets Streamlit
age = st.text_input("Âge:")
# Vérifiez si le champ "Âge" n'est pas vide
if age:
    age = int(age)  # Convertissez en entier si ce n'est pas vide
else:
    # Fournissez une valeur par défaut ou un message d'erreur si le champ est vide
    st.error("Veuillez saisir l'âge.")
flight_distance = st.text_input("Distance de vol:")
# Vérifiez si le champ "Distance de vol" n'est pas vide
if flight_distance:
    flight_distance = int(flight_distance)  # Convertissez en entier si ce n'est pas vide
else:
    # Fournissez une valeur par défaut ou un message d'erreur si le champ est vide
    st.error("Veuillez saisir la distance de vol.")
wifi_service = st.radio('Service Wifi en Vol:', evaluation(), horizontal=True)
departure_arrival_time_convenient = st.radio('Heure de départ/arrivée pratique:', evaluation(), horizontal=True)
online_booking = st.radio('Facilité de réservation en ligne:', evaluation(), horizontal=True)
gate_location = st.radio('Emplacement de la porte:', evaluation(), horizontal=True)
food_and_drink = st.radio('Nourriture et boissons:', evaluation(), horizontal=True)
online_boarding = st.radio('Embarquement en ligne:', evaluation(), horizontal=True)
seat_comfort = st.radio('Confort du siège:', evaluation(), horizontal=True)
inflight_entertainment = st.radio('Divertissement à bord:', evaluation(), horizontal=True)
onboard_service = st.radio('Service à board:', evaluation(), horizontal=True)
leg_room_service = st.radio('Service de chambre pour le jamble:', evaluation(), horizontal=True)
baggage_handling = st.radio('Gestion des bagages:', evaluation(), horizontal=True)
checkin_service = st.radio('Service d\'enregistrement:', evaluation(), horizontal=True)
inflight_service = st.radio('Service en vol:', evaluation(), horizontal=True)
cleanliness = st.radio('Propreté:', evaluation(), horizontal=True)
arrival_delay_in_minutes = st.text_input("Retard d'arrivée en minutes:")
# Vérifiez si le champ "Retard d'arrivée en minutes" n'est pas vide
if arrival_delay_in_minutes:
    arrival_delay_in_minutes = int(arrival_delay_in_minutes)  # Convertissez en entier si ce n'est pas vide
else:
    # Fournissez une valeur par défaut ou un message d'erreur si le champ est vide
    st.error("Veuillez saisir le retard d'arrivée en minutes.")

# Utilisez un widget st.radio pour collecter le genre (Homme ou Femme)
gender_choice = st.radio("Genre", ["Homme", "Femme"])
# Définissez les valeurs en fonction du choix de l'utilisateur
if gender_choice == "Homme":
    gender_Male = 1
    gender_Female = 0
else:  # Si l'utilisateur choisit "Femme"
    gender_Male = 0
    gender_Female = 1

# Utilisez un widget st.radio pour collecter le type de client (Client Loyal ou Client Non-Loyal)
customer_type_choice = st.radio("Type de Client", ["Client Loyal", "Client Non-Loyal"])
# Définissez les valeurs en fonction du choix de l'utilisateur
if customer_type_choice == "Client Loyal":
    customer_type_Loyal_Customer = 1
    customer_type_disloyal_Customer = 0
else:  # Si l'utilisateur choisit "Client Non-Loyal"
    customer_type_Loyal_Customer = 0
    customer_type_disloyal_Customer = 1

# Utilisez un widget st.radio pour collecter le type de voyage (Voyage d'Affaires ou Voyage Personnel)
travel_type_choice = st.radio("Type de Voyage", ["Voyage d'Affaires", "Voyage Personnel"])

# Définissez les valeurs en fonction du choix de l'utilisateur
if travel_type_choice == "Voyage d'Affaires":
    type_of_travel_Business_travel = 1
    type_of_travel_Personal_Travel = 0
else:  # Si l'utilisateur choisit "Voyage Personnel"
    type_of_travel_Business_travel = 0
    type_of_travel_Personal_Travel = 1

# Utilisez un widget st.radio pour collecter la classe (Business, Eco, ou Eco Plus)
class_choice = st.radio("Classe", ["Business", "Eco", "Eco Plus"])

# Définissez les valeurs en fonction du choix de l'utilisateur
if class_choice == "Business":
    class_Business = 1
    class_Eco = 0
    class_Eco_Plus = 0
elif class_choice == "Eco":
    class_Business = 0
    class_Eco = 1
    class_Eco_Plus = 0
else:  # Si l'utilisateur choisit "Eco Plus"
    class_Business = 0
    class_Eco = 0
    class_Eco_Plus = 1

if age and flight_distance and arrival_delay_in_minutes and gender_Male is not None and gender_Female is not None and customer_type_Loyal_Customer is not None and customer_type_disloyal_Customer is not None and type_of_travel_Business_travel is not None and type_of_travel_Personal_Travel is not None and class_Business is not None and class_Eco is not None and class_Eco_Plus is not None:

    # Créez un dictionnaire avec les données collectées
    manual_data = {
        'age': int(age),
        'flight_distance': int(flight_distance),
        'inflight_wifi_service': wifi_service,
        'departure_arrival_time_convenient': departure_arrival_time_convenient,
        'ease_of_online_booking': online_booking,
        'gate_location': gate_location,
        'food_and_drink': food_and_drink,
        'online_boarding': online_boarding,
        'seat_comfort': seat_comfort,
        'inflight_entertainment': inflight_entertainment,
        'on-board_service': onboard_service,
        'leg_room_service': leg_room_service,
        'baggage_handling': baggage_handling,
        'checkin_service': checkin_service,
        'inflight_service': inflight_service,
        'cleanliness': cleanliness,
        'arrival_delay_in_minutes': int(arrival_delay_in_minutes),
        'gender_Female': 0,  # Remplissez en fonction de la sélection
        'gender_Male': 1,  # Remplissez en fonction de la sélection
        'customer_type_Loyal_Customer': 0,  # Remplissez en fonction de la sélection
        'customer_type_disloyal_Customer': 1,  # Remplissez en fonction de la sélection
        'type_of_travel_Business_travel': 0,  # Remplissez en fonction de la sélection
        'type_of_travel_Personal_Travel': 1,  # Remplissez en fonction de la sélection
        'class_Business': 0,  # Remplissez en fonction de la sélection
        'class_Eco': 1,  # Remplissez en fonction de la sélection
        'class_Eco_Plus': 0,  # Remplissez en fonction de la sélection
    }
    manual_df = pd.DataFrame([manual_data])
    model = CatBoostClassifier()
    model.load_model('components/modele_catboost.cbm')
    # Utilisez ce dictionnaire pour effectuer des prédictions avec votre modèle CatBoost
    y_manual_pred = model.predict(pd.DataFrame([manual_data]))

    # Collectez les données et effectuez les prédictions comme expliqué précédemment

    # Affichez les prédictions sur la page Streamlit
        # Effectuez la prédiction
    y_manual_pred = model.predict(pd.DataFrame([manual_data]))
        # Affichez le résultat de la prédiction
    st.write("Résultat de la prédiction:", y_manual_pred)
else:
        # Affichez un message d'erreur si un champ obligatoire n'est pas rempli
    st.error("Veuillez remplir tous les champs obligatoires pour effectuer la prédiction.")