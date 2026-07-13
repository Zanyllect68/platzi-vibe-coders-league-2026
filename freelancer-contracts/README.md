# 📄 Freelancer Contracts — Generador de Contratos

> **Proyecto 2** — Vibe Coders League 2.0 (Platzi)
> Stack: React 18 + Vite + Tailwind CSS 3 | Python FastAPI | Supabase (PostgreSQL) | Vercel (Frontend) | Railway (Backend)

## 📋 Propuesta

| | |
|:---|:---|
| **¿Qué es?** | Generador de contratos freelance con wizard interactivo de 3 pasos, validación de datos en backend y almacenamiento seguro en Supabase. |
| **¿Para quién?** | Freelancers latinoamericanos que trabajan con clientes y necesitan contratos claros con términos legales básicos. |
| **¿Por qué importa?** | Reduce la fricción de empezar un proyecto freelance al tener un contrato listo en minutos, incluyendo cláusulas de propiedad intelectual, plazos, montos y formas de pago adaptadas al mercado local. |

---

## 🏗️ Arquitectura

```
React (Vite)  ──fetch──▶  FastAPI (API Gateway)  ──insert──▶  Supabase (PostgreSQL)
  :5173                    :8000                            kmzlfuaufmgvmlzatlnk
```

## 📁 Estructura del Proyecto

```
freelancer-contracts/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI + CORS + endpoint /api/generate-contract
│   │   ├── config.py        # Conexión a Supabase (variables de entorno)
│   │   └── schemas.py       # Pydantic models con validaciones
│   ├── requirements.txt
│   ├── .env                 # SUPABASE_URL + SUPABASE_KEY
│   └── supabase-schema.sql  # CREATE TABLE + RLS policies
│
└── frontend/
    ├── src/
    │   ├── components/
    │   │   └── ContractForm.jsx   # Wizard de 3 pasos con estados idle/loading/success
    │   ├── App.jsx                # Layout principal
    │   ├── index.css              # Tailwind + animaciones
    │   └── main.jsx
    ├── index.html
    ├── vite.config.js             # Proxy /api → localhost:8000
    ├── tailwind.config.js
    └── package.json
```

---

## 🚀 Instalación y Ejecución

### 1. Requisitos

