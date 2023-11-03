import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from components.readfromsql import read_from_sqlite
from catboost import CatBoostClassifier


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
