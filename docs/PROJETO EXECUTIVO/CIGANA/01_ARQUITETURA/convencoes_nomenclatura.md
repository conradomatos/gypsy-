---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Convenções de nomenclatura — Gypsy

## Banco de dados (Supabase/PostgreSQL)

### Tabelas
- Inglês, snake_case, plural: `materials`, `labor_roles`, `equipment`, `pricebooks`
- Tabelas de junção: `assembly_items`, `motor_sections`
- Tabelas de parâmetro: `global_parameters`, `project_parameters`
- Tabelas de referência: `material_prices`, `social_charges`

### Colunas
- Inglês, snake_case: `power_kw`, `cross_section_mm2`, `hourly_cost`
- Sem prefixo de tabela: `id` (não `material_id` dentro de `materials`)
- FK usa nome da tabela referenciada no singular: `material_id`, `section_id`, `budget_id`
- Campos padrão em toda tabela: `id` (UUID), `created_at`, `updated_at`, `created_by`
- Unidades no nome quando ambíguo: `distance_m`, `power_kw`, `weight_kg`, `area_m2`

### Views
- Prefixo `vw_`: `vw_budget_summary`, `vw_consolidated_bom`

### Functions
- Prefixo `fn_`: `fn_calculate_cross_section`, `fn_estimate_crew`

### Policies RLS
- Nome descritivo entre aspas: `"authenticated_select_own"`

## Frontend (TypeScript/React)

### Arquivos
- Páginas: PascalCase `DimensionadorForca.tsx`
- Hooks: camelCase com prefixo use `useMotores.ts`
- Engines: kebab-case `composicao-hh.ts`
- Types: kebab-case `motor.ts`
- Componentes: PascalCase `MotorCard.tsx`

### Variáveis e funções
- camelCase: `calculateCrossSection`, `hourlyCostWithoutBdi`
- Constantes: UPPER_SNAKE: `MAX_CONDUIT_FILL_RATIO = 0.40`
- Tipos/Interfaces: PascalCase: `Motor`, `ProjectParameters`, `HourlyCost`

### Rotas
- kebab-case: `/operational-costs/mob-demob`

## Obsidian (documentação)
- Pastas: MAIÚSCULO
- Notas: `COD_descricao_minuscula.md` (código em MAIÚSCULO, descrição minúscula sem acento)
