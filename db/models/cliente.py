from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base import BaseConnection


class Cliente(BaseConnection):
    __tablename__ = 'clientes'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    tipo_identificacion = Column(String(100), nullable=False)
    identificacion = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    direccion = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=False)
    pais = Column(String(100), nullable=False)
    acumula_puntos = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
