---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, pre-projeto, monte-carlo]
---

## Como produtos desse tipo são projetados no mundo

### Metodologia de desenvolvimento de produto (o que você perguntou)

O padrão pra desenvolver um produto de software/dados complexo como esse segue uma variação de **Stage-Gate** ou **Double Diamond**, usado por empresas como Google, Amazon, e também por empresas de engenharia como Bentley Systems e Autodesk:

### Fase 0: Discovery (4-6 semanas)

- ~~Pesquisa de mercado (quem mais faz isso, como, quanto cobram)~~
- ~~Entrevistas com usuários (orçamentistas, diretores de EPC)~~
- ~~Benchmark de produtos existentes (CostOS, Cleopatra, InEight, ProEst)~~
- ~~Definição do problema e hipóteses~~

### Fase 1: Definition (4-6 semanas)

- Arquitetura do modelo de dados
- Definição dos parâmetros e fontes
- Prototipagem do motor de cálculo (em planilha/Python primeiro)
- Wireframes das telas
- Business model canvas
- Análise de viabilidade financeira

### Fase 2: Design (4-6 semanas)

- Projeto executivo do software (specs de cada módulo)
- Modelo de ML definido (que algoritmo, que dados de treino)
- Plano de validação (como provar que o orçamento da IA é bom)
- UX/UI design
- Plano de dados (como coletar, limpar, manter)

### Fase 3: Development (12-24 semanas)

- Construção do MVP
- Testes com dados reais da Concept
- Iteração

## Sugestão de projeto (3-6 meses, ritmo de estudo + execução)

| Mês     | Fase        | Entrega                                                                                                            |
| ------- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| **1**   | Discovery   | Benchmark de CostOS/InEight/Cleopatra. Mapear todos os parâmetros. Definir escopo do MVP. Estudar AACE RP 18R-97.  |
| **2**   | Definition  | Arquitetura do modelo de dados. Protótipo do motor em Python/Excel. Definir quais fatores de ajuste entram no MVP. |
| **3**   | Design      | Spec completa do produto. Modelo de ML definido. Wireframes. Business case.                                        |
| **4-5** | Development | MVP funcionando com dados da Concept. Integração SINAPI + RSMeans + histórico.                                     |
| **6**   | Validation  | Testar com 3-5 orçamentos reais. Comparar resultado da IA vs orçamento manual. Medir acurácia.                     |

Quer que eu monte o briefing detalhado da Fase 1 (Discovery) pra você começar?
