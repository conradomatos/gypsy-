---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

### composicoes

A composição é a unidade fundamental de orçamentação. Representa um serviço completo (ex: instalação de eletroduto) com todos os insumos, mão de obra e equipamentos necessários. Cada composição é versionada.

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo**|**Constraints**|**Descrição**|
|**id**|UUID|PK|Identificador único da versão|
|**composicao_root_id**|UUID|NOT NULL|ID da composição raiz (agrupa versões)|
|**organization_id**|UUID|FK organizations|Tenant. NULL = global|
|**codigo**|VARCHAR(50)|NOT NULL|Código (ex: COMP-ELE-001, SINAPI 94xxx)|
|**descricao**|TEXT|NOT NULL|Descrição completa do serviço|
|**unidade**|VARCHAR(10)|NOT NULL|Unidade de medida da composição|
|**revisao**|INTEGER|NOT NULL, DEFAULT 1|Número da revisão (incrementa a cada alteração)|
|**is_current**|BOOLEAN|DEFAULT true|Flag: esta é a versão vigente?|
|**fonte**|VARCHAR(30)|NOT NULL|sinapi \| rsmeans \| concept \| custom|
|**categoria**|VARCHAR(50)||Classificação: eletrica, civil, mecanica, etc.|
|**custo_unitario_base**|NUMERIC(14,4)|GENERATED ALWAYS AS|Soma calculada dos itens da composição (trigger ou view)|
|**created_by**|UUID|FK users|Usuário que criou esta versão|
|ativo, created_at, updated_at|(padrão)|(padrão)|Campos padrão|

**Mecanismo de versionamento:** composicao_root_id agrupa todas as versões de uma mesma composição. Quando o usuário edita, o sistema cria novo registro com revisao+1 e marca is_current=true na nova, false na anterior. Índice único parcial: UNIQUE(composicao_root_id) WHERE is_current = true.

### 2.2.4 itens_composicao

Relação N:N entre composições e seus componentes (insumos, mão de obra, equipamentos, ou sub-composições). Cada linha define um componente com seu coeficiente (rendimento).

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo**|**Constraints**|**Descrição**|
|**id**|UUID|PK|Identificador único|
|**composicao_id**|UUID|FK composicoes, NOT NULL|Composição pai (versão específica)|
|**tipo_componente**|VARCHAR(20)|NOT NULL, CHECK|insumo \| mao_de_obra \| equipamento \| composicao|
|**insumo_id**|UUID|FK insumos, NULLABLE|Referência se tipo = insumo|
|**mao_de_obra_id**|UUID|FK mao_de_obra, NULLABLE|Referência se tipo = mao_de_obra|
|**equipamento_id**|UUID|FK equipamentos, NULLABLE|Referência se tipo = equipamento|
|**sub_composicao_id**|UUID|FK composicoes, NULLABLE|Referência se tipo = composicao (recursivo)|
|**coeficiente**|NUMERIC(12,6)|NOT NULL, > 0|Rendimento/consumo por unidade da composição|
|**custo_parcial**|NUMERIC(14,4)|GENERATED|= coeficiente * preço unitário do componente|

**CHECK constraint polimórfico:** Exatamente um dos campos de FK (insumo_id, mao_de_obra_id, equipamento_id, sub_composicao_id) deve ser NOT NULL, de acordo com tipo_componente. Implementado via CHECK constraint com lógica XOR.