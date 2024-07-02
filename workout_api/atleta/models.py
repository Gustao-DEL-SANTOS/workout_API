from datetime import datetime
from sqlalchemy import Datetime, Float, Foreignkey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(Datetime, nullable=False)
    categoria: Mapped["CategoriaModel"] = relationship(back_populate="atleta", lazy='selectin')
    categoria_id: Mapped[int] = mapped_column(Foreignkey("categoria.pk_id"))
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(back_populate="atleta", lazy='selectin')
    centro_treinamento_id: Mapped[int] = mapped_column(Foreignkey("centros_treinamento.pk_id"))
