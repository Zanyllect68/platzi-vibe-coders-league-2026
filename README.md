# 🚀 Platzi Vibe Coders League

> Repo multi-proyecto de la **Platzi Vibe Coders League**. Cada carpeta contiene un proyecto independiente con su propio stack, README y documentación.

---

## 📂 Proyectos

| Proyecto | Stack | Descripción | Link |
|----------|-------|-------------|------|
| 🐾 **Patitas Felices** | Next.js 16 · TypeScript · Tailwind · NVIDIA NIM | Asistente virtual IA para una veterinaria y pet shop en Medellín | [`./proyecto 1/`](./proyecto 1/README.md) |

> Próximamente más proyectos se unirán a esta colección.

---

## 🛠️ Patrones del repo

- **Cada proyecto vive en su propia carpeta** y tiene su propio `README.md`.
- **Las dependencias se instalan dentro de la carpeta del proyecto** (no hay `package.json` raíz ni monorepo).
- **Los secretos nunca se suben**: cada proyecto usa su propio `.env.local` o `.env`, todos ya listados en `.gitignore`.

```gitignore
# Patrón común por proyecto
node_modules/
.next/
.env
.env.local
*.log
dist/
build/
```

---

🤝 Aportes y nuevos proyectos son bienvenidos en sus propias carpetas.