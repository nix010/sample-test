from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

from dependency import engine

Base = declarative_base()


# Club model
class Club(Base):
    __tablename__ = "clubs"

    club_id = Column(Integer, primary_key=True)
    club_code = Column(String(255))
    name = Column(String(255))
    domestic_competition_id = Column(String(255))
    total_market_value = Column(DECIMAL(10, 2))
    squad_size = Column(Integer)
    average_age = Column(Integer)
    foreigners_number = Column(Integer)
    foreigners_percentage = Column(DECIMAL(10, 2))
    national_team_players = Column(Integer)
    stadium_name = Column(String(255))
    stadium_seats = Column(Integer)
    net_transfer_record = Column(String)
    coach_name = Column(String(255))
    last_season = Column(String(255))
    url = Column(String(255))


Base.metadata.create_all(bind=engine)
