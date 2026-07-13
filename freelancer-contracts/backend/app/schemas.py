from datetime import date
from pydantic import BaseModel, Field, field_validator
from typing import Literal

# ── Enums replicados en backend y frontend ──

TIPO_TARIFAS = Literal["por_hora", "precio_fijo", "mensual"]
MONEDAS = Literal["USD", "EUR", "COP", "MXN", "ARS", "CLP", "PEN", "UYU"]
FORMAS_PAGO = Literal["50_50", "100_final", "hitos_mensuales"]
PROPIEDAD_INTELECTUAL = Literal["pasa_al_cliente", "retiene_freelancer"]

ETIQUETAS = {
    "tipo_tarifa": {
        "por_hora": "Por hora",
        "precio_fijo": "Precio fijo",
        "mensual": "Mensual / Retainer",
    },
    "moneda": {
        "USD": "USD (Dólar)",
        "EUR": "EUR (Euro)",
        "COP": "COP (Peso colombiano)",
        "MXN": "MXN (Peso mexicano)",
        "ARS": "ARS (Peso argentino)",
        "CLP": "CLP (Peso chileno)",
        "PEN": "PEN (Sol peruano)",
        "UYU": "UYU (Peso uruguayo)",
    },
    "forma_pago": {
        "50_50": "50% anticipado y 50% al finalizar",
        "100_final": "100% al finalizar",
        "hitos_mensuales": "Hitos mensuales",
    },
    "propiedad_intelectual": {
        "pasa_al_cliente": "Pasa al cliente al pagar",
        "retiene_freelancer": "La retiene el freelancer",
    },
}


class ContractCreate(BaseModel):
    # ── Sección 1: Partes ──
    nombre_freelancer: str = Field(
        ..., min_length=2, max_length=120,
        description="Nombre completo del freelancer",
    )
    email_freelancer: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Correo del freelancer",
    )
    nombre_cliente: str = Field(
        ..., min_length=2, max_length=120,
        description="Nombre del cliente o empresa",
    )
    identificacion_cliente: str = Field(
        ..., min_length=3, max_length=30,
        description="RUT / RFC / DNI del cliente",
    )

    # ── Sección 2: Proyecto y pago ──
    titulo_proyecto: str = Field(
        ..., max_length=200,
        description="Título del proyecto",
    )
    descripcion_entregables: str = Field(
        ..., max_length=3000,
        description="Descripción de los entregables",
    )
    tipo_tarifa: str = Field(
        ..., description="Tipo de tarifa",
    )
    monto_tarifa: float = Field(
        ..., gt=0, le=9999999.99,
        description="Monto de la tarifa",
    )
    moneda: str = Field(
        ..., description="Moneda del contrato",
    )
    forma_pago: str = Field(
        ..., description="Forma de pago acordada",
    )

    # ── Sección 3: Tiempos y legales ──
    fecha_inicio: date = Field(
        ..., description="Fecha de inicio del proyecto",
    )
    fecha_fin_estimada: date = Field(
        ..., description="Fecha estimada de finalización",
    )
    propiedad_intelectual: str = Field(
        ..., description="Cláusula de propiedad intelectual",
    )
    clausula_rescision_dias: int = Field(
        ..., gt=0, le=365,
        description="Días de preaviso para rescisión",
    )

    # ── Validaciones ──

    @field_validator("titulo_proyecto")
    @classmethod
    def validar_titulo(cls, v: str) -> str:
        if len(v) < 5:
            raise ValueError("El título del proyecto debe tener al menos 5 caracteres")
        return v

    @field_validator("descripcion_entregables")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        if len(v) < 20:
            raise ValueError("La descripción debe tener al menos 20 caracteres")
        return v

    @field_validator("tipo_tarifa")
    @classmethod
    def validar_tipo_tarifa(cls, v: str) -> str:
        if v not in ("por_hora", "precio_fijo", "mensual"):
            raise ValueError("Tipo de tarifa inválido")
        return v

    @field_validator("moneda")
    @classmethod
    def validar_moneda(cls, v: str) -> str:
        validas = ("USD", "EUR", "COP", "MXN", "ARS", "CLP", "PEN", "UYU")
        if v not in validas:
            raise ValueError(f"Moneda inválida. Opciones: {', '.join(validas)}")
        return v

    @field_validator("forma_pago")
    @classmethod
    def validar_forma_pago(cls, v: str) -> str:
        if v not in ("50_50", "100_final", "hitos_mensuales"):
            raise ValueError("Forma de pago inválida")
        return v

    @field_validator("propiedad_intelectual")
    @classmethod
    def validar_propiedad(cls, v: str) -> str:
        if v not in ("pasa_al_cliente", "retiene_freelancer"):
            raise ValueError("Opción de propiedad intelectual inválida")
        return v

    @field_validator("fecha_fin_estimada")
    @classmethod
    def validar_fechas(cls, v: date, info) -> date:
        if "fecha_inicio" in info.data and v < info.data["fecha_inicio"]:
            raise ValueError("La fecha de fin debe ser posterior a la fecha de inicio")
        return v


class ContractResponse(BaseModel):
    message: str
    data: list | None = None
