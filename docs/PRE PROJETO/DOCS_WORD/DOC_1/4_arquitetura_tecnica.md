---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc1]
---

## 4.1 Stack Tecnológica

|**Camada**|**Tecnologia**|**Justificativa**|
|---|---|---|
|Frontend|React 18 + TypeScript + Tailwind|Ecossistema maduro, tipagem forte, dev rapido|
|UI Components|shadcn/ui + Radix UI|Acessiveis, customizaveis, sem vendor lock-in|
|Backend/API|Supabase (PostgreSQL + Edge Functions)|Serverless, RLS nativo, real-time|
|Auth|Supabase Auth|SSO, magic link, RBAC nativo|
|IA/LLM|Claude API (Anthropic)|Melhor reasoning para composicoes tecnicas|
|State|Zustand + React Query|Leve, previsivel, cache inteligente|
|Hosting|Vercel + Supabase Cloud|Deploy auto, edge global, zero DevOps|
|Monitoring|Sentry + Supabase Analytics|Error tracking + metricas de uso|
|CI/CD|GitHub Actions|Testes auto, deploy continuo|

## 4.2 Modelo de Dados (6 Tabelas Nucleares)

### 4.2.1 insumos

|**Coluna**|**Tipo**|**Descricao**|
|---|---|---|
|id|uuid PK|Identificador unico|
|codigo_sinapi|text|Codigo SINAPI (nullable se custom)|
|nome|text|Nome descritivo|
|unidade|text|kg, m, m2, m3, un, etc.|
|preco_unitario|numeric(12,4)|Preco base (data-base SINAPI ou cotacao)|
|fonte|enum|sinapi \| sicro \| rsmeans \| historico \| cotacao|
|data_referencia|date|Data-base do preco|
|uf_referencia|char(2)|UF de referencia|
|categoria|text|Classificacao (material, eletrico, etc.)|
|score_confianca|smallint|0-100, calculado pelo motor|
|metadata|jsonb|NCM, fornecedor, variantes|
|org_id|uuid FK|Multi-tenant|

### 4.2.2 mao_de_obra

|**Coluna**|**Tipo**|**Descricao**|
|---|---|---|
|id|uuid PK|Identificador unico|
|codigo_sinapi|text|Codigo SINAPI da funcao|
|funcao|text|Servente, eletricista, soldador, etc.|
|salario_hora|numeric(10,4)|Custo horario com encargos|
|encargos_sociais|numeric(6,4)|Percentual (ex: 1.8734)|
|uf_referencia|char(2)|UF de referencia|
|convencao_coletiva|text|Ref. sindicato/regiao|
|qualificacao|text|ajudante \| oficial \| mestre \| tecnico \| engenheiro|
|metadata|jsonb|CBO, piso, beneficios|
|org_id|uuid FK|Multi-tenant|

### 4.2.3 composicoes

|**Coluna**|**Tipo**|**Descricao**|
|---|---|---|
|id|uuid PK|Identificador unico|
|codigo|text|Codigo (SINAPI ou proprio)|
|nome|text|Descricao do servico|
|unidade|text|m2, m3, m, un|
|custo_unitario|numeric(12,4)|Custo calculado (soma componentes)|
|componentes|jsonb|Array de {tipo, ref_id, coeficiente, custo}|
|fonte|enum|sinapi \| sicro \| propria \| ia_gerada|
|score_confianca|smallint|0-100|
|fatores_aplicados|jsonb|Registro de todos os fatores|
|versao|integer|Versionamento incremental|
|orcamento_id|uuid FK|Orcamento pai (nullable se template)|
|org_id|uuid FK|Multi-tenant|

### 4.2.4 itens_orcamento

|**Coluna**|**Tipo**|**Descricao**|
|---|---|---|
|id|uuid PK|Identificador unico|
|orcamento_id|uuid FK|Referencia ao orcamento|
|composicao_id|uuid FK|Referencia a composicao|
|descricao|text|Descricao no contexto|
|quantidade|numeric(12,4)|Quantidade medida|
|custo_unitario|numeric(12,4)|Custo unitario ajustado|
|custo_total|numeric(14,4)|Qtd x custo unitario|
|bdi_aplicado|numeric(6,4)|BDI deste item|
|preco_venda|numeric(14,4)|Custo total x (1+BDI)|
|etapa|text|Fundacao, estrutura, etc.|
|ordem|integer|Ordem de apresentacao|
|org_id|uuid FK|Multi-tenant|

### 4.2.5 equipamentos

|**Coluna**|**Tipo**|**Descricao**|
|---|---|---|
|id|uuid PK|Identificador unico|
|codigo_sicro|text|Codigo SICRO (nullable se custom)|
|nome|text|Descricao do equipamento|
|tipo|enum|proprio \| alugado \| terceirizado|
|custo_hora_produtiva|numeric(10,4)|Custo/hora em operacao|
|custo_hora_improdutiva|numeric(10,4)|Custo parado|
|vida_util_horas|integer|Vida util em horas|
|potencia_cv|numeric(8,2)|Potencia em CV|
|consumo_litros_hora|numeric(6,2)|Consumo combustivel|
|metadata|jsonb|Marca, modelo, ano, manutencao|
|org_id|uuid FK|Multi-tenant|

### 4.2.6 bdi_configuracoes

|**Coluna**|**Tipo**|**Descricao**|
|---|---|---|
|id|uuid PK|Identificador unico|
|nome|text|Nome (padrao, obra X, licitacao)|
|administracao_central|numeric(6,4)|% AC|
|custo_financeiro|numeric(6,4)|% CF|
|seguro_garantia|numeric(6,4)|% SG|
|margem_lucro|numeric(6,4)|% ML|
|despesas_financeiras|numeric(6,4)|% DF|
|imprevistos|numeric(6,4)|% imprevistos|
|impostos|jsonb|{iss, pis, cofins, irpj, csll}|
|bdi_calculado|numeric(6,4)|BDI final|
|orcamento_id|uuid FK|Orcamento especifico (nullable)|
|org_id|uuid FK|Multi-tenant|

## 4.3 Fluxo do Motor de Calculo

5 etapas sequenciais, cada uma auditavel:

1.     INGESTAO: Importa SINAPI/SICRO/cotacoes, normaliza unidades e nomenclatura

2.     COMPOSICAO: Monta ou recupera composicao unitaria (SINAPI, propria ou gerada por IA)

3.     AJUSTE: Aplica cadeia de fatores (regional, temporal, produtividade, escala, risco)

4.     SCORING: Calcula score de confianca (idade do dado, variancia, fonte, #cotacoes)

5.     CONSOLIDACAO: Agrega itens, aplica BDI, gera relatorio com drill-down ate insumo

## 4.4 Integracao IA (Claude API)

IA em 4 capacidades, como complemento ao motor de calculo (nao substituto):

|**Capacidade**|**Input**|**Output**|**Modelo**|**Custo/Call**|
|---|---|---|---|---|
|Gerar composicao|Descricao servico + contexto|Composicao JSON|Claude Sonnet|~US$ 0.03|
|Classificar insumo|Nome + fornecedor|Categoria + cod SINAPI|Claude Haiku|~US$ 0.002|
|Analisar desvio|Orcado vs. realizado|Diagnostico + recomendacoes|Claude Sonnet|~US$ 0.05|
|Chat tecnico|Pergunta orcamentista|Resposta com refs|Claude Sonnet|~US$ 0.04|

## 4.5 Seguranca e Multi-Tenancy

•        RLS em todas as tabelas: cada org so ve seus dados
•        Dados SINAPI/SICRO compartilhados (org_id = null), proprios isolados
•        Supabase Auth com SSO para enterprise
•        TLS 1.3 em transito, AES-256 em repouso
•        Audit log de todas as operacoes de escrita
•        Backups diarios, retencao 30 dias