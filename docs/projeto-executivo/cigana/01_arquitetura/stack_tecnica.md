---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
revisado: 2026-07-19
---

# Stack técnica — Gypsy

> **Escopo:** este documento descreve **a arquitetura e as tecnologias que compõem o
> produto**. As ferramentas de desenvolvimento, teste e operação estão em
> [`toolchain.md`](toolchain.md) — não duplicar aqui.
>
> Classificação usada: **DECIDIDO** · **PROPOSTO** · **PENDENTE** · **REVOGADO**.
> Versão anterior (React + Supabase) em [`_historico/`](_historico/stack_tecnica.react-supabase.2026-04-04.md).

## Objetivo da arquitetura

Separar com clareza **apresentação**, **API**, **domínio** e **cálculo**, de modo que o
motor de orçamentação seja auditável e testável isoladamente, e que a interface possa
evoluir sem tocar na lógica de custo. A regra de custo é o ativo crítico do Gypsy — ela
não pode ficar acoplada a framework web, a ORM nem a UI.

## Camadas

```
┌────────────────────────────┐
│ Frontend (React SPA)        │  React + TS + Vite + Tailwind + shadcn/ui
└──────────────┬─────────────┘
               │  API REST (JSON)
┌──────────────▼─────────────┐
│ API (Django REST Framework) │  serializers, views, autenticação, permissões
└──────────────┬─────────────┘
               │  chamadas de domínio
┌──────────────▼─────────────┐
│ Domínio (Django app)        │  models, services (regra de negócio), persistência
└──────────────┬─────────────┘
               │  entra dado puro, sai resultado puro
┌──────────────▼─────────────┐
│ Engine de cálculo (Python)  │  puro, isolado, sem Django/ORM/I/O, Decimal
└────────────────────────────┘
```

- O **frontend** nunca fala com o banco; só com a API REST.
- A **API** orquestra: valida entrada, chama services/engine, serializa a saída.
- O **domínio** detém models e regras de negócio; persiste via ORM do Django.
- O **engine** recebe dados (dataclasses/dicts) e devolve resultado — sem efeitos colaterais.

## Frontend — DECIDIDO

| Tecnologia | Papel |
|---|---|
| React | Framework de UI (SPA) |
| TypeScript | Tipagem estática (strict) |
| Vite | Build e dev server do frontend |
| Tailwind CSS | Estilo utilitário |
| shadcn/ui | Biblioteca de componentes (Radix + Tailwind) |

O frontend consome a API Django/DRF via REST. Bibliotecas de apoio (data-fetching,
formulários, validação, gráficos) serão escolhidas quando as telas forem implementadas
— **não decididas nesta etapa**.

## Backend — DECIDIDO

| Tecnologia | Papel |
|---|---|
| Django | Framework de aplicação (models, admin, auth) |
| Django REST Framework | Camada de API REST |
| PostgreSQL | Banco de dados relacional |
| uv | Gerência de Python e dependências |

**Autorização:** autenticação do Django + permissions do DRF. **RLS não é o mecanismo de
autorização** da aplicação (era a abordagem Supabase, revogada).

## Engine de cálculo — DECIDIDO

- **Python puro**, em pacote próprio, **isolado do Django**.
- **Sem ORM, sem HTTP, sem leitura/gravação em banco, sem I/O** dentro das funções de cálculo.
- Funções **determinísticas** — mesma entrada, mesma saída.
- **Valores monetários em `Decimal`, nunca `float`.**
- **Testável diretamente** (pytest), incluindo o **golden test** contra a HOLLOS
  (R$ 216.188,04). Detalhe de padrões em [`padroes_de_codigo.md`](padroes_de_codigo.md).

## Integração frontend ↔ backend — DECIDIDO / PROPOSTO

- **DECIDIDO:** contrato via **API REST** (JSON).
- **PROPOSTO** (validar quando o código começar): documentação **OpenAPI** gerada por
  **DRF-Spectacular** e **geração automática de cliente TypeScript** a partir do schema.
  Ver [`toolchain.md`](toolchain.md).

## Desenvolvimento e produção

- **Local-first (DECIDIDO):** roda na máquina do Conrado — Postgres local, API local,
  frontend local — até a validação do MVP. Local ≠ mock: banco e API de verdade.
- **Produção (PENDENTE):** nenhuma infraestrutura de produção (VPS/PaaS/cloud) foi
  escolhida. A decisão fica para depois do golden test e da definição de requisitos de
  segurança, backup, observabilidade e custo. Ver [`deploy_pipeline.md`](deploy_pipeline.md).

## Tecnologias revogadas (REVOGADO — 2026-07-19)

Não usar, não recomendar em documentação vigente: **Supabase**, **Edge Functions**,
**Deno**, **cliente Supabase**, **backend no Supabase**, **RLS como autorização principal**,
**Coolify**. Histórico preservado em [`_historico/`](_historico/).

## Tecnologias propostas (PROPOSTO — não decididas)

OpenAPI, DRF-Spectacular, cliente TypeScript gerado, Ruff, Pyright, pytest, Vitest,
Playwright, Storybook, GitHub Actions, observabilidade. Finalidade e critério de
validação de cada uma em [`toolchain.md`](toolchain.md). Registrá-las aqui **não** as
torna decisão.
