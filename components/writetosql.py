import os
import sys
import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from models.model import Base, ClassType, CustomerType, CustomerSatisfaction, Gender, TravelType, Satisfaction

def write_to_sqlite():
    engine = create_engine("sqlite:///data/airline_database.sqlite")

    if database_exists(engine.url):
        drop_database(engine.url)

    # Database creation
    create_database(engine.url)
    print("was it create? ", database_exists(engine.url))

    # Tables creation
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    df = pd.read_csv("data/Airline_Dataset.csv")

    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('/', '_')

    with Session() as session:
        for gender in df["gender"].unique():
            new_gender = Gender(gender=gender)
            session.add(new_gender)

        for customer_type in df["customer_type"].unique():
            new_customer_type = CustomerType(customer_type=customer_type)
            session.add(new_customer_type)

        for travel_type in df["type_of_travel"].unique():
            new_travel_type = TravelType(travel_type=travel_type)
            session.add(new_travel_type)

        for class_type in df["class"].unique():
            new_class_type = ClassType(class_type=class_type)
            session.add(new_class_type)

        for satisfaction in df["satisfaction"].unique():
            new_satisfaction = Satisfaction(satisfaction=satisfaction)
            session.add(new_satisfaction)

        session.commit()

        for index, row in df.iterrows():
            gender = session.query(Gender).filter_by(
                gender=row['gender']).first()

            customer_type = session.query(CustomerType).filter_by(
                customer_type=row['customer_type']).first()

            type_of_travel = session.query(TravelType).filter_by(
                travel_type=row['type_of_travel']).first()

            class_type = session.query(ClassType).filter_by(
                class_type=row['class']).first()

            satisfaction = session.query(Satisfaction).filter_by(
                satisfaction=row['satisfaction']).first()

            new_customer = CustomerSatisfaction(
                id=row['id'],
                age=row['age'],
                flight_distance=row['flight_distance'],
                inflight_wifi_service=row['inflight_wifi_service'],
                departure_arrival_time_convenient=row['departure_arrival_time_convenient'],
                ease_of_online_booking=row['ease_of_online_booking'],
                gate_location=row['gate_location'],
                food_and_drink=row['food_and_drink'],
                online_boarding=row['online_boarding'],
                seat_comfort=row['seat_comfort'],
                inflight_entertainment=row['inflight_entertainment'],
                on_board_service=row['on-board_service'],
                leg_room_service=row['leg_room_service'],
                baggage_handling=row['baggage_handling'],
                checkin_service=row['checkin_service'],
                inflight_service=row['inflight_service'],
                cleanliness=row['cleanliness'],
                departure_delay_in_minutes=row['departure_delay_in_minutes'],
                arrival_delay_in_minutes=row['arrival_delay_in_minutes'],
                id_gender=gender.id,
                id_customer_type=customer_type.id,
                id_class_type=class_type.id,
                id_travel_type=type_of_travel.id,
                id_satisfaction=satisfaction.id
            )
            session.add(new_customer)

        session.commit()


if __name__ == '__main__':
    write_to_sqlite()
