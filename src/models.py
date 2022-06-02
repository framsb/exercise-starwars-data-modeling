import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    mail = Column(String(30), nullable=False)
    address = Column(String(260))
    number = Column(String(30), nullable=False)
    daycreation = Column(String(60), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer,primary_key=True)
    name = Column(String(60), nullable=False)
    location = Column(String(60), nullable=False)
    weight = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    fauna = Column(String(60), nullable=False)
    race = Column(String(60), nullable=False)
 
class Characters(Base):
    __tablename__= "characters"
    id = Column(Integer,primary_key=True)
    name = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    gender = Column(String(60),nullable=False)
    eyes = Column(String(60), nullable=False)
    hair = Column(String(60),nullable=False)
    birth_year = Column(String(60), nullable=False)

class Favorite_Character(Base):
    __tablename__="favorite_character"
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.id'))
    characterid = Column(Integer, ForeignKey('characters.id'))

class Favorite_planets(Base):
    __tablename__="favorite_planets"
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.id'))
    planetid = Column(Integer, ForeignKey('planets.id'))

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')