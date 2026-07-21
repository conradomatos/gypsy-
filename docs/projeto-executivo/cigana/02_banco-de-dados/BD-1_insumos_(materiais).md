---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

### insumos

Armazena matéria-prima, componentes e materiais individuais. É o átomo do sistema — tudo começa aqui.

|                     |                     |                               |                                                            |
| ------------------- | ------------------- | ----------------------------- | ---------------------------------------------------------- |
| **Coluna**          | **Tipo PostgreSQL** | **Constraints**               | **Descrição**                                              |
| **id**              | UUID                | PK, DEFAULT gen_random_uuid() | Identificador único                                        |
| **organization_id** | UUID                | FK organizations, NOT NULL    | Tenant owner. NULL = dado global (SINAPI/RSMeans)          |
| **codigo**          | VARCHAR(50)         | NOT NULL                      | Código do insumo (ex: SINAPI 00000001)                     |
| **descricao**       | TEXT                | NOT NULL                      | Descrição completa do insumo                               |
| **unidade**         | VARCHAR(10)         | NOT NULL                      | Unidade de medida (m, kg, un, m², m³, h)                   |
| **tipo**            | VARCHAR(20)         | NOT NULL, CHECK               | material \| equipamento \| mao_de_obra \| servico_terceiro |
| **preco_unitario**  | NUMERIC(14,4)       | NOT NULL, >= 0                | Preço unitário na data de referência                       |
| **data_referencia** | DATE                | NOT NULL                      | Mês/ano de referência do preço (ex: 2026-03)               |
| **fonte**           | VARCHAR(30)         | NOT NULL                      | sinapi \| rsmeans \| concept \| manual                     |
| **estado**          | CHAR(2)             | DEFAULT 'PR'                  | UF de referência para preços regionais                     |
| **ativo**           | BOOLEAN             | DEFAULT true                  | Soft-delete flag                                           |
| **created_at**      | TIMESTAMPTZ         | DEFAULT now()                 | Criação do registro                                        |
| **updated_at**      | TIMESTAMPTZ         | DEFAULT now()                 | Última atualização                                         |

**Índices:** idx_insumos_org_codigo (organization_id, codigo) UNIQUE; idx_insumos_tipo (tipo); idx_insumos_fonte (fonte, data_referencia); idx_insumos_search (descricao) usando GIN com pg_trgm para busca fuzzy.