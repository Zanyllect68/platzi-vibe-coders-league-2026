-- ============================================================
-- Esquema SQL: contracts_leads (versión extendida)
-- Ejecutar en el SQL Editor del panel de Supabase
-- ============================================================

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

DROP TABLE IF EXISTS public.contracts_leads;

CREATE TABLE public.contracts_leads (
  id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- 1. DATOS DE LAS PARTES
  nombre_freelancer       TEXT            NOT NULL,
  email_freelancer        TEXT            NOT NULL,
  nombre_cliente          TEXT            NOT NULL,
  identificacion_cliente  TEXT            NOT NULL,

  -- 2. DETALLES DEL PROYECTO Y PAGO
  titulo_proyecto         TEXT            NOT NULL,
  descripcion_entregables TEXT            NOT NULL,
  tipo_tarifa             TEXT            NOT NULL CHECK (tipo_tarifa IN (
                            'por_hora', 'precio_fijo', 'mensual'
                          )),
  monto_tarifa            DECIMAL(12,2)   NOT NULL CHECK (monto_tarifa > 0),
  moneda                  TEXT            NOT NULL CHECK (moneda IN (
                            'USD', 'EUR', 'COP', 'MXN', 'ARS', 'CLP', 'PEN', 'UYU'
                          )),
  forma_pago              TEXT            NOT NULL CHECK (forma_pago IN (
                            '50_50', '100_final', 'hitos_mensuales'
                          )),

  -- 3. TIEMPOS Y LEGALES
  fecha_inicio            DATE            NOT NULL,
  fecha_fin_estimada      DATE            NOT NULL,
  propiedad_intelectual   TEXT            NOT NULL CHECK (propiedad_intelectual IN (
                            'pasa_al_cliente', 'retiene_freelancer'
                          )),
  clausula_rescision_dias INTEGER         NOT NULL CHECK (clausula_rescision_dias > 0),

  creado_en               TIMESTAMPTZ     NOT NULL DEFAULT NOW(),

  CONSTRAINT fin_despues_de_inicio CHECK (fecha_fin_estimada >= fecha_inicio)
);

ALTER TABLE public.contracts_leads ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Permitir inserción desde API anónima"
  ON public.contracts_leads
  FOR INSERT
  TO anon
  WITH CHECK (true);

CREATE POLICY "Permitir lectura solo a usuarios autenticados"
  ON public.contracts_leads
  FOR SELECT
  TO authenticated
  USING (true);
