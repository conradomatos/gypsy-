---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura, nomenclatura]
revisado: 2026-07-19
---

# Convenções de nomenclatura — Gypsy

**Idioma:** **inglês** para código, banco de dados e API; **português (PT-BR)** para
interface e documentação em `docs/`. Nome do produto: **Gypsy** ("CostAI" é branding
antigo — só em docs arquivados/histórico). Regra do projeto: `nomenclatura` (`.claude/rules/`).

## Banco de dados (PostgreSQL)

### Tabelas
- Inglês, snake_case, plural: `materials`, `labor_roles`, `equipment`, `pricebooks`
- Junção: `assembly_items`, `motor_sections`
- Parâmetro: `global_parameters`, `project_parameters`
- Referência: `material_prices`, `social_charges`

### Colunas
- Inglês, snake_case: `power_kw`, `cross_section_mm2`, `hourly_cost`
- Sem prefixo de tabela: `id` (não `material_id` dentro de `materials`)
- FK usa a tabela referenciada no singular: `material_id`, `section_id`, `budget_id`
- Campos padrão: `id`, `created_at`, `updated_at`, `created_by`
  (`created_by` referencia o **modelo de usuário do Django**, não `auth.users`)
- Unidade no nome quando ambíguo: `distance_m`, `power_kw`, `weight_kg`, `area_m2`

### Views / Functions
- View: prefixo `vw_` — `vw_budget_summary`
- Function: prefixo `fn_` — `fn_calculate_cross_section`

> **Autorização não é por RLS.** O controle de acesso é feito na aplicação, por
> **autenticação do Django + permissions do DRF** — não por Row Level Security no banco
> (abordagem Supabase, revogada em 2026-07-19).

## Backend — Python / Django

### Python
- Módulos e pacotes: snake_case — `composicao_hh.py`, `bdi_markup.py`
- Funções e variáveis: snake_case — `calculate_cross_section`, `hourly_cost_without_bdi`
- Classes / dataclasses: PascalCase — `Motor`, `ProjectParameters`, `HourlyCost`
- Constantes: UPPER_SNAKE — `MAX_CONDUIT_FILL_RATIO = 0.40`

### Django
- Apps: snake_case, curto — `budgets`, `dimensioner`, `cost_base`
- Models: singular, PascalCase — `Material`, `LaborRole` (tabela gerada no plural)
- Services/selectors: funções snake_case com verbo — `create_budget`, `get_budget_summary`
- Serializers: `<Model>Serializer` — `MaterialSerializer`

## Frontend — React / TypeScript

### Arquivos
- Páginas / componentes: PascalCase — `DimensionadorForca.tsx`, `MotorCard.tsx`
- Hooks: camelCase com prefixo `use` — `useMotores.ts`
- Módulos utilitários / tipos: kebab-case — `format-currency.ts`, `motor.ts`

### Código
- Variáveis / funções: camelCase — `calculateCrossSection`, `hourlyCostWithoutBdi`
- Constantes: UPPER_SNAKE — `MAX_CONDUIT_FILL_RATIO`
- Tipos / interfaces: PascalCase — `Motor`, `ProjectParameters`, `HourlyCost`
- Rotas: kebab-case — `/operational-costs/mob-demob`

## Documentação (`docs/`)
- Pastas: MAIÚSCULO
- Notas: `COD_descricao_minuscula.md` (código em MAIÚSCULO, descrição minúscula sem acento)
- Idioma: português (PT-BR)

> **Referências históricas:** menções à nomenclatura da era Supabase (RLS, `auth.users`)
> podem permanecer em `_historico/` e no `registro_de_decisoes.md` quando necessárias para
> explicar a migração — nunca como orientação vigente.
