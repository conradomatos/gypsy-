---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc1]
---

## 3.1 Arquitetura de Parametros

O motor opera sobre composicoes unitarias, ajustando cada componente por uma cadeia de fatores multiplicativos auditaveis. Formula geral:

**Custo_Ajustado = Custo_Base x F_regional x F_temporal x F_produtividade x F_escala x F_complexidade x F_risco**

## 3.2 Fatores Regionais

|**Parametro**|**Descricao**|**Fonte**|**Granularidade**|**Update**|
|---|---|---|---|---|
|fator_uf|Coeficiente por estado (base SP=1.0)|SINAPI desonerado|27 UFs|Mensal|
|fator_municipio|Ajuste intra-estado|CAGED + IBGE|5.570 municipios|Trimestral|
|fator_zona|Urbano vs. rural vs. industrial|IBGE + heuristica|3 categorias|Semestral|
|fator_distancia_base|Custo logistico por km do CD|ANTT + diesel|Continuo (km)|Mensal|
|fator_altitude|Impacto na produtividade e logistica|IBGE + historico|Continuo (m)|Anual|
|fator_clima|Regime de chuvas no cronograma|INMET historico|12 meses x UF|Mensal|

## 3.3 Fatores Temporais

|**Parametro**|**Descricao**|**Fonte**|**Granularidade**|**Update**|
|---|---|---|---|---|
|fator_inflacao_geral|INCC acumulado desde data-base|FGV/IBGE|Mensal|Mensal|
|fator_inflacao_grupo|Inflacao por grupo (mat, MO, equip)|INCC grupo|Mensal x 3|Mensal|
|fator_inflacao_insumo|Variacao especifica (aco, cimento)|SINAPI + cotacoes|Por insumo|Mensal|
|fator_sazonalidade|Ajuste seco/chuvoso, fim de ano|Historico proprio|12 meses|Anual|
|fator_tendencia|Projecao 3-6 meses|ARIMA + IA|Por insumo|Semanal|
|data_base_orcamento|Data referencia para precos|Input usuario|Data|Por orcamento|

## 3.4 Fatores de Produtividade

|**Parametro**|**Descricao**|**Fonte**|**Range**|**Update**|
|---|---|---|---|---|
|fator_produtividade_mo|Rendimento real vs. composicao|Historico + TCPO|0.6-1.4|Por obra|
|fator_experiencia_equipe|Curva de aprendizado|Classificacao RH|0.8-1.2|Por equipe|
|fator_turno|Noturno/extra|CLT + convencao|1.0-1.8|Anual|
|fator_mecanizacao|MO manual vs. equipamento|Catalogo equip.|0.3-1.0|Por composicao|
|fator_retrabalho|Historico de retrabalho|Historico proprio|1.0-1.25|Trimestral|
|fator_supervisao|Ratio supervisor/operario|Benchmarks AACE|0.9-1.15|Por obra|

## 3.5 Fatores de Escala e Complexidade

|**Parametro**|**Descricao**|**Fonte**|**Range**|**Update**|
|---|---|---|---|---|
|fator_escala_quantidade|Desconto/premio por volume|Curva fornecedor|0.85-1.15|Por cotacao|
|fator_complexidade_tecnica|Acesso, altura, confinamento|AACE|1.0-2.0|Por composicao|
|fator_porte_obra|Economia de escala|Regressao historica|0.9-1.1|Trimestral|
|fator_repeticao|Eficiencia em servicos repetitivos|Curva aprendizado|0.85-1.0|Por composicao|
|fator_simultaneidade|Ganho por execucao paralela|Planejamento|0.9-1.0|Por obra|

## 3.6 Fatores de Risco e Contingencia

|**Parametro**|**Descricao**|**Fonte**|**Range**|**Update**|
|---|---|---|---|---|
|fator_risco_tecnico|Servico nao usual/inovador|AACE Class 1-5|1.0-1.3|Por composicao|
|fator_risco_geologico|Solo/fundacao desconhecido|Sondagens|1.0-1.5|Por obra|
|fator_risco_regulatorio|Mudanca normativa|Historico + IA|1.0-1.1|Semestral|
|fator_contingencia_global|% contingencia sobre total|Politica empresa|5%-25%|Por orcamento|
|score_confianca|Nivel de confianca 0-100|Ensemble IA|0-100|Por item|

## 3.7 Parametros de BDI

|**Componente**|**Descricao**|**Range Tipico**|**Parametrizavel Por**|
|---|---|---|---|
|Administracao Central|Rateio custos fixos|3%-8%|Empresa|
|Custo Financeiro|Custo capital durante obra|0.5%-3%|Obra + prazo|
|Seguro e Garantia|Seguro + performance bond|0.5%-2%|Tipo de obra|
|Margem de Lucro|Margem bruta desejada|5%-15%|Obra + cliente|
|Impostos|ISS+PIS+COFINS+IRPJ+CSLL|Regime tributario|Empresa + municipio|
|Despesas Financeiras|Taxas, garantias bancarias|0.5%-2%|Contrato|
|Imprevistos|Margem nao mapeada|1%-5%|Classe AACE|

**Formula:** BDI = ((1+AC)(1+CF)(1+SG)(1+ML)(1+DF)(1+IMP)) / (1-Impostos) - 1

## 3.8 Fontes de Dados e Prioridade

|**Fonte**|**Tipo**|**Cobertura**|**Prioridade**|**Confianca**|
|---|---|---|---|---|
|SINAPI Analitico|Publica oficial|Construcao civil geral|1 (primaria)|75-85|
|SICRO|Publica oficial|Infra rodoviaria|1 (primaria)|75-85|
|RSMeans (Gordian)|Comercial int'l|Benchmark internacional|2 (referencia)|70-80|
|Historico Proprio|Privado|Obras executadas pela empresa|1 (primaria)|85-95|
|Cotacoes Mercado|Tempo real|Insumos especificos|1 (primaria)|80-90|
|TCPO (Pini)|Comercial BR|Composicoes detalhadas|2 (referencia)|70-80|
|CAGED/RAIS|Publica oficial|Salarios regionais|1 (primaria)|80-85|
