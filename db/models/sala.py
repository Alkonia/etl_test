from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base import BaseConnection


class Sala(BaseConnection):
    __tablename__ = 'salas'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    letra_sala = Column(String(100), nullable=False)
    tipo_sala = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
