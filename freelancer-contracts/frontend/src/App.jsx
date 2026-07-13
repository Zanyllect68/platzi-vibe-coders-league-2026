import { FileCheck, ShieldCheck, Timer } from 'lucide-react'
import ContractForm from './components/ContractForm'

const highlights = [
  {
    icon: FileCheck,
    title: 'Listo en minutos',
    text: 'Un asistente de 3 pasos que arma tu contrato sin fricción.',
  },
  {
    icon: ShieldCheck,
    title: 'Términos claros',
    text: 'Propiedad intelectual, montos y forma de pago bien definidos.',
  },
  {
    icon: Timer,
    title: 'Pensado para LATAM',
    text: 'Monedas locales, plazos y cláusulas de rescisión adaptadas.',
  },
]

export default function App() {
  return (
    <main className="relative min-h-screen overflow-hidden bg-background">
      <div className="pointer-events-none absolute inset-x-0 top-0 h-[420px] bg-gradient-to-b from-accent/40 to-transparent" />

      <div className="relative mx-auto max-w-5xl px-5 py-14 sm:py-20">
        <header className="text-center">
          <a
            href="https://platzi.com/p/andresfelipegt70/"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-full border border-border bg-card px-4 py-1.5 text-xs font-medium text-muted-foreground shadow-soft transition-colors hover:text-foreground"
          >
            <span className="h-1.5 w-1.5 rounded-full bg-primary" />
            Vibe Coders League 2.0 · Platzi · Votar 🏆
          </a>
          <h1 className="mx-auto mt-6 max-w-2xl font-display text-4xl leading-tight text-foreground sm:text-5xl">
            Contratos freelance claros, en minutos.
          </h1>
          <p className="mx-auto mt-4 max-w-xl text-base text-muted-foreground sm:text-lg">
            Genera un contrato profesional con cláusulas de propiedad intelectual, plazos y
            formas de pago adaptadas al mercado latinoamericano.
          </p>
        </header>

        <div className="mt-12">
          <ContractForm />
        </div>

        <section className="mt-14 grid gap-4 sm:grid-cols-3">
          {highlights.map((h) => {
            const Icon = h.icon
            return (
              <div
                key={h.title}
                className="rounded-2xl border border-border bg-card/60 p-5 shadow-soft"
              >
                <Icon className="h-5 w-5 text-primary" />
                <h3 className="mt-3 font-medium text-foreground">{h.title}</h3>
                <p className="mt-1 text-sm text-muted-foreground">{h.text}</p>
              </div>
            )
          })}
        </section>

        <footer className="mt-16 text-center text-sm text-muted-foreground">
          Hecho con 💻 para la Vibe Coders League 2.0 de Platzi
        </footer>
      </div>
    </main>
  )
}
