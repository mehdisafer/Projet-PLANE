import streamlit as st
from components.readfromsql import get_gender, get_class_type, get_customer_type, get_travel_type

st.title('Prediction de la :blue[satisfaction du client] :sunglasses:')

def evaluation():
    return range(6)

# Colonne à gauche
with st.sidebar:
    deroulant = st.selectbox("Choisir :",["Formulaire","Graphique","About-us"])

if deroulant == "Formulaire":
    st.header("Fomulaire de satisfaction - Client")

    st.selectbox("Genre", [gender[0] for gender in get_gender()])
    st.selectbox("Type de Client", [customer_type[0]
                for customer_type in get_customer_type()])
    st.selectbox("Classe", [class_type[0] for class_type in get_class_type()])
    st.selectbox("Type de Voyage", [travel_type[0]
                for travel_type in get_travel_type()])


    st.text_input("L'âge:")
    st.text_input("Distance de vol:")
    st.text_input("Retard de départ en minutes:")
    st.text_input("Retard d'arrivée en minutes:")

    st.radio('Service Wifi en Vol:', evaluation(), horizontal=True)
    st.radio('Heure de départ/arrivée pratique:', evaluation(), horizontal=True)
    st.radio('Facilité de réservation en ligne:', evaluation(), horizontal=True)
    st.radio('Emplacement de la porte:', evaluation(), horizontal=True)
    st.radio('Nourriture et boissons:', evaluation(), horizontal=True)
    st.radio('Embarquement en ligne:', evaluation(), horizontal=True)
    st.radio('Confort du siège:', evaluation(), horizontal=True)
    st.radio('Divertissement à bord:', evaluation(), horizontal=True)
    st.radio('Service à board:', evaluation(), horizontal=True)
    st.radio('Service de chambre pour le jamble:', evaluation(), horizontal=True)
    st.radio('Gestion des bagages:', evaluation(), horizontal=True)
    st.radio('Service d\'enregistrement:', evaluation(), horizontal=True)
    st.radio('Service en vol:', evaluation(), horizontal=True)
    st.radio('Propreté:', evaluation(), horizontal=True)


if deroulant == "Graphique":
    st.header("Graphique")