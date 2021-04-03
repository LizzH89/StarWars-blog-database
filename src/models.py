import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favpeople(Base):
    __tablename__ = 'Favoritos_People'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_User = Column(Integer, ForeignKey('user.id'))
    id_People = Column(Integer, ForeignKey('People.id'))

    
class Favplanet(Base):
    __tablename__ = 'Favoritos_Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_User = Column(Integer, ForeignKey('user.id'))
    id_People = Column(Integer, ForeignKey('Planet.id'))



class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True)
    año = Column(String(250), nullable=False)
    ojos = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    color = Column(String(250), nullable=False)
    pelo = Column(String(250), nullable=False)
    vihiculos = Column(String(250), nullable=False)
    altura = Column(String(250), nullable=False)
    gordura = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    gravedad = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    especies = Column(String(250), nullable=False)
    periodo_rotacion = Column(String(250), nullable=False)
    masa = Column(String(250), nullable=False)
    radio = Column(String(250), nullable=False)











    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')