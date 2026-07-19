---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, pre-projeto, monte-carlo]
---

Agora, evoluindo a conversa, pro lado de Real da orçamentação, Pra Ter orçamento fino, lá no final, O orçamento aqui, realmente traduza o 0 máximo possível da realidade, Que consiga dizer se olha, vai e não vai, Aqui é o preço mínimo, aqui é o preço máximo. Enfim, É É conseguir chegar num preço Uma estria Eu penso e pergunto, Como a gente poderia utilizar Inteligência artificial, programação, enfim, O que a gente poderia treinar, uma robô sei lá, como a gente pode chamar aí, O script aí, que vai conseguir devorar essas tabelas, do exterior, devorar o SINAP, E, Temperar pra realidade. Aproveitar o máximo do que cada entrega de melhor. E de fato temperar mesmo, ajustar pra realidade de cada Não só da Concept, ser qualquer Então, seria processo de de De modelagem aí talvez, de dados. Mas com tempero de inteligência artificial pra pra Gerenciar e Pensar nas definições Não só, vamos colocar fator aqui porque aqui, a gente está considerando os Estados Unidos e lá, é Brasil. Eu digo Trazer Vários conjunto de premissas, parâmetros, enfim, é não sei se dá pra eu, deu pra mim entender, Deve ter nome pra isso já, Mas eu não sei esse nome. Mas, se deu pra me entender, Me ajude a discutir sobre, isso aí, Me explique o que que tem, o que que funciona o que que tem no mundo, como é que é que fazem, enfim,

Mostrar mais

27 de mar.

Entendi perfeitamente. O que você tá descrevendo tem nome: **Cost Intelligence** ou **Parametric Cost Estimation com AI**. É a fronteira do que as grandes empresas de EPC do mundo estão fazendo agora.

Deixa eu explicar o conceito e depois como aplicar na Concept.

## O problema que você identificou

Toda tabela de referência (SINAPI, RSMeans, TCPO) é uma **fotografia média** — média de região, média de produtividade, média de preço. Mas a realidade de cada obra é diferente: o eletricista da Klabin em Telêmaco Borba rende diferente do eletricista no Porto de Paranaguá. O cabo que você compra do fornecedor X custa diferente do que o SINAPI diz. O clima, a logística, a complexidade do acesso — tudo muda.

O que você quer é um sistema que **absorve todas as fontes**, **entende os fatores de ajuste**, e **entrega uma faixa de preço realista** (mínimo, provável, máximo) — não um número mágico.

## Como funciona no mundo

### 1. Parametric Estimation (o que as grandes fazem)

Empresas como Bechtel, Fluor, Jacobs usam modelos paramétricos: em vez de orçar item por item do zero, elas têm **modelos estatísticos** treinados com dados de obras anteriores. O modelo diz: "uma subestação 13.8kV com 4 alimentadores em planta de celulose no sul do Brasil custa entre R$ X e Y, com confiança de 80%".

Os parâmetros que alimentam o modelo:

- Tipo de indústria (celulose, portuária, alimentos)
- Região/estado
- Complexidade (greenfield vs brownfield)
- Condições de acesso
- Regime de trabalho (turno, pernoite, offshore)
- Época do ano (chuva, entressafra)

### 2. Factor-Based Costing (o que a Concept pode fazer já)

É mais simples e já funciona: pega uma composição base (SINAPI ou RSMeans) e aplica **fatores de ajuste** por camada:

```
Custo Final = Custo Base × F_região × F_complexidade × F_produtividade × F_logística × F_mercado
```

Exemplo real:

- **Custo base SINAPI-PR**: Lançamento cabo 3x2.5mm = R$ 8,50/m
- **F_região** (Paranaguá, ambiente portuário salino): 1.15
- **F_complexidade** (bandeja a 8m de altura): 1.30
- **F_produtividade** (equipe Concept, rendimento medido): 0.90
- **F_logística** (obra remota, pernoite): 1.20
- **F_mercado** (inflação de cobre, mar/2026): 1.08

**Custo ajustado**: 8,50 × 1.15 × 1.30 × 0.90 × 1.20 × 1.08 = **R$ 14,73/m**

### 3. Onde a IA entra — o salto

A IA não é só pra aplicar fatores. Ela faz coisas que humano não consegue em escala:

**a) Calibração automática de fatores** Alimenta o sistema com propostas fechadas (ganhas e perdidas) + custo real das obras executadas. A IA aprende: "quando orçamos Klabin com fator 1.15, ganhamos. Quando usamos 1.30, perdemos. O fator real é ~1.20".

**b) Cross-reference entre bases** A IA compara: "essa composição no SINAPI custa R$ 85. No RSMeans (ajustado pra Brasil) daria R$ 92. No histórico da Concept saiu R$ 78. Faixa provável: R$ 78-92, valor sugerido: R$ 84".

