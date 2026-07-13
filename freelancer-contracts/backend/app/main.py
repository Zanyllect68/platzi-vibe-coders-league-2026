from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .config import supabase
from .schemas import ContractCreate, ContractResponse

app = FastAPI(
    title="Freelancer Contracts API",
    description="API para generación de contratos freelance — Vibe Coders League 2.0",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://freelancer-contracts.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "message": "Freelancer Contracts API v2 running"}

@app.post("/api/generate-contract", status_code=201, response_model=ContractResponse)
def create_contract(contract: ContractCreate):
    if supabase is None:
        raise HTTPException(
            status_code=500,
            detail="Error de configuración: Supabase no está conectado",
        )

    # Convertir fechas a string ISO para Supabase
    payload = contract.model_dump()
    payload["fecha_inicio"] = payload["fecha_inicio"].isoformat()
    payload["fecha_fin_estimada"] = payload["fecha_fin_estimada"].isoformat()

    try:
        result = supabase.table("contracts_leads").insert(payload).execute()
        return ContractResponse(
            message="Contrato registrado exitosamente",
            data=result.data,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error de base de datos: {str(e)}",
        )
