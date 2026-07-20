---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

### equipamentos

Equipamentos utilizados em composições, com custo por hora (produtivo e improdutivo). Separado de insumos pela lógica de cálculo diferente: depende de horas produtivas vs improdutivas.

|                               |               |                  |                                  |
| ----------------------------- | ------------- | ---------------- | -------------------------------- |
| **Coluna**                    | **Tipo**      | **Constraints**  | **Descrição**                    |
| **id**                        | UUID          | PK               | Identificador único              |
| **organization_id**           | UUID          | FK organizations | Tenant owner                     |
| **codigo**                    | VARCHAR(50)   | NOT NULL         | Código (ex: EQ-MUNCK-01)         |
| **descricao**                 | TEXT          | NOT NULL         | Descrição do equipamento         |
| **custo_hora_produtivo**      | NUMERIC(10,4) | NOT NULL, >= 0   | Custo por hora em operação       |
| **custo_hora_improdutivo**    | NUMERIC(10,4) | NOT NULL, >= 0   | Custo por hora parado (stand-by) |
| **depreciacao_mensal**        | NUMERIC(10,4) | DEFAULT 0        | Custo de depreciação mensal      |
| **fonte, data_referencia**    | (padrão)      | (padrão)         | Origem e data de referência      |
| ativo, created_at, updated_at | (padrão)      | (padrão)         | Campos padrão                    |
