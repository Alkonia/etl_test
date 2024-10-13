from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base import BaseConnection


class Multiplex(BaseConnection):
    __tablename__ = 'multiplex'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    descripcion = Column(String(100), nullable=False)
    direccion = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
