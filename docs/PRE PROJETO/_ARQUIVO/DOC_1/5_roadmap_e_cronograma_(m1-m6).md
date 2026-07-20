---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc1]
---

## 5.1 Fases

|**Fase**|**Periodo**|**Foco**|**Entregaveis**|
|---|---|---|---|
|Discovery & Foundation|M1 (S1-4)|Dados, infra, SINAPI|Schema, parser SINAPI, seed data, CI/CD|
|Core Engine|M2-M3 (S5-12)|Motor, fatores, API|CRUD, engine composicao, API REST, testes|
|Intelligence Layer|M3-M4 (S9-16)|IA, scoring, dashboard|Claude API, score confianca, analytics|
|Product Polish|M4-M5 (S13-20)|UX, BDI, relatorios|UI completa, BDI, export PDF/Excel|
|Beta & Validation|M5-M6 (S17-24)|Pilotos, go-to-market|5 pilotos, feedback, pricing validado|

## 5.2 Sprints Detalhadas

### Sprint 1-2: Foundation (M1)

| **ID**    | **Descricao**                                    | **Est.** | **Dep.** |
| --------- | ------------------------------------------------ | -------- | -------- |
| DB-001    | Schema 6 tabelas + RLS + indexes                 | 3d       | -        |
| DB-002    | Seed SINAPI analitico (Jan/2026)                 | 2d       | DB-001   |
| DB-003    | Parser SINAPI automatizado (PDF/XLS -> Supabase) | 5d       | DB-001   |
| FE-001    | Scaffold React + Tailwind + shadcn + Zustand     | 1d       | -        |
| FE-002    | CRUD insumos                                     | 3d       | DB-001   |
| FE-003    | CRUD mao de obra                                 | 2d       | FE-002   |
| API-001   | Edge Functions: CRUD insumos + MO                | 3d       | DB-001   |
| INFRA-001 | Setup Supabase + GitHub Actions + Sentry         | 2d       | -        |

### Sprint 3-4: Core Engine (M2)

| **ID**  | **Descricao**                             | **Est.** | **Dep.** |
| ------- | ----------------------------------------- | -------- | -------- |
| ENG-001 | Motor composicao unitaria (calculo base)  | 5d       | DB-001   |
| ENG-002 | Fatores regionais (UF + municipio)        | 3d       | ENG-001  |
| ENG-003 | Fatores temporais (INCC + inflacao)       | 3d       | ENG-001  |
| FE-004  | Editor visual de composicao               | 5d       | ENG-001  |
| FE-005  | Tela orcamento (arvore de itens)          | 5d       | FE-004   |
| DB-004  | Importar SICRO                            | 3d       | DB-003   |
| API-002 | Endpoint: calcular composicao com fatores | 3d       | ENG-001  |

### Sprint 5-6: Intelligence (M3)

| **ID**  | **Descricao**                              | **Est.** | **Dep.** |
| ------- | ------------------------------------------ | -------- | -------- |
| IA-001  | Claude API: gerar composicao por descricao | 5d       | ENG-001  |
| IA-002  | Classificador automatico de insumos        | 3d       | DB-002   |
| ENG-004 | Score de confianca (ensemble)              | 5d       | ENG-001  |
| ENG-005 | Fatores produtividade e escala             | 3d       | ENG-002  |
| FE-006  | Dashboard cost intelligence                | 5d       | ENG-004  |
| FE-007  | Indicador visual score de confianca        | 2d       | ENG-004  |

### Sprint 7-8: Polish (M4)

| **ID**  | **Descricao**                             | **Est.** | **Dep.** |
| ------- | ----------------------------------------- | -------- | -------- |
| BDI-001 | BDI parametrizavel (7 componentes)        | 5d       | DB-001   |
| BDI-002 | Calculo por regime tributario             | 3d       | BDI-001  |
| FE-008  | UX polish: responsividade, acessibilidade | 5d       | FE-005   |
| REP-001 | Export PDF orcamento profissional         | 5d       | BDI-001  |
| REP-002 | Export Excel detalhado                    | 3d       | REP-001  |
| API-003 | Docs OpenAPI + Postman                    | 2d       | API-002  |

### Sprint 9-12: Beta (M5-M6)

| **ID**    | **Descricao**                       | **Est.** | **Dep.**  |
| --------- | ----------------------------------- | -------- | --------- |
| PILOT-001 | Onboarding 5 empresas piloto        | 10d      | Todas     |
| PILOT-002 | Feedback loop semanal               | 20d      | PILOT-001 |
| ENG-006   | Ajustes acuracia com feedback real  | 10d      | PILOT-002 |
| BIZ-001   | Validacao pricing (testes de preco) | 5d       | PILOT-001 |
| BIZ-002   | Materiais go-to-market              | 5d       | PILOT-002 |
| INFRA-002 | Load testing + performance          | 5d       | Todas     |

## 5.3 Milestones

|**Marco**|**Data**|**Criterio de Sucesso**|**Gate**|
|---|---|---|---|
|Foundation Complete|Fim S4|Schema, SINAPI importado, CI/CD|Gate 1|
|Engine MVP|Fim S8|Motor calcula com fatores regionais/temporais|Gate 2|
|IA Integrada|Fim S12|Claude gera composicoes, score funcional|Gate 3|
|Produto Beta|Fim S16|BDI, relatorios, UX polida|Gate 4|
|Beta Launch|Fim S20|5 empresas em producao|Gate 5|
|Validacao|Fim S24|NPS>50, acuracia>85%, pricing validado|Go/No-Go|
