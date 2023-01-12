import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_height = Column(String(250))
    character_hair_color= Column(String(250), nullable=True)
    character_planet_id = Column(Integer, ForeignKey('planet.id'))
    


class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_climate = Column(String(250))
    planet_terrain = Column(String(250), nullable=False)
    planet_population = Column(Integer)
  


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_planet_id = Column(Integer, ForeignKey('planet.id'))
    favorite_character_id = Column(Integer, ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)
 
 
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')