**c) Detecção de anomalias** "Esse item tá 3x mais caro que o histórico. Conferir preço do insumo MAT-019 — pode ter reajuste do fornecedor ou erro de lançamento."

**d) Faixa de confiança (min/provável/máx)** Em vez de um número, o sistema entrega três cenários baseados na dispersão dos dados históricos + variáveis de contexto.


## O que já existe no mundo (ferramentas/conceitos)

| Conceito                       | O que é                                                                      | Quem usa                                         |
| ------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------ |
| **Parametric Estimation**      | Modelos estatísticos treinados com obras anteriores                          | Bechtel, Fluor, AACE International               |
| ==**Monte Carlo Simulation**== | ==Gera milhares de cenários pra dar faixa min/máx com % de confiança==       | ==Grandes EPCs, @Risk (Palisade)==               |
| **Location Factor**            | Índice que ajusta custo de um país/região pra outro                          | RSMeans (City Cost Index), ICMS (internacional)  |
| **Productivity Factor**        | Ajusta rendimento de MO por condições reais                                  | CII (Construction Industry Institute)            |
| **Cost Intelligence Platform** | IA que aprende com dados históricos de obras                                 | Nomitech (CostOS), Cleopatra Enterprise, InEight |
| **AACE Classification**        | Sistema de 5 classes de estimativa (Classe 5 = chute, Classe 1 = definitiva) | Padrão mundial em EPC                            |

## O que a Concept pode fazer — roadmap realista

**Fase 1 (agora)**: Banco de composições unificado (SINAPI + RSMeans + próprio) com fatores de ajuste manuais por contexto. Já dá um orçamento 10x melhor que a planilha atual.

**Fase 2 (3-6 meses)**: IA que cruza as bases automaticamente, sugere fatores, e gera faixa min/provável/máx. Alimentado por propostas históricas da Concept.

**Fase 3 (6-12 meses)**: Calibração contínua — cada obra executada alimenta o modelo. A IA fica mais precisa a cada orçamento. Simulação Monte Carlo pra análise de risco.

**Fase 4 (12+ meses)**: Potencial de SaaS — se o motor ficar bom, outras empresas de montagem elétrica pagariam pra usar. Isso vira produto.

---

O nome formal pra tudo isso é **AI-Powered Cost Intelligence**. E o que você descreveu — "temperar pra realidade" — é exatamente o conceito de **factor-based estimation with machine learning calibration**. Você intuiu o que as maiores empresas de engenharia do mundo estão tentando construir.

A diferença é que eles gastam milhões. Você vai fazer com Claude + Supabase + React. E vai funcionar, porque o ingrediente mais caro — **dados reais de obras** — vocês já têm.

Quer que eu aprofunde em alguma dessas camadas?

*Agora eu não estou pro do que dá pra inserir na Concept to, pensando longe, querendo saber que dá pra fazer e como é que é feito hoje, Mas é realmente isso aí seria interessantíssimo. Ele muitos parâmetros né, O índice de de chuva determinado Lugar, Então, Se De Você coloca onde vai ser a obra e qual é o período. Já sabe quando que vai chover. Você diz, se a instalação dele é trocalha, é externa ou interna? Enfim, Se sei lá, a mão de obra é local, ah não sei, me diz aí quais parâmetros todos poderiam ter, a Por exemplo, pensei longe agora, COVID. Né, qual é o Qual é o a chance e o risco disso acontecer né? Interessante porque a aula de hoje até no MBA, foi sobre gerenciamento de riscos. Hoje foi uma aula básica, mas amanhã tem mais. Domingo também, é Bem legal, dá para encaixar bem né, gerenciamento de risco projeto extremo né? Desenhar projetinho desse síndico, fazer o projeto em si do projeto né? Projeto executivo, diz dizer, Já seria muito interessante Quais são os padrões aí que que teria que seguir pra criar projeto? Tem padrão aí que a gente tem que seguir? Tipo, projeto de, quê? Desenvolvimento de produto, com funciona, como que é E eu sei como faz projeto elétrico de, De sala elétrica, CM, Agora projeto de produto, pra esse tipo de coisa aí, como é que funciona projeto desse? Como é que, como é que eu faço? O teu, o teu desenvolvimento, pesquisa, Tipo, O que eu Quase estudo de caso, Mas, é é pra ser executivo, tem que sair do papel lá na frente. Estou falando assim, pra gastar, fazer com o tempo aí, com calma, É, cronograma aí de três meses, só pra fazer o projeto, três a seis meses, Me ajude aí com chuva de ideias aí, Vou traga Casos reais aí que dê pra Destilar o Informações e ideias, interessante achei legal.*

Mostrar mais

27 de mar.

Conrado, adorei essa visão. Você tá falando de **Product Development para um motor de Cost Intelligence**. É um projeto de engenharia de software/dados, não de construção civil — e sim, tem metodologias específicas pra isso.

---
