---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, pre-projeto, destilacao]
---


### EPIC E-001: Destilação de Dados (Spec 0)

Fase de data engineering. Extrair, normalizar e consolidar dados de 7 fontes heterogêneas em tabelas padronizadas. É o "projeto antes do projeto" — maior que todas as sprints de desenvolvimento juntas.

**Fase:** PH-0 | **Status:** Em andamento

>[!coment] Conrado
>Já extraido os dados das tabelas hollos e murilo, nao foi extraido composições.


#### FEATURE F-003: Extração Fontes Complementares

SINAPI-PR, RSMeans, Arquimedes, catálogo Siemens, planilha insumos Concept.

**STORY S-003:** Como engenheiro, quero composições SINAPI-PR de instalações elétricas como referência de rendimentos.

| ID    | Descrição                                                                  | Tipo | Esforço |
| ----- | -------------------------------------------------------------------------- | ---- | ------- |
| T-019 | Baixar e importar SINAPI-PR composições analíticas (elétrica/civil leve)   | Task | L       |
| T-020 | Importar RSMeans Electrical Division 26 (trial 30 dias)                    | Task | L       |
| T-021 | Exportar composições do Arquimedes (formato BC3) e importar via parser     | Task | M       |
| T-022 | Importar planilha insumos Concept (catálogo por categoria, sem preços)     | Task | S       |
| T-023 | Avaliar e filtrar catálogo Siemens (~100k produtos → extrair só relevante) | Task | L       |
| T-024 | Importar planilha de outro concorrente (índices diferentes)                | Task | M       |

#### FEATURE F-004: Consolidação e Deduplicação

Juntar todas as extrações em Excel master por tipo, identificar duplicatas, resolver conflitos.

**STORY S-004:** Como engenheiro, quero um catálogo único consolidado com rastreabilidade da fonte original.

| ID    | Descrição                                                              | Tipo | Esforço |
| ----- | ---------------------------------------------------------------------- | ---- | ------- |
| T-025 | Consolidar MASTER_Insumos.xlsx (todas fontes, coluna _fonte)           | Task | L       |
| T-026 | Consolidar MASTER_MaoDeObra.xlsx                                       | Task | M       |
| T-027 | Consolidar MASTER_Equipamentos.xlsx                                    | Task | M       |
| T-028 | Consolidar MASTER_Composicoes.xlsx + MASTER_ItensComposicao.xlsx       | Task | L       |
| T-029 | Consolidar MASTER_EncargosBDI.xlsx                                     | Task | S       |
| T-030 | Identificar duplicatas entre fontes (match por descrição/código)       | Task | XL      |
| T-031 | Sessão Conrado + Sandro: resolver conflitos, definir dado autoritativo | Task | XL      |

> **Milestone M-001:** Spec 0 concluída — catálogo master validado por Conrado + Sandro


