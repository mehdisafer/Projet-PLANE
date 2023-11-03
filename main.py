import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from components.readfromsql import read_from_sqlite
from catboost import CatBoostClassifier
from catboost import CatBoostClassifier
from streamlit_lottie import st_lottie

__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 400, height = 500, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()


with st.sidebar:
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("**Le modèle a été entrainé sur un dataset de **+** de **100K** lignes de données, provenant de **+** de **100** entreprises différentes.**")
    st.markdown("**Voici quelques exemples d'utilisation du modèle :**")
    st.markdown("* **Identifier les sources de satisfaction et d'insatisfaction des clients.**")
    st.markdown("* **Développer des stratégies pour améliorer la satisfaction des clients.**")
    st.markdown("* **Mesurer l'impact des changements apportés à l'expérience client.**")
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("## Description :")
    st.markdown("**Notre modèle est là pour vous aider à améliorer la satisfaction de vos clients.**")
    st.markdown("**Il utilise l'apprentissage automatique pour analyser les données sur les interactions entre les clients et votre entreprise.**")
    st.markdown("**Cela lui permet de comprendre les facteurs qui influencent la satisfaction des clients et de proposer des recommandations pour l'améliorer.**")
    st.markdown('<hr>', unsafe_allow_html=True)

if  LOGGED_IN == True:
    st.title('Satisfaction :blue[Series X] :red[360]')
    def evaluation():
        return range(6)
        
    st.header("Accueil :sunglasses:")
    
    deroulant = st.selectbox("Choisir :",["Formulaire","Graphique","About-us"])
    st.markdown('<hr>', unsafe_allow_html=True)

    if deroulant == "Formulaire":
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
    
    if deroulant == "Graphique":
        @st.cache_resource
        def load_model():
            model = CatBoostClassifier()
            model.load_model('components/modele_catboost.cbm')
            return model


        @st.cache_resource
        def load_dataframe():
            data = read_from_sqlite()
            data.columns = data.columns.str.replace('_', ' ').str.capitalize()
            data.drop(["Id"], axis=1, inplace=True)
            return data


        model = load_model()
        data = load_dataframe()

        # Affichage d'un graphique interactif
        st.header("Graphique interactif")
        selected_x = st.selectbox("Sélectionnez la variable X :", data.columns)
        selected_y = st.selectbox("Sélectionnez la variable Y :", data.columns)

        if selected_x and selected_y:
            fig, ax = plt.subplots()
            sns.scatterplot(data=data, x=selected_x, y=selected_y, ax=ax)
            st.pyplot(fig)

        # Ajout d'un histogramme
        st.header("Histogramme")
        selected_numeric_column = st.selectbox(
            "Sélectionnez une colonne numérique :", data.select_dtypes("number").columns)
        num_bins = st.slider("Nombre de bacs", min_value=5, max_value=50)

        # Par cette ligne
        fig, ax = plt.subplots()
        hist = plt.hist(data[selected_numeric_column],
                        bins=num_bins, edgecolor="k")
        st.pyplot(fig)



        feature_importance = model.get_feature_importance()
        sorted_idx = np.argsort(feature_importance)
        fig, ax = plt.subplots()

        ax.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center')
        ax.set_facecolor("white")
        ax.set_yticks(range(0,len(sorted_idx)))
        ax.set_yticklabels(np.array(model.feature_names_)[sorted_idx])

        ax.set_title('Feature Importance')
        st.pyplot(fig, use_container_width=True)
