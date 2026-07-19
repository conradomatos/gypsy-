---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

## Orçamentos — Geral (12 tabelas)
| Tabela                     | Rows | Uso                   |
| -------------------------- | ---- | --------------------- |
| budgets                    | 1    | Orçamentos            |
| budget_revisions           | 1    | Revisões              |
| budget_wbs                 | 0    | EAP/WBS               |
| budget_summary             | 1    | Resumo                |
| budget_circuits            | 0    | Circuitos             |
| budget_generated_materials | 0    | Materiais gerados     |
| budget_documents           | 0    | Documentos            |
| budget_histogram           | 0    | Histograma            |
| cashflow_schedule          | 0    | Cronograma financeiro |
| tax_rules                  | 0    | Regras fiscais        |
| markup_rules               | 0    | Markup                |
| budget_regions             | 8    | Regiões               |
## Orçamentos — Materiais (10 tabelas)
| Tabela                         | Rows |
| ------------------------------ | ---- |
| material_catalog               | 0    |
| material_catalog_price_history | 0    |
| material_catalog_variants      | 0    |
| material_variant_price_history | 0    |
| material_groups                | 0    |
| material_categories            | 0    |
| material_subcategories         | 0    |
| material_tags                  | 0    |
| material_catalog_tags          | 0    |
| budget_material_items          | 0    |

## Orçamentos — MO (14 tabelas)
| Tabela                        | Rows      |
| ----------------------------- | --------- |
| labor_roles                   | 0         |
| labor_parameters              | 0         |
| labor_cost_snapshot           | 0         |
| labor_hh_allocations          | 0         |
| budget_labor_groups           | 0         |
| budget_labor_categories       | 0         |
| budget_labor_tags             | 0         |
| budget_labor_charge_sets      | 3         |
| budget_labor_roles_catalog    | 0         |
| budget_labor_catalog_tags     | 0         |
| budget_labor_roles_history    | 0         |
| budget_labor_import_runs      | 0         |
| budget_labor_items            | 0         |
| labor_incidence_* (6 tabelas) | 5-17 rows |
## Orçamentos — Equipamentos (10 tabelas)
| Tabela                     | Rows |
| -------------------------- | ---- |
| equipment_groups           | 0    |
| equipment_categories       | 0    |
| equipment_subcategories    | 0    |
| equipment_tags             | 0    |
| equipment_catalog          | 0    |
| equipment_catalog_tags     | 0    |
| equipment_price_history    | 0    |
| equipment_import_runs      | 0    |
| budget_equipment_items     | 0    |
| equipment_catalog_requests | 0    |

## Orçamentos — Outros (5 tabelas)
| Tabela                   | Rows |
| ------------------------ | ---- |
| mobilization_items       | 0    |
| site_maintenance_items   | 0    |
| engineering_items        | 0    |
| pricebooks               | 2    |
| budget_fabricantes       | 0    |
| material_pricebook_items | 0    |
| mo_pricebook_items       | 0    |
|                          |      |
