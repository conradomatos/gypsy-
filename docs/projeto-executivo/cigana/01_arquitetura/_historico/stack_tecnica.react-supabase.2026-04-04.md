> **STATUS: REVOGADO**
>
> - **Stack histórica:** React 18 + TypeScript + Vite + shadcn/ui + Supabase (Postgres managed) + Edge Functions (Deno)
> - **Data da revogação:** 2026-07-19
> - **Decisão substituta:** `../registro_de_decisoes.md` — entrada de 2026-07-19
> - **Motivo:** convergência dos apps da Concept para **Django + DRF + PostgreSQL**; Supabase, Edge Functions, Deno, cliente Supabase e RLS-como-autorização foram abandonados.
> - **Documento vigente:** `../stack_tecnica.md`
>
> Este documento existe **apenas para auditoria e rastreabilidade**. Não orienta implementação.
> Decisões vigentes prevalecem sobre este histórico.

<!-- FIM DO CABECALHO DE HISTORICO -- CONTEUDO ORIGINAL PRESERVADO ABAIXO -->

---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Stack técnica — Gypsy

## Decisão: mesma stack do PWC

Trocar de stack não se justifica. O ganho de velocidade por reaproveitar patterns, skills do Code e infraestrutura existente supera qualquer benefício teórico de outra tecnologia.

## Frontend

| Tecnologia | Versão | Uso |
|---|---|---|
| React | 18 | UI framework |
| TypeScript | 5.x | Tipagem estática |
| Vite | 5.x | Build tool + dev server |
| shadcn/ui | latest | Component library (Radix + Tailwind) |
| Tailwind CSS | 3.x | Utility-first CSS |
| Recharts | 2.x | Gráficos, Monte Carlo, dashboards |
| TanStack Query | 5.x | Server state (useQuery/useMutation) |
| react-hook-form | 7.x | Formulários |
| zod | 3.x | Validação de schemas |
| sonner | latest | Toast notifications |
| date-fns | 2.x | Manipulação de datas |
| Lucide React | latest | Ícones |
| mathjs | latest | Cálculos NBR 5410 (bitola, corrente) |
| Vitest | latest | Testes unitários nos engines |
## Backend / database

| Tecnologia | Detalhes |
|---|---|
| Supabase | Projeto SEPARADO do PWC (novo projeto) |
| PostgreSQL | Via Supabase (managed) |
| RLS | Row Level Security em todas as tabelas |
| Edge Functions | Deno/TypeScript (cálculos pesados, PDF) |
| Auth | Supabase Auth (email/password) |
| Storage | Supabase Storage (planilhas, propostas) |

## Infraestrutura

| Componente | Detalhes |
|---|---|
| VPS | Mesmo do PWC — Hostinger 72.60.13.91 |
| Deploy | Coolify (segundo app, mesmo servidor) |
| Reverse Proxy | Caddy (HTTPS automático) |
| Containers | Docker v28.2.2 |
| CI | GitHub webhooks → Coolify |

## Domínio

A definir. Candidatos: `app.gypsy.com.br` ou `gypsy.powerconcept.com.br`

## O que NÃO herdar do PWC

- God Mode / RBAC complexo — MVP é single-user (Concept), RBAC vem depois
- Integrações externas (Omie, Secullum, Evolution) — Gypsy não tem
- Edge Functions do PWC — Gypsy terá as próprias

## Quando mover cálculo pro servidor

Se o dimensionador pra 500 motores + 200 trechos ficar lento no browser, mover o engine pra Edge Function. A arquitetura `src/engines/` permite isso sem refatorar — TypeScript puro, roda no browser ou no servidor.