---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc1]
---

## 6.1 AACE (Classes de Estimativa)

Classificacao AACE RP 18R-97 como padrao de maturidade. Cada orcamento e classificado automaticamente:

| **Classe** | **Maturidade** | **Acuracia** | **Uso**    | **Mapping CostAI**                        |
| ---------- | -------------- | ------------ | ---------- | ----------------------------------------- |
| Class 5    | 0-2%           | -30% a +100% | Screening  | Estimativa parametrica IA                 |
| Class 4    | 1-15%          | -15% a +50%  | Conceitual | Composicoes SINAPI + fatores              |
| Class 3    | 10-40%         | -10% a +30%  | Preliminar | Composicoes ajustadas + cotacoes parciais |
| Class 2    | 30-75%         | -5% a +20%   | Definitivo | Composicoes detalhadas + cotacoes reais   |
| Class 1    | 65-100%        | -3% a +15%   | Executivo  | Full detail + historico + validacao       |

## 6.2 CRISP-DM

Processo para desenvolvimento do motor de IA:

| **Fase**               | **Aplicacao CostAI**                        | **Entregavel**               |
| ---------------------- | ------------------------------------------- | ---------------------------- |
| Business Understanding | KPIs orcamentacao, acuracia por classe AACE | OKRs, metricas               |
| Data Understanding     | Catalogar SINAPI, SICRO, CAGED, historico   | Data catalog, quality report |
| Data Preparation       | Parsers, normalizacao, deduplicacao         | Pipeline, schema             |
| Modeling               | Ensemble fatores, scoring, Claude prompts   | Modelos, prompts otimizados  |
| Evaluation             | Backtest obras reais, orcado vs. realizado  | Acuracia report              |
| Deployment             | Producao, monitoring, feedback, retrain     | Dashboard performance        |

## 6.3 Stage-Gate (Cooper)

|**Gate**|**Checkpoint**|**Criterios Go/Kill**|**Decisor**|
|---|---|---|---|
|Gate 0|Pre-projeto (completo)|Problema validado, mercado dimensionado|PO|
|Gate 1|Fim M1|Schema funcional, SINAPI importado|PO + Tech|
|Gate 2|Fim M2|Motor calcula com <20% desvio em 10 testes|PO + Tech|
|Gate 3|Fim M3|IA gera composicoes score>60, dashboard ok|PO + Tech + Orcamentista|
|Gate 4|Fim M4|Produto end-to-end, relatorios profissionais|PO + cliente piloto|
|Gate 5|Fim M6|NPS>50, <10% desvio, 5 pilotos, pricing ok|PO + Board|

## 6.4 Metodologia de Desenvolvimento

•        **Sprints de 2 semanas:** Cadencia Scrum para entrega incremental
•        **Kanban continuo:** Bugs, suporte, operacoes do dia a dia
•        **Stage-Gate:** Decisoes estrategicas go/kill por marco
•        **Claude Code como pair programmer:** Desenvolvimento IA-assistido para velocidade 3-5x
•        **Dogfooding obrigatorio:** Concept usa CostAI em orcamentos reais a partir de M3