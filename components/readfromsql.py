import os
import sys
import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from models.model import Base, ClassType, CustomerType, CustomerSatisfaction, Gender, TravelType

""" 

"""
def read_from_sqlite():
    engine = create_engine("sqlite:///data/airline_database.sqlite")
    Session = sessionmaker(bind=engine)

    with Session.begin() as session:
        result = session.query(
                    CustomerSatisfaction.id,
                    Gender.gender,
                    CustomerType.customer_type,
                    CustomerSatisfaction.age,
                    TravelType.travel_type,
                    ClassType.class_type,
                    CustomerSatisfaction.flight_distance, 
                    CustomerSatisfaction.inflight_wifi_service, 
                    CustomerSatisfaction.departure_arrival_time_convenient, 
                    CustomerSatisfaction.ease_of_online_booking, 
                    CustomerSatisfaction.gate_location, 
                    CustomerSatisfaction.food_and_drink, 
                    CustomerSatisfaction.online_boarding, 
                    CustomerSatisfaction.seat_comfort, 
                    CustomerSatisfaction.inflight_entertainment, 
                    CustomerSatisfaction.on_board_service, 
                    CustomerSatisfaction.leg_room_service, 
                    CustomerSatisfaction.baggage_handling, 
                    CustomerSatisfaction.checkin_service, 
                    CustomerSatisfaction.inflight_service, 
                    CustomerSatisfaction.cleanliness, 
                    CustomerSatisfaction.departure_delay_in_minutes, 
                    CustomerSatisfaction.arrival_delay_in_minutes, 
        ).join(Gender, Gender.id == CustomerSatisfaction.id_gender).join(
                CustomerType, CustomerType.id == CustomerSatisfaction.id_customer_type).join(
                TravelType, TravelType.id == CustomerSatisfaction.id_travel_type).join(
                ClassType, ClassType.id == CustomerSatisfaction.id_class_type).all()

        df = pd.DataFrame(result)

    return df

if __name__ == '__main__':
    read_from_sqlite()