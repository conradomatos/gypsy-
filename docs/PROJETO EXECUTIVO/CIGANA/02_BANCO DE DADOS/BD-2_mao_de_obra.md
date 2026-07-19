---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

### mao_de_obra

Categorias de mão de obra com salário-hora e encargos. Separada de insumos porque tem lógica própria: encargos sociais, periculosidade, turno, etc.

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo**|**Constraints**|**Descrição**|
|**id**|UUID|PK|Identificador único|
|**organization_id**|UUID|FK organizations|Tenant owner|
|**codigo**|VARCHAR(50)|NOT NULL|Código (ex: MO-ELE-01)|
|**funcao**|VARCHAR(100)|NOT NULL|Eletricista, Encarregado, Ajudante, etc.|
|**salario_hora_base**|NUMERIC(10,4)|NOT NULL, >= 0|Salário-hora sem encargos|
|**encargos_sociais_pct**|NUMERIC(6,4)|NOT NULL|Percentual de encargos (ex: 0.8230 = 82,30%)|
|**periculosidade_pct**|NUMERIC(5,4)|DEFAULT 0.30|Adicional periculosidade (30% padrão)|
|**custo_hora_total**|NUMERIC(10,4)|GENERATED ALWAYS AS|= salario_hora_base * (1 + periculosidade_pct) * (1 + encargos_sociais_pct)|
|**fonte**|VARCHAR(30)|NOT NULL|sinapi \| convencao \| concept \| manual|
|**data_referencia**|DATE|NOT NULL|Mês/ano de referência|
|ativo, created_at, updated_at|(padrão)|(padrão)|Campos padrão de auditoria|

**Nota técnica:** custo_hora_total é coluna GENERATED (computed). O PostgreSQL recalcula automaticamente quando qualquer componente muda. Isso elimina inconsistência entre salário e custo total.