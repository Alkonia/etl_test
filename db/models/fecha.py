from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base import BaseConnection


class Fecha(BaseConnection):
    __tablename__ = 'fechas'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    dia = Column(String(100), nullable=False)
    mes = Column(String(100), nullable=False)
    ano = Column(String(100), nullable=False)
    semestre = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
