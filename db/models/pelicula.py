from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base import BaseConnection


class Pelicula(BaseConnection):
    __tablename__ = 'peliculas'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    nombre = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    duracion = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
