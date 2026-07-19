---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc2]
---

## 1.1 Visão Geral

O Cost Intelligence Engine é organizado em 5 camadas horizontais, cada uma com responsabilidade bem definida. A comunicação entre camadas é sempre unidirecional de cima para baixo (frontend → API → engine → data), com exceção da camada de IA que atua transversalmente.

### 1.1.1 Diagrama de Camadas

A arquitetura segue o padrão de camadas (layered architecture) com separação clara de responsabilidades:

|                         |                                           |                                                                                           |
| ----------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Camada**              | **Componentes**                           | **Responsabilidade**                                                                      |
| **5. Presentação**      | React + TypeScript + Tailwind + shadcn/ui | Interface do usuário. Renderiza orçamentos, WBS, dashboards. Zero lógica de negócio.      |
| **4. API Gateway**      | Supabase Edge Functions (Deno/TypeScript) | Autenticação, validação de input, roteamento, rate limiting, versionamento de endpoints.  |
| **3. Motor de Cálculo** | Edge Functions + PostgreSQL Functions     | Lógica core: resolver composições, aplicar fatores, calcular faixas de preço, gerar BDI.  |
| **2. Camada de IA**     | Claude API (Anthropic) via Edge Functions | Leitura de escopo, sugestão de composições, auditoria, geração de propostas. Transversal. |
| **1. Dados**            | PostgreSQL (Supabase) + Storage           | Tabelas core, referências (SINAPI, RSMeans), histórico de obras, arquivos BC3.            |
|                         |                                           |                                                                                           |
|                         |                                           |                                                                                           |

### 1.1.2 Princípios de Arquitetura

**Multi-tenancy nativo:** Toda tabela possui organization_id. Row Level Security (RLS) do Supabase garante isolamento. Uma empresa nunca vê dados de outra.

**Composições imutáveis com versionamento:** Cada alteração em uma composição gera nova versão (revision). O orçamento referencia a versão específica, garantindo rastreabilidade. Nunca se edita in-place.

**Separação dados-referência vs dados-operação:** Tabelas de referência (SINAPI, RSMeans) são read-only para o usuário. Dados operacionais (orçamentos, propostas) pertencem à organização.

**IA como advisor, não como decisor:** A camada de IA sugere, audita e alerta. A decisão final (aprovar composição, enviar proposta) sempre é humana. Isso é crítico para responsabilidade técnica (ART/CREA).


## 1.2 Fluxo de Dados Completo

O fluxo end-to-end de um orçamento segue 7 estágios:

|       |                          |                                   |                                        |
| ----- | ------------------------ | --------------------------------- | -------------------------------------- |
| **#** | **Estágio**              | **Input**                         | **Output**                             |
| 1     | Recepção do Escopo       | PDF/doc do cliente, e-mail, BC3   | Texto estruturado, itens identificados |
| 2     | Parse e Estruturação     | Texto bruto do escopo             | WBS preliminar, lista de serviços      |
| 3     | Match de Composições     | Lista de serviços                 | Composições sugeridas (IA + busca)     |
| 4     | Resolução de Preços      | Composições selecionadas          | Custo unitário base por composição     |
| 5     | Aplicação de Fatores     | Custos base + contexto do projeto | Faixa min/provável/máx ajustada        |
| 6     | Auditoria e Consistência | Orçamento montado                 | Alertas, inconsistências, benchmarks   |
| 7     | Geração de Proposta      | Orçamento auditado + template     | Proposta comercial formatada           |

### 1.2.1 Comunicação entre Componentes

Toda comunicação frontend ↔ backend passa pelas Edge Functions do Supabase, que atuam como API Gateway. O frontend nunca acessa o PostgreSQL diretamente para operações de cálculo — apenas para leitura de dados via Supabase Client (que já aplica RLS).

**Frontend → Edge Function:** HTTP POST com payload JSON. Exemplo: POST /functions/v1/calculate-budget com body contendo IDs das composições, quantitativos e parâmetros do projeto.

**Edge Function → PostgreSQL:** Queries via supabase-js (server-side, com service_role key). Para cálculos pesados, chama stored procedures (PL/pgSQL) que rodam no banco.

**Edge Function → Claude API:** Chamada HTTP para api.anthropic.com. A Edge Function monta o prompt com contexto do orçamento, envia e parseia a resposta estruturada (JSON).

## 1.3 Decisões de Arquitetura e Justificativas

|   |   |   |
|---|---|---|
|**Decisão**|**Alternativas Avaliadas**|**Justificativa**|
|**Supabase como backend**|Firebase, AWS Amplify, backend custom (Node/Express)|PostgreSQL nativo (vs NoSQL), RLS embutido, Edge Functions com Deno, auth pronto. Custo previsível. Já em uso no PowerConcept.|
|**Edge Functions (não serverless AWS)**|AWS Lambda, Vercel Functions, Cloud Functions|Latência mínima com Supabase (mesma infra), sem cold start significativo, Deno é TypeScript nativo.|
|**Claude API (não GPT/Gemini)**|OpenAI GPT-4, Google Gemini, Llama local|Melhor aderência a instruções longas, output estruturado mais confiável, contexto longo (200k tokens). Você já conhece a API.|
|**PostgreSQL Functions para cálculo**|Cálculo no Edge Function, cálculo no frontend|Dados já estão no banco — evita round-trip. PL/pgSQL é otimizado para operações em conjunto. Escala melhor para orçamentos grandes (1000+ itens).|
|**BC3 como formato de troca**|CSV, JSON próprio, IFC|Padrão FIEBDC-3 é o formato da indústria para orçamentação. Interoperável com Arquimedes, Presto, TCQ. Parser já funcional.|
|**Versionamento de composições**|Edição in-place, soft-delete|Orçamentos são documentos legais. Se a composição muda depois de fechado o orçamento, ele deve manter o preço original. Imutabilidade garante isso.|

## 1.4 Padrões de Projeto Aplicados

**Strategy Pattern (Motor de Cálculo):** Cada tipo de fator de ajuste (região, complexidade, produtividade) é uma estratégia intercambiável. O motor aplica uma cadeia de estratégias ao custo base. Isso permite adicionar novos fatores sem alterar o código existente.

**Repository Pattern (Acesso a Dados):** Cada entidade (Insumo, Composição, Orçamento) tem um repository que encapsula queries. O motor de cálculo nunca faz SQL direto — sempre via repository. Facilita testes unitários e troca de fonte de dados.

**Observer Pattern (Eventos de Auditoria):** Toda mutação em dados críticos dispara um evento. Listeners gravam no audit_log. O frontend pode se inscrever para atualizações real-time via Supabase Realtime.

**Pipeline Pattern (Processamento de IA):** A leitura de escopo passa por um pipeline: extração de texto → normalização → classificação → match com composições. Cada estágio é independente e testável.