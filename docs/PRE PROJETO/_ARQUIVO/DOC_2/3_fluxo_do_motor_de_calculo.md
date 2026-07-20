---
tipo: referencia
status: arquivado
area: gypsy
tags: [gypsy, pre-projeto, doc2]
---

## 3.1 Visão Geral

O motor de cálculo transforma uma composição em custo final ajustado em 5 passos: resolução de componentes, cálculo de custo base, aplicação de fatores, geração de faixa de preços, e aplicação de BDI. A seguir, cada passo com exemplo numérico real.

## 3.2 Exemplo Numérico: Eletroduto Galvanizado 1 pol

Composição: Instalação de eletroduto galvanizado 1" (25mm) em leito/bandeja, incluindo conexões, fixação e acessórios. Unidade: metro (m).

### 3.2.1 Passo 1 — Resolução de Componentes

O motor busca todos os itens_composicao vinculados, resolve preços atuais de cada componente e calcula o custo parcial.

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|**#**|**Componente**|**Un**|**Coef.**|**Preço Un.**|**Parcial**|**Fonte**|
|1|Eletroduto galv. 1" (barra 3m)|m|1,0500|R$ 18,72|R$ 19,66|SINAPI-PR mar/26|
|2|Curva 90° galv. 1"|un|0,2500|R$ 8,45|R$ 2,11|SINAPI-PR mar/26|
|3|Luva galv. 1"|un|0,3500|R$ 4,20|R$ 1,47|SINAPI-PR mar/26|
|4|Abraçadeira tipo D 1"|un|0,5000|R$ 2,85|R$ 1,43|Concept|
|5|Parafuso + bucha S8|un|0,5000|R$ 0,65|R$ 0,33|Concept|
|6|Eletricista (oficial)|h|0,3500|R$ 42,18|R$ 14,76|Concept (c/ enc.)|
|7|Ajudante de eletricista|h|0,3500|R$ 28,94|R$ 10,13|Concept (c/ enc.)|

### 3.2.2 Passo 2 — Cálculo do Custo Base

Soma de todos os custos parciais:

**Custo Base =** 19,66 + 2,11 + 1,47 + 1,43 + 0,33 + 14,76 + 10,13 = **R$ 49,89/m**

Decomposição por natureza:

•        Material: R$ 25,00/m (50,1%)

•        Mão de Obra: R$ 24,89/m (49,9%)

### 3.2.3 Passo 3 — Aplicação de Fatores de Ajuste

Os fatores são aplicados como multiplicadores encadeados sobre o custo base. Para este exemplo, considere um projeto de montagem industrial em Telêmaco Borba/PR (Klabin):

|   |   |   |   |   |
|---|---|---|---|---|
|**Fator**|**Valor**|**Multiplicador**|**Aplica sobre**|**Justificativa**|
|Regionalização (PR interior)|+5%|1,05|Material|Frete interior PR vs capital|
|Complexidade industrial|+15%|1,15|MO|Ambiente industrial (NR-10, NR-33, NR-35)|
|Produtividade (parada programada)|-10%|0,90|MO|Trabalho em parada: produtividade menor|
|Logística (canteiro grande)|+3%|1,03|Total|Deslocamento dentro da planta|

**Cálculo encadeado:**

Material ajustado: R$ 25,00 × 1,05 (região) = R$ 26,25

MO ajustada: R$ 24,89 × 1,15 (complexidade) × 0,90 (produtividade) = R$ 25,76

Subtotal: R$ 26,25 + R$ 25,76 = R$ 52,01

Com logística: R$ 52,01 × 1,03 = R$ 53,57/m

**Custo Direto Ajustado = R$ 53,57/m** (vs R$ 49,89 base — aumento de 7,4%)

### 3.2.4 Passo 4 — Faixa de Preços (Min/Provável/Máx)

O motor aplica coeficientes de variação para gerar a faixa triplice. Os coeficientes são calibrados por categoria de serviço com base em histórico de obras:

•        Mínimo: custo ajustado × 0,85 (cenário otimista: condições ideais, equipe experiente, sem imprevistos)

•        Provável: custo ajustado × 1,00 (cenário base)

•        Máximo: custo ajustado × 1,25 (cenário pessimista: atrasos, retrabalho, condições adversas)

|   |   |   |   |
|---|---|---|---|
||**Mínimo**|**Provável**|**Máximo**|
|**Custo Direto (/m)**|R$ 45,53|R$ 53,57|R$ 66,96|
|**Coeficiente**|× 0,85|× 1,00|× 1,25|

**Nota:** Os coeficientes 0,85/1,00/1,25 são valores iniciais. Com o acumulo de histórico de obras, o motor de machine learning calibra esses coeficientes por tipo de serviço. Exemplo: eletroduto em área industrial pode ter min/max mais apertado (0,90/1,15) se o histórico mostra baixa variabilidade.