- Python 3.13+
- Node.js 18+
- Una cuenta en [Supabase](https://supabase.com) con un proyecto creado

### 2. Base de Datos (Supabase)

1. Ve a tu [Supabase Dashboard](https://supabase.com/dashboard/project/kmzlfuaufmgvmlzatlnk)
2. Abre el **SQL Editor**
3. Pega y ejecuta el contenido de `backend/supabase-schema.sql`
4. Ve a **Project Settings → API** y copia la **`anon public` key**

### 3. Backend

```bash
cd backend
cp .env.example .env
# Editar .env con SUPABASE_URL y SUPABASE_KEY reales
pip install -r requirements.txt
uvicorn app.main:app --reload
```

El backend arranca en `http://localhost:8000`. Documentación interactiva en `http://localhost:8000/docs`.

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

El frontend arranca en `http://localhost:5173`. El `vite.config.js` tiene proxy configurado para que `/api` redirija al backend automáticamente.

---

## 📋 API Endpoint

### `POST /api/generate-contract`

**Request body:**

```json
{
  "nombre_freelancer": "Ana Pérez",
  "email_freelancer": "ana@ejemplo.com",
  "nombre_cliente": "TechCorp SAS",
  "identificacion_cliente": "12.345.678-9",
  "titulo_proyecto": "Rediseño de plataforma e-commerce",
  "descripcion_entregables": "Diseño UX/UI completo con 5 pantallas, prototipo navegable y entrega en Figma.",
  "tipo_tarifa": "precio_fijo",
  "monto_tarifa": 4500,
  "moneda": "COP",
  "forma_pago": "50_50",
  "fecha_inicio": "2026-08-01",
  "fecha_fin_estimada": "2026-09-15",
  "propiedad_intelectual": "pasa_al_cliente",
  "clausula_rescision_dias": 15
}
```

**Response:** `201 Created`
```json
{
  "message": "Contrato registrado exitosamente",
  "data": [{ ... }]
}
```

**Validaciones incluidas:**
- Título del proyecto: mínimo 5 caracteres
- Descripción: mínimo 20 caracteres
- `tipo_tarifa`: `por_hora`, `precio_fijo`, `mensual`
- `moneda`: `USD`, `EUR`, `COP`, `MXN`, `ARS`, `CLP`, `PEN`, `UYU`
- `forma_pago`: `50_50`, `100_final`, `hitos_mensuales`
- `propiedad_intelectual`: `pasa_al_cliente`, `retiene_freelancer`
- `fecha_fin_estimada` debe ser >= `fecha_inicio`
- `monto_tarifa` > 0
- `clausula_rescision_dias` entre 1 y 365

---

## 🧩 Frontend — Wizard de 3 Pasos

| Paso | Sección | Campos |
|:---:|:---|:---|
| 1 | Datos de las Partes | nombre_freelancer, email_freelancer, nombre_cliente, identificacion_cliente |
| 2 | Proyecto y Pago | titulo_proyecto, descripcion_entregables, tipo_tarifa, monto_tarifa, moneda, forma_pago |
| 3 | Tiempos y Legales | fecha_inicio, fecha_fin_estimada, propiedad_intelectual, clausula_rescision_dias |

**Estados:** `idle` → formulario editable | `loading` → spinner + campos deshabilitados | `success` → pantalla de confirmación con CTA para votar en Platzi.

---

## 🗄️ Esquema de Base de Datos

```sql
CREATE TABLE public.contracts_leads (
  id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  nombre_freelancer       TEXT NOT NULL,
  email_freelancer        TEXT NOT NULL,
  nombre_cliente          TEXT NOT NULL,
  identificacion_cliente  TEXT NOT NULL,
  titulo_proyecto         TEXT NOT NULL,
  descripcion_entregables TEXT NOT NULL,
  tipo_tarifa             TEXT NOT NULL CHECK (...),
  monto_tarifa            DECIMAL(12,2) NOT NULL CHECK (monto_tarifa > 0),
  moneda                  TEXT NOT NULL CHECK (...),
  forma_pago              TEXT NOT NULL CHECK (...),
  fecha_inicio            DATE NOT NULL,
  fecha_fin_estimada      DATE NOT NULL,
  propiedad_intelectual   TEXT NOT NULL CHECK (...),
  clausula_rescision_dias INTEGER NOT NULL CHECK (...),
  creado_en               TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  CONSTRAINT fin_despues_de_inicio CHECK (fecha_fin_estimada >= fecha_inicio)
);
```

Row Level Security activado con políticas para INSERT anónimo y SELECT autenticado.

---

## 🌐 Deploy

| Capa | Servicio | URL |
|:---|:---|---:|
| Frontend | Vercel | `https://platzi-vibe-coders-league-2026.vercel.app` |
| Backend | Railway | Asignada por Railway al desplegar |
| Base de Datos | Supabase | `kmzlfuaufmgvmlzatlnk.supabase.co` |

### Variables de entorno en producción

**Vercel (Frontend):**
```
VITE_API_URL=https://<railway-url>.up.railway.app/api
```

**Railway (Backend):**
```
SUPABASE_URL=https://kmzlfuaufmgvmlzatlnk.supabase.co
SUPABASE_KEY=<anon-key>
```

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología |
|:---|:---|
| Frontend | React 18, Vite 6, Tailwind CSS 3 |
| Backend | Python 3.13, FastAPI, Pydantic v2 |
| Base de Datos | Supabase (PostgreSQL) |
| API Client | supabase-py 2.5 |
| Deploy Frontend | Vercel |
| Deploy Backend | Railway |

---

*Hecho con 💻 para la Vibe Coders League 2.0 de Platzi*
