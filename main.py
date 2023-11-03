import streamlit as st
from components.readfromsql import get_gender, get_class_type, get_customer_type, get_travel_type
from catboost import CatBoostClassifier
import pandas as pd

from components.mymodule import *
from configs.config import *
from models.model_account import *

from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import create_database, database_exists, drop_database

st.title('Prediction de la :blue[satisfaction du client] :sunglasses:')

if 'register' not in st.session_state:
    st.session_state.register = None

def evaluation():
    return range(6)

windows = ["Formulaire","Graphique","About-us"]

# Colonne à gauche
with st.sidebar:
    st.header("Accueil ")
    deroulant = st.selectbox("Choisir :",["S'inscrire","Se connecter"])
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("## Description :")
    st.markdown("*Vous êtes préoccupé par la satisfaction*")
    st.markdown("*de vos clients ? Nous aussi!*")
    st.markdown("*Notre modèle a été entrainé sur un dataset*")
    st.markdown('*de **+** de **100K de lignes**!*')
    st.markdown("*Avec une précision de **+ de 95%** !*")
    st.text(" ")
    st.markdown('<hr>', unsafe_allow_html=True)
    # connect = st.button("Se connecter")
    # register = st.button("S'inscrire")

if deroulant == "S'inscrire" and st.session_state.register == None:
    # Définissez les éléments de l'interface
    st.title("Inscription")
    username = st.text_input("Nom d'utilisateur")
    email = st.text_input("Adresse e-mail")
    password = st.text_input("Mot de passe", type="password")

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()


    # # Vérifiez si la base de données existe
    # if database_exists(engine.url):# Supprimez la base de données si elle existe
    #     drop_database(engine.url)


    # # Créez la base de données si elle n'existe pas
    # create_database(engine.url)

    # Vérifiez si la base de données a été créée
    # if database_exists(engine.url):
    #     print("Base de données créée")

    # # Créez la table dans la base de données
    # Base.metadata.create_all(engine)

    # Afficher les données saisies
    if  st.button("Envoyer"):

        # Insérez les données dans la base de données
        user = User(
            username=username,
            email=email,
            password=password,
        )

        # Validez les données saisies
        if not validate_username(username):
            st.error("Le nom d'utilisateur doit contenir au moins 3 caractères et ne pas contenir de caractères spéciaux.")
        if not validate_email(email):
            st.error("L'adresse e-mail n'est pas valide.")
        if not validate_password(password):
            st.error("Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial.")
        if validate_username(username) and validate_email(email) and validate_password(password):
            #user.save(engine)
            session.add(user)
            session.commit()
            st.session_state.register = "Register_success"
            create_account = st.text(f"Félicitation {username} ! Tu viens de créer ton compte ! ")
            # redirection = create_account
            

if st.session_state.register == "Register_success":
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
        import pandas as pd

        manual_df = pd.DataFrame([manual_data])
        from catboost import CatBoostClassifier

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

# if windows == "Graphique":
#     st.header("Graphique")

# if windows == "About-us":
#     st.header("About-us")





