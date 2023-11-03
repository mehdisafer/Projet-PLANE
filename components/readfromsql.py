import os
import sys
import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from models.model import Base, ClassType, CustomerType, CustomerSatisfaction, Gender, TravelType, Satisfaction

engine = create_engine("sqlite:///data/airline_database.sqlite")


def read_from_sqlite():
    """Reads all data from the SQLite database.

    Returns:
        A Pandas DataFrame containing all data from the database.
    """
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
            Satisfaction.satisfaction
        ).join(Gender, Gender.id == CustomerSatisfaction.id_gender).join(
            CustomerType, CustomerType.id == CustomerSatisfaction.id_customer_type).join(
            TravelType, TravelType.id == CustomerSatisfaction.id_travel_type).join(
            Satisfaction, Satisfaction.id == CustomerSatisfaction.id_satisfaction).join(
            ClassType, ClassType.id == CustomerSatisfaction.id_class_type).all()

        df = pd.DataFrame(result)

    return df


def get_gender(filter=None):
    """Gets all genders from the database, or a specific gender if a filter is provided.

    Args:
        filter: A string filter for the gender.

    Returns:
        A list of strings containing all genders from the database, or a specific gender if a filter is provided.
    """
    Session = sessionmaker(bind=engine)

    with Session.begin() as session:
        if filter:
            result = session.query(Gender.id).filter_by(gender=filter).all()
        else:
            result = session.query(Gender.gender).all()
    return result


def get_customer_type(filter=None):
    """Gets all genders from the database, or a specific gender if a filter is provided.

    Args:
        filter: A string filter for the gender.

    Returns:
        A list of strings containing all genders from the database, or a specific gender if a filter is provided.
    """
    Session = sessionmaker(bind=engine)

    with Session.begin() as session:
        if filter:
            result = session.query(CustomerType.id).filter_by(
                customer_type=filter).all()
        else:
            result = session.query(CustomerType.customer_type).all()
    return result


def get_travel_type(filter=None):
    """Gets all genders from the database, or a specific gender if a filter is provided.

    Args:
        filter: A string filter for the gender.

    Returns:
        A list of strings containing all genders from the database, or a specific gender if a filter is provided.
    """
    Session = sessionmaker(bind=engine)

    with Session.begin() as session:
        if filter:
            result = session.query(TravelType.id).filter_by(
                travel_type=filter).all()
        else:
            result = session.query(TravelType.travel_type).all()
    return result


def get_class_type(filter=None):
    """Gets all genders from the database, or a specific gender if a filter is provided.

    Args:
        filter: A string filter for the gender.

    Returns:
        A list of strings containing all genders from the database, or a specific gender if a filter is provided.
    """
    Session = sessionmaker(bind=engine)

    with Session.begin() as session:
        if filter:
            result = session.query(ClassType.id).filter_by(
                class_type=filter).all()
        else:
            result = session.query(ClassType.class_type).all()
    return result


if __name__ == '__main__':
    print(read_from_sqlite())