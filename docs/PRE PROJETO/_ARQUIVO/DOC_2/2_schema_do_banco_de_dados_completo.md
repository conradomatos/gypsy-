---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc2]
---

## 2.1 Visão Geral do Schema

O banco de dados está organizado em 3 domínios: Core (tabelas de referência e cálculo), Operacional (orçamentos, projetos, propostas), e Sistema (usuários, organizações, auditoria). Todas as tabelas seguem convenções: snake_case, UUID como PK, timestamps automáticos, soft-delete onde aplicável.

## 2.2 Tabelas Core (Pricebook)

### 2.2.1 insumos

Armazena matéria-prima, componentes e materiais individuais. É o átomo do sistema — tudo começa aqui.

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo PostgreSQL**|**Constraints**|**Descrição**|
|**id**|UUID|PK, DEFAULT gen_random_uuid()|Identificador único|
|**organization_id**|UUID|FK organizations, NOT NULL|Tenant owner. NULL = dado global (SINAPI/RSMeans)|
|**codigo**|VARCHAR(50)|NOT NULL|Código do insumo (ex: SINAPI 00000001)|
|**descricao**|TEXT|NOT NULL|Descrição completa do insumo|
|**unidade**|VARCHAR(10)|NOT NULL|Unidade de medida (m, kg, un, m², m³, h)|
|**tipo**|VARCHAR(20)|NOT NULL, CHECK|material \| equipamento \| mao_de_obra \| servico_terceiro|
|**preco_unitario**|NUMERIC(14,4)|NOT NULL, >= 0|Preço unitário na data de referência|
|**data_referencia**|DATE|NOT NULL|Mês/ano de referência do preço (ex: 2026-03)|
|**fonte**|VARCHAR(30)|NOT NULL|sinapi \| rsmeans \| concept \| manual|
|**estado**|CHAR(2)|DEFAULT 'PR'|UF de referência para preços regionais|
|**ativo**|BOOLEAN|DEFAULT true|Soft-delete flag|
|**created_at**|TIMESTAMPTZ|DEFAULT now()|Criação do registro|
|**updated_at**|TIMESTAMPTZ|DEFAULT now()|Última atualização|

**Índices:** idx_insumos_org_codigo (organization_id, codigo) UNIQUE; idx_insumos_tipo (tipo); idx_insumos_fonte (fonte, data_referencia); idx_insumos_search (descricao) usando GIN com pg_trgm para busca fuzzy.

### 2.2.2 mao_de_obra

Categorias de mão de obra com salário-hora e encargos. Separada de insumos porque tem lógica própria: encargos sociais, periculosidade, turno, etc.

|                               |               |                     |                                                                             |
| ----------------------------- | ------------- | ------------------- | --------------------------------------------------------------------------- |
| **Coluna**                    | **Tipo**      | **Constraints**     | **Descrição**                                                               |
| **id**                        | UUID          | PK                  | Identificador único                                                         |
| **organization_id**           | UUID          | FK organizations    | Tenant owner                                                                |
| **codigo**                    | VARCHAR(50)   | NOT NULL            | Código (ex: MO-ELE-01)                                                      |
| **funcao**                    | VARCHAR(100)  | NOT NULL            | Eletricista, Encarregado, Ajudante, etc.                                    |
| **salario_hora_base**         | NUMERIC(10,4) | NOT NULL, >= 0      | Salário-hora sem encargos                                                   |
| **encargos_sociais_pct**      | NUMERIC(6,4)  | NOT NULL            | Percentual de encargos (ex: 0.8230 = 82,30%)                                |
| **periculosidade_pct**        | NUMERIC(5,4)  | DEFAULT 0.30        | Adicional periculosidade (30% padrão)                                       |
| **custo_hora_total**          | NUMERIC(10,4) | GENERATED ALWAYS AS | = salario_hora_base * (1 + periculosidade_pct) * (1 + encargos_sociais_pct) |
| **fonte**                     | VARCHAR(30)   | NOT NULL            | sinapi \| convencao \| concept \| manual                                    |
| **data_referencia**           | DATE          | NOT NULL            | Mês/ano de referência                                                       |
| ativo, created_at, updated_at | (padrão)      | (padrão)            | Campos padrão de auditoria                                                  |

**Nota técnica:** custo_hora_total é coluna GENERATED (computed). O PostgreSQL recalcula automaticamente quando qualquer componente muda. Isso elimina inconsistência entre salário e custo total.

### 2.2.3 composicoes

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

### 2.2.5 equipamentos

Equipamentos utilizados em composições, com custo por hora (produtivo e improdutivo). Separado de insumos pela lógica de cálculo diferente: depende de horas produtivas vs improdutivas.

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo**|**Constraints**|**Descrição**|
|**id**|UUID|PK|Identificador único|
|**organization_id**|UUID|FK organizations|Tenant owner|
|**codigo**|VARCHAR(50)|NOT NULL|Código (ex: EQ-MUNCK-01)|
|**descricao**|TEXT|NOT NULL|Descrição do equipamento|
|**custo_hora_produtivo**|NUMERIC(10,4)|NOT NULL, >= 0|Custo por hora em operação|
|**custo_hora_improdutivo**|NUMERIC(10,4)|NOT NULL, >= 0|Custo por hora parado (stand-by)|
|**depreciacao_mensal**|NUMERIC(10,4)|DEFAULT 0|Custo de depreciação mensal|
|**fonte, data_referencia**|(padrão)|(padrão)|Origem e data de referência|
|ativo, created_at, updated_at|(padrão)|(padrão)|Campos padrão|

