from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, Integer, DateTime, String
from db.base import BaseConnection


class VentaTaquilla(BaseConnection):
    __tablename__ = 'ventas_taquilla'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    id_fecha: Mapped[int] = mapped_column(ForeignKey("fechas.id"))
    id_multiplex: Mapped[int] = mapped_column(ForeignKey("multiplex.id"))
    id_pelicula: Mapped[int] = mapped_column(ForeignKey("peliculas.id"))
    id_sala: Mapped[int] = mapped_column(ForeignKey("salas.id"))
    hora_funcion = Column(String(100), nullable=False)
    valor = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
