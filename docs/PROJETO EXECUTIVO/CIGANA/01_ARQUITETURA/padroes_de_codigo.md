---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura, padroes]
revisado: 2026-07-19
---

# Padrões de código — Gypsy

> **Escopo:** princípios de como escrever código nas três camadas. Nomes de pastas de
> código **ainda não estão congelados** — as estruturas abaixo são **PROPOSTO** até o
> scaffold ser aprovado no subprojeto correspondente.
> Stack em [`stack_tecnica.md`](stack_tecnica.md) · nomenclatura em
> [`convencoes_nomenclatura.md`](convencoes_nomenclatura.md).
> Versão anterior (engines TS + Supabase + RLS) em
> [`_HISTORICO/`](_HISTORICO/padroes_de_codigo.supabase.2026-04-04.md).

## Regra mãe: separação de responsabilidades

Cálculo não conhece web. Web não conhece cálculo. O que os liga é a camada de serviço.

```
Frontend (React)  →  API (DRF)  →  Services (regra de negócio)  →  Engine (cálculo puro)
                                          ↑
                                     Models (ORM/persistência)
```

---

## Backend — Python + Django + DRF

- **Separação por domínio:** organizar por área de negócio (orçamento, dimensionador,
  base de custos, parâmetros…), não por tipo técnico.
- **Services concentram a regra de negócio.** Uma operação de escrita não-trivial vive
  num service, não no serializer nem na view.
- **Leitura via selectors/queries dedicados** quando a consulta for não-trivial — manter
  querysets complexos fora das views.
- **Serializers e views são finos:** serializer valida e (de)serializa; view orquestra
  (autentica, chama service/selector, devolve). Nenhum dos dois carrega o núcleo da regra.
- **Migrations controladas:** revisadas, nomeadas, uma intenção por migration.
- **Autorização** por auth do Django + permissions do DRF. Não usar RLS como mecanismo
  principal de autorização (era Supabase, revogado).

Estrutura de exemplo (**PROPOSTO** — não congelar):

```
backend/
  <dominio>/
    models.py
    services.py       # regra de negócio (escrita)
    selectors.py      # consultas (leitura)
    serializers.py    # (de)serialização + validação
    views.py          # orquestração DRF
    migrations/
```

---

## Engine — Python puro (regra inviolável)

- **Python puro, isolado do Django.** Sem `import django`, sem ORM, sem HTTP, sem I/O.
- **Entra dado, sai resultado.** Recebe dataclasses/dicts, devolve resultado. Sem efeito
  colateral, **determinístico**.
- **`Decimal` para dinheiro — nunca `float`.** Arredondamento explícito onde a norma/HOLLOS
  exigir.
- **Teste obrigatório (pytest).** Engine sem teste não mergeia.
- **Golden test:** o orçamento de referência reproduzido pelo engine bate a HOLLOS em
  **R$ 216.188,04**; divergência item a item tem de ser explicável.
- **Dados normativos (NBR 5410/14039/5419)** ficam em **estrutura própria do engine**,
  como constantes versionadas — não no banco, não por tenant. (Local exato: **PROPOSTO**,
  a fixar no subprojeto do engine.)
- **Rastreabilidade:** todo número carrega fonte, data-base e flag de imposto quando
  aplicável (ver regra do projeto `rastreabilidade-precos`).

Estrutura de exemplo (**PROPOSTO** — não congelar):

```
engine/
  <modulo>/            # composicao_hh, bdi, dimensionador, ...
  data/                # tabelas normativas (constantes)
  tests/               # pytest, casos do Sandro + valores HOLLOS
```

---

## Frontend — React + TypeScript

- **TypeScript strict.** Nunca `any` nem `@ts-ignore`.
- **Vite + Tailwind + shadcn/ui** como base (ver `stack_tecnica.md`).
- **Componentes reutilizáveis**, coerentes com um **design system** (a firmar junto com
  os mockups — SP-02).
- **Chamadas à API ficam fora dos componentes visuais.** A camada de dados (client da API,
  hooks de fetching) é separada do componente que só apresenta.
- **Validação de dados** na entrada de formulários e nas fronteiras da API.
- O frontend consome **exclusivamente a API REST** — nunca acessa banco diretamente.

Estrutura de exemplo (**PROPOSTO** — não congelar): definida no SP-02/scaffold do frontend.

---

## Anti-patterns (não fazer)

- Regra de cálculo dentro de view, serializer, componente React ou template.
- `float` para dinheiro.
- Engine importando Django/ORM/HTTP.
- Frontend acessando banco direto ou embutindo lógica de custo.
- Número sem fonte/data-base (ver `rastreabilidade-precos`).
- Parâmetro (alíquota, encargo, fator) hardcoded no código (ver `parametros-nao-hardcode`).
- Copiar fórmula da HOLLOS às cegas — dimensionamento vem da norma.
