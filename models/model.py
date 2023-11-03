from sqlalchemy import Integer, String, ForeignKey, Column, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(String(15))


class CustomerType(Base):
    __tablename__ = 'customer_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_type = Column(String(50))


class TravelType(Base):
    __tablename__ = 'travel_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    travel_type = Column(String(50))


class ClassType(Base):
    __tablename__ = 'class_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_type = Column(String(50))


class Satisfaction(Base):
    __tablename__ = 'satisfaction'
    id = Column(Integer, primary_key=True, autoincrement=True)
    satisfaction = Column(String(50))


class CustomerSatisfaction(Base):
    __tablename__ = 'customer_satisfaction'

    id = Column(Integer, primary_key=True)
    id_gender = Column(Integer, ForeignKey('gender.id'))
    id_customer_type = Column(Integer, ForeignKey('customer_type.id'))
    id_class_type = Column(Integer, ForeignKey('class_type.id'))
    id_travel_type = Column(Integer, ForeignKey('travel_type.id'))
    id_satisfaction = Column(Integer, ForeignKey('satisfaction.id'))

    age = Column(Integer)
    flight_distance = Column(Integer)
    inflight_wifi_service = Column(Integer)
    departure_arrival_time_convenient = Column(Integer)
    ease_of_online_booking = Column(Integer)
    gate_location = Column(Integer)
    food_and_drink = Column(Integer)
    online_boarding = Column(Integer)
    seat_comfort = Column(Integer)
    inflight_entertainment = Column(Integer)
    on_board_service = Column(Integer)
    leg_room_service = Column(Integer)
    baggage_handling = Column(Integer)
    checkin_service = Column(Integer)
    inflight_service = Column(Integer)
    cleanliness = Column(Integer)
    departure_delay_in_minutes = Column(Integer)
    arrival_delay_in_minutes = Column(Integer)

    gender = relationship("Gender")
    customer_type = relationship("CustomerType")
    class_type = relationship("ClassType")
    travel_type = relationship("TravelType")
    satisfaction = relationship("Satisfaction")