### 3.2.5 Passo 5 — Aplicação do BDI

O BDI transforma custo direto em preço de venda. Usando o perfil BDI Obra Privada com BDI = 26,76%:

Preço Venda = Custo Direto × (1 + BDI)

|   |   |   |   |
|---|---|---|---|
||**Mínimo**|**Provável**|**Máximo**|
|**Custo Direto (/m)**|R$ 45,53|R$ 53,57|R$ 66,96|
|**BDI (26,76%)**|R$ 12,18|R$ 14,33|R$ 17,91|
|**PREÇO DE VENDA (/m)**|**R$ 57,71**|**R$ 67,90**|**R$ 84,87**|

### 3.2.6 Resultado Consolidado

Para um orçamento com 500m de eletroduto galvanizado 1":

|   |   |   |   |
|---|---|---|---|
|**500m de eletroduto 1"**|**Mínimo**|**Provável**|**Máximo**|
|**Custo Direto**|R$ 22.765|R$ 26.785|R$ 33.480|
|**Preço de Venda (c/ BDI)**|**R$ 28.855**|**R$ 33.950**|**R$ 42.435**|

_O orçamentista apresenta ao cliente o valor provável (R$ 33.950) e usa a faixa min/máx para negociação e análise de risco. A IA pode alertar: "O item eletroduto 1" representa 12% do orçamento total. Variação de 30% entre min/max. Recomendo fixar preço com fornecedor para reduzir risco."_

  

## 3.3 Fluxo Técnico do Motor (Pseudocódigo)

Abaixo, o fluxo simplificado em pseudocódigo de como a Edge Function orquestra o cálculo:

async function calcularOrcamento(orcamentoId, projetoId) {

  // 1. Buscar itens do orçamento com composições

  const itens = await repo.getItensOrcamento(orcamentoId);

  const fatores = await repo.getFatoresProjeto(projetoId);

  const bdi = await repo.getBDIPerfil(orcamento.encargo_bdi_id);

  for (const item of itens) {

    // 2. Resolver composição (recursivo se tem sub-composições)

    const custoBase = await resolverComposicao(item.composicao_id);

    // 3. Aplicar fatores (Strategy Pattern)

    let custoAjustado = custoBase;

    for (const fator of fatores) {

      custoAjustado = fator.strategy.apply(custoAjustado, fator.valor);

    }

    // 4. Gerar faixa de preços

    const faixa = {

      min: custoAjustado * item.coef_min,   // default 0.85

      provavel: custoAjustado,

      max: custoAjustado * item.coef_max,   // default 1.25

    };

    // 5. Aplicar BDI

    item.preco_venda = {

      min: faixa.min * (1 + bdi.bdi_total),

      provavel: faixa.provavel * (1 + bdi.bdi_total),

      max: faixa.max * (1 + bdi.bdi_total),

    };

    // 6. Salvar com histórico (audit_log automático via trigger)

    await repo.updateItemOrcamento(item);

  }

  // 7. Totalizar orçamento

  return await repo.totalizarOrcamento(orcamentoId);

}

## 3.4 Resolução Recursiva de Composições

Uma composição pode conter sub-composições (ex: "Instalação elétrica de sala" contém a composição "Instalação de eletroduto 1""). O motor resolve recursivamente até chegar em componentes atômicos (insumos, MO, equipamentos).

**Proteção contra ciclos:** O motor mantém um Set de composicao_ids visitados. Se detectar referência circular, lança erro e marca a composição como inconsistente. Limite de profundidade: 10 níveis (configurável).

## 3.5 Ordem de Aplicação dos Fatores

A ordem de aplicação dos fatores impacta o resultado final. O motor aplica na seguinte sequência fixa:

•        Nível 1 — Fatores de componente: aplicados sobre material OU MO separadamente (ex: regionalização de material, complexidade de MO)

•        Nível 2 — Fatores de composição: aplicados sobre o subtotal da composição (ex: logística, produtividade)

•        Nível 3 — Fatores de projeto: aplicados sobre todo o orçamento (ex: mercado aquecido +5%, contingência de cronograma)

•        Nível 4 — BDI: sempre último, sobre o custo direto total ajustado

Dentro de cada nível, fatores são multiplicativos (encadeados). Entre níveis, a aplicação é sequencial.

## 3.6 Performance e Limites

**Orçamento típico (100-500 itens):** Resolução completa em < 2 segundos usando PostgreSQL functions (SET-based, sem loops).

**Orçamento grande (1000+ itens):** Resolução em < 10 segundos. Para estes casos, o motor usa cálculo incremental: só recalcula itens que mudaram desde a última execução.

**Cache de composições:** Composições resolvidas são cacheadas por (composicao_id + data_referencia). Invalidado quando qualquer componente é atualizado.