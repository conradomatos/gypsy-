---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc1]
---

## 1.1 Declaração do Problema

A orçamentação de obras no Brasil e um processo artesanal, lento e propenso a erros sistemáticos. Engenheiros gastam de 2 a 6 semanas montando planilhas, consultando tabelas SINAPI/SICRO defasadas, negociando com fornecedores e tentando estimar custos com alta variabilidade regional e temporal.

Dados do setor (CNI/CBIC 2024): 73% das obras brasileiras estouram o orçamento original, com desvio médio de 22%. Em empresas de médio porte (faturamento R$ 10M-200M/ano), o custo de orçamentação representa 3-5% do valor da obra, e o ciclo médio de elaboração e de 18 dias uteis.

## 1.2 Causas Raiz

•        Composições de custo estáticas (SINAPI atualiza mensalmente mas reflete mercado publico, não privado)
•        Dependencia critica de experiencia tacita do orcamentista (risco de pessoa-chave)
•        Falta de historico estruturado: custos reais vs. orcados raramente retroalimentam o processo
•        Retrabalho manual a cada revisao de projeto (media de 3.2 revisoes por obra)
•        Ausencia de inteligencia preditiva sobre variacoes sazonais, regionais e de mercado
•        Ferramentas existentes sao caras demais (SAP/Oracle) ou simplistas demais (planilhas Excel)

## 1.3 Visao do Produto

**CostAI** e um motor de inteligencia de custos que combina bases publicas (SINAPI, SICRO, CAGED), historico real de obras, cotacoes de mercado e modelos de IA para gerar orcamentos precisos, adaptativos e auditaveis. O produto nasce dentro do ecossistema PowerConcept e evolui para produto de mercado independente.

## 1.4 Decisoes Estrategicas Ja Tomadas

|**Decisao**|**Escolha**|**Justificativa**|
|---|---|---|
|Sistema legado|Aposentar Arquimedes|Limitacoes de integracao, custo de licenca, vendor lock-in|
|Plataforma|PowerConcept como sistema unico|Controle total, integracao nativa, propriedade intelectual|
|Modelo de dados|6 tabelas nucleares|Insumos, MO, Composicoes, Itens, Equipamentos, BDI|
|Fontes de dados|SINAPI + RSMeans + Historico proprio|Cobertura publica + benchmark internacional + realidade empresa|
|Mercado-alvo|Medio porte (R$ 10M-200M/ano)|Gap entre planilhas e SAP/Oracle|
|Stack tecnica|React + TS + Supabase + Claude API|Velocidade, custo baixo, IA nativa|

## 1.5 Objetivos Mensuraveis (OKRs)

### Objetivo 1: Precisao

•        KR1: Desvio medio orcado vs. realizado < 10% em 12 meses

•        KR2: 85% das composicoes com menos de 15% de desvio

•        KR3: Score de confianca por item com acuracia > 80%

### Objetivo 2: Velocidade

•        KR1: Orcamento completo em < 48h (vs. 18 dias atual)

•        KR2: Revisao por mudanca de escopo em < 4h

•        KR3: Geracao de composicao unitaria em < 30 segundos

### Objetivo 3: Escala de Mercado

•        KR1: 5 empresas piloto usando ate M6

•        KR2: 50 empresas pagantes ate M12

•        KR3: NPS > 50 entre usuarios ativos

## 1.6 Escopo (In/Out)

|**In Scope (Fase 1: M1-M6)**|**Out of Scope (Backlog Futuro)**|
|---|---|
|Motor de calculo de composicoes unitarias|Integracao com ERP (Omie, TOTVS, SAP)|
|Importacao e normalizacao SINAPI|App mobile nativo|
|Banco de 6 tabelas com CRUD completo|Marketplace de composicoes entre empresas|
|Ajustes regionais, temporais e de produtividade|Integracao BIM (IFC/Revit)|
|Score de confianca por item|Modulo de medicao de obra|
|Dashboard de cost intelligence|Integracao AutoCAD para quantitativos automaticos|
|API REST para integracao|ML preditivo avancado (fase 2)|
|Modulo de BDI parametrizavel|Gestao de contratos e aditivos|

## 1.7 Stakeholders

| **Papel**       | **Nome/Area**            | **Responsabilidade**                              |
| --------------- | ------------------------ | ------------------------------------------------- |
| Product Owner   | Sandro Matos             | Visao, priorizacao, decisoes de negocio           |
| Tech Lead       | Claude Code + Freelancer | Arquitetura, code review, decisoes tecnicas       |
| Orcamentistas   | Equipe Concept           | Validacao de composicoes, feedback de usabilidade |
| Financeiro      | Controladoria Concept    | Validacao de BDI, margens, viabilidade            |
| Clientes Piloto | 5 empresas parceiras     | Beta testing, feedback de mercado                 |

## 1.8 Riscos e Mitigacoes

| **Risco**                        | **Prob.** | **Impacto** | **Mitigacao**                                                   |
| -------------------------------- | --------- | ----------- | --------------------------------------------------------------- |
| SINAPI muda formato/acesso       | Media     | Alto        | Parser adaptativo + cache local + fallback RSMeans              |
| Custo Claude API escala demais   | Media     | Medio       | Modelos locais como fallback + cache agressivo                  |
| Baixa adesao do mercado          | Baixa     | Alto        | Pilotos gratuitos + case studies + integracao fluxos existentes |
| Acuracia insuficiente da IA      | Media     | Alto        | Human-in-the-loop obrigatorio + score de confianca visivel      |
| Competidor lanca produto similar | Media     | Medio       | Velocidade de execucao + foco mercado BR + historico proprio    |