### 2.2.6 encargos_bdi

Tabela de configuração de BDI (Bonificação e Despesas Indiretas) e encargos. Cada organização pode ter múltiplos perfis de BDI (ex: obra pública, obra privada, manutenção).

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo**|**Constraints**|**Descrição**|
|**id**|UUID|PK|Identificador único|
|**organization_id**|UUID|FK organizations, NOT NULL|Tenant owner|
|**nome_perfil**|VARCHAR(100)|NOT NULL|Ex: BDI Obra Privada, BDI Manutenção|
|**administracao_central_pct**|NUMERIC(6,4)|NOT NULL|% Administração central|
|**seguro_garantia_pct**|NUMERIC(6,4)|NOT NULL|% Seguro e garantia|
|**risco_pct**|NUMERIC(6,4)|NOT NULL|% Risco/contingência|
|**despesas_financeiras_pct**|NUMERIC(6,4)|NOT NULL|% Despesas financeiras|
|**lucro_pct**|NUMERIC(6,4)|NOT NULL|% Lucro/bonificação|
|**impostos_pct**|NUMERIC(6,4)|NOT NULL|% Impostos (ISS, PIS, COFINS, IRPJ, CSLL)|
|**bdi_total**|NUMERIC(6,4)|GENERATED|Fórmula BDI consolidada (SINAPI/TCU)|
|**is_default**|BOOLEAN|DEFAULT false|Perfil padrão da organização|

**Fórmula BDI (TCU):** BDI = ((1 + AC + S + R + DF + L) / (1 - I)) - 1, onde AC=Adm Central, S=Seguro, R=Risco, DF=Desp Financeiras, L=Lucro, I=Impostos. Exemplo: ((1 + 0.04 + 0.01 + 0.015 + 0.012 + 0.08) / (1 - 0.0865)) - 1 = 0.2676 (26,76%).

  

## 2.3 Tabelas Operacionais

Tabelas que suportam a operação diária: orçamentos, projetos, propostas. Referenciam as tabelas core mas pertencem ao contexto específico de cada projeto.

### 2.3.1 Resumo das Tabelas Operacionais

|   |   |   |
|---|---|---|
|**Tabela**|**Descrição**|**Principais Colunas (além das padrão)**|
|**organizations**|Empresas/tenants. Raíz do multi-tenancy.|nome, cnpj, plano (starter/pro/enterprise), settings (JSONB)|
|**users**|Usuários do sistema. Vinculados a auth.users do Supabase.|auth_user_id (FK auth.users), organization_id, role (admin/manager/user), nome, email|
|**projetos**|Agrupa orçamentos de uma mesma obra/contrato.|organization_id, cliente_id, nome, descricao, status, localizacao (JSONB com lat/lng/cidade/uf)|
|**clientes**|Cadastro de clientes da organização.|organization_id, razao_social, cnpj, contato_nome, contato_email, contato_telefone|
|**orcamentos**|Orçamento completo com WBS e itens.|projeto_id, encargo_bdi_id, status (rascunho/em_revisao/aprovado/enviado), valor_total, revisao, moeda|
|**orcamento_itens**|Itens do orçamento (linha a linha da WBS).|orcamento_id, composicao_id (versão específica), wbs_code, quantidade, custo_unitario_ajustado, custo_total, fatores_aplicados (JSONB)|
|**propostas**|Propostas comerciais geradas a partir de orçamentos.|orcamento_id, template_id, conteudo (JSONB), status, pdf_url, enviado_em|
|**audit_log**|Log imutável de todas as mutações.|user_id, organization_id, tabela, registro_id, acao (INSERT/UPDATE/DELETE), dados_antes (JSONB), dados_depois (JSONB), ip|
|**fatores_projeto**|Fatores de ajuste aplicados a um projeto específico.|projeto_id, tipo_fator, valor, justificativa, fonte_dado, aplicado_por|

## 2.4 RLS Policies (Row Level Security)

Toda tabela com organization_id tem RLS habilitado. A política base é:

CREATE POLICY "tenant_isolation" ON [tabela]

  FOR ALL

  USING (organization_id = (SELECT organization_id FROM users

    WHERE auth_user_id = auth.uid()));

Tabelas de referência global (SINAPI, RSMeans) têm organization_id = NULL e política adicional:

CREATE POLICY "global_read" ON insumos

  FOR SELECT USING (organization_id IS NULL);

O audit_log é INSERT-only: usuários não podem UPDATE nem DELETE registros de auditoria.

## 2.5 Diagrama ER (Descritivo)

Relacionamentos principais entre entidades:

•        organizations 1:N users, projetos, clientes, orcamentos, composicoes, insumos, mao_de_obra, equipamentos, encargos_bdi

•        projetos N:1 clientes; projetos 1:N orcamentos

•        orcamentos N:1 encargos_bdi; orcamentos 1:N orcamento_itens

•        orcamento_itens N:1 composicoes (versão específica)

•        composicoes 1:N itens_composicao (via composicao_id)

•        itens_composicao N:1 insumos | mao_de_obra | equipamentos | composicoes (polimórfico)

•        projetos 1:N fatores_projeto

•        audit_log: tabela isolada, recebe eventos de todas as outras via triggers