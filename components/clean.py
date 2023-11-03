import pandas as pd

def clean(df):

    # conversion des noms de colonnes en minuscule
    df.columns = df.columns.str.lower()
    df.drop(["departure_delay_in_minutes"], axis=1, inplace=True)
    df.drop(["id"], axis=1, inplace=True)

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

    return df