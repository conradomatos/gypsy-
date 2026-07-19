---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, pre-projeto, apresentacao]
---

# CostAI — Mapa de Módulos (Arquitetura)

Data: 2026-04-03 Base: Planilha HOLLOS.xlsx (Pequenas Obras) — 37 abas mapeadas Status: Discussão

---

## Visão Geral

A planilha atual tem 37 abas que misturam dados de referência, calculadoras, configurações, resumos e planejamento. No CostAI, isso se reorganiza em **9 módulos** + **4 bancos de dados** + **3 motores de cálculo** + **outputs**.

---

## 1. BANCOS DE DADOS (Spec 0 — dados de referência)

São as tabelas mestras que alimentam todo o sistema. Vêm do Spec 0 (data engineering).

|ID|Módulo CostAI|Abas que alimentam|Registros estimados|
|---|---|---|---|
|BD-1|**Banco de Insumos / Materiais**|Base de Materiais (~2.879 linhas), BASE DADOS PAINEIS (~30.557 linhas Siemens)|~33.000 itens|
|BD-2|**Banco de Mão de Obra / Tabela Salarial**|Tabela de Entrada de Peços (116 linhas, 41 funções), Encargos (58 linhas)|~50 funções × versões|
|BD-3|**Banco de Equipamentos**|Equipamentos (70 itens), Cálculo Custo de Equipamentos (55 itens)|~120 itens|
|BD-4|**Banco de Itens de Canteiro**|Manutenção de Canteiro (22 itens), EPI e Ferramentas (16 itens)|~40 itens|

### BD-1: Banco de Insumos / Materiais

**Merge:** Base de Materiais + BASE DADOS PAINEIS + 5 outras fontes do Spec 0 (FAZZER, SINAPI-PR, RSMeans, Arquimedes, catálogo concorrente)

**Estrutura no CostAI:**

- Tabela `insumos`: código, descrição, unidade, família, subfamília, Hxh_unitário
- Tabela `precos_insumos`: insumo_id, fonte (Siemens/Concept/SINAPI/etc), preço, data_base, fornecedor
- Tabela `fatores_reajuste`: insumo_id, commodity (cobre/aço/PVC), Kcobre, fórmula de reajuste

**Decisão:** A fórmula de reajuste de cabos (aba Formula Reajuste Cabos) NÃO é uma aba — vira um **atributo do insumo** (commodity + Kcobre) + um **serviço de cotação** que puxa LME/câmbio atuais.

### BD-2: Banco de Mão de Obra

**Merge:** Tabela de Entrada de Preços + Encargos + EPI e Ferramentas (parcial)

**Estrutura no CostAI:**

- Tabela `funcoes`: código, descrição, categoria (MOD/MOI/Gerência), regime (CLT/PJ)
- Tabela `salarios`: funcao_id, valor_mensal_220h, dissídio_ano, periculosidade (bool), adicional_%
- Tabela `encargos_sociais`: grupo (A/B/C/D), item, alíquota_horista, alíquota_mensalista, versão
- Tabela `custos_funcionario`: funcao_id, epi_mensal, ferramentas_mensal (calculados de EPI e Ferramentas)

### BD-3: Banco de Equipamentos

**Merge:** Equipamentos + Cálculo Custo de Equipamentos

**Decisão:** Os dois se fundem. O cálculo de depreciação/combustível (aba Cálculo Custo) gera o valor/dia que aparece na aba Equipamentos. No CostAI = uma tabela com campos de custo (locação OU depreciação calculada).

### BD-4: Banco de Itens de Canteiro

**Merge:** Manutenção de Canteiro + EPI e Ferramentas (parcial)

---

## 2. MOTORES DE CÁLCULO (engines reutilizáveis)

Lógica de negócio pura, sem UI. Recebem inputs → retornam valores.

|ID|Motor|Abas que substitui|O que calcula|
|---|---|---|---|
|MC-1|**Motor de Composição de Custo HH**|COMPOSIÇÃO Hh, M.O.I, M.O.D. Elétrica, TAB HH|Salário → +encargos → +alimentação/transporte → +EPI → custo/hora sem BDI → custo/hora com BDI|
|MC-2|**Motor de BDI / Formação de Preço**|Administração Central IND, Impostos-industrial|Custo → +ADM Central → +impostos (ISS/PIS/COFINS/ICMS) → +lucro diferenciado (MO/Mat/Equip) → preço de venda|
|MC-3|**Motor de Reajuste de Commodities**|Formula Reajuste Cabos|Pi → +(ΔLMEf×US$f - ΔLMEi×US$i) × K/1000 → Preço reajustado. Extensível para aço, alumínio.|

### MC-1: Motor de Composição de Custo HH

**O que absorve:** 6 abas (COMPOSIÇÃO Hh + M.O.I + M.O.D. Elétrica + TAB HH + parcial de Mobilização + parcial de Desmobilização)

**Fórmula core:**

```
Custo_Funcionario_Mes = Salário + Periculosidade + Encargos_Sociais
                      + Alimentação + Transporte + EPI + Ferramentas
                      + Exames + Seguro_Vida + Hospedagem

Custo_HH_sem_BDI = Custo_Funcionario_Mes / Horas_Mes (180 ou 220)
Custo_HH_com_BDI = Custo_HH_sem_BDI / (1 - BDI%)

HE_50% = Custo_HH × 1.5
HE_100% = Custo_HH × 2.0
Noturno = Custo_HH × 1.2
```

**Input:** função, regime, local da obra (afeta alimentação/transporte/hospedagem), dissídio vigente **Output:** custo HH por função em 4 modalidades (normal, HE50%, HE100%, noturno) + preço de venda HH

### MC-2: Motor de BDI / Formação de Preço

**O que absorve:** Administração Central IND + Impostos-industrial + bloco "Encargos sobre Faturamento" que aparece em ~8 abas

**Nota:** O bloco "2 - ENCARGOS SOBRE FATURAMENTO DE SERVIÇOS" (ISS 3%, PIS 0,65%, COFINS 3%, ADM 10%, Lucro 15%, IR 4,8%, IR Adicional 3,2%, CSLL 2,88% = **42,53%**) se repete identicamente em: PROJETOS, Manutenção de Canteiro, Equipamentos, Seguros e Outros, Mobilização, Desmobilização, Despesas Viagens, Prog. Segurança. No CostAI isso é UM motor chamado uma vez com parâmetros.

**Cenários:**

- "Todo Fornecimento" (Concept compra e fornece) vs "Faturamento Direto" (cliente compra material)
- Lucro diferenciado: MO Direta 15%, Materiais 12%, Equipamentos 15%, Terceiros 15%

### MC-3: Motor de Reajuste de Commodities

Absorve a aba Formula Reajuste Cabos. Extensível.

---

## 3. MÓDULOS FUNCIONAIS (telas/features do CostAI)

| ID  | Módulo                              | Abas que absorve                                                           | Fase Jira |
| --- | ----------------------------------- | -------------------------------------------------------------------------- | --------- |
| M-1 | **Cadastro do Orçamento**           | LEVANTAMENTO (cabeçalho + flags)                                           | —         |
| M-2 | **Dimensionador de Força**          | Alimentação-industrial                                                     | F1        |
| M-3 | **Dimensionador de Instrumentação** | Instrumentação-industrial                                                  | F5        |
| M-4 | **Configurador de Painéis**         | Paineis (2)                                                                | F5        |
| M-5 | **Quantitativo de Materiais (BOM)** | Materiais-industrial                                                       | F2/F3     |
| M-6 | **Mobilização / Desmobilização**    | Mobilização, Desmobilização, LEVANTAMENTO (bloco mob/desmob)               | F2        |
| M-7 | **Custos Complementares**           | Seguros e Outros, PROJETOS, Prog. Segurança, Despesas Viagens, Pintura     | F2        |
| M-8 | **Horas Improdutivas**              | Horas improdutivas                                                         | F2        |
| M-9 | **Resumo / Dashboard**              | RESUMO PREÇOS Industrial, Custo Obra_Industrial, Custos MOI Mensal, TAB HH | F6/F7     |

### M-1: Cadastro do Orçamento

**Absorve:** Cabeçalho do LEVANTAMENTO (linhas 3-9) + Flags de cliente (linhas 12-16)

**No CostAI:** Tela de criação do orçamento com:

- Metadados: nº, cliente, obra, local, data, revisão, tipo (Industrial/Predial)
- **Perfil do cliente** (substituindo flags hardcoded): seleção de perfil (VALE/Klabin/genérico) que ativa/desativa regras automaticamente
- Parâmetros globais: dias integração, faturamento direto (sim/não)

**Decisão sobre flags:** "Padrão VALE", "Padrão Klabin", "Lixo Classe 2", "Plano Saúde" viram **perfis de cliente configuráveis**, não checkboxes com nome de empresa.

### M-2: Dimensionador de Força (Alimentação-industrial)

Maior módulo. 631 linhas, 9.326 fórmulas. Já mapeado como F1 no Jira.

**No CostAI:** Módulo dedicado que recebe lista de cargas (motor/iluminação com KW, V, distância) e calcula: corrente, bitola de cabo, eletroduto, leito, terminais. Output = lista de materiais que alimenta M-5.

Itens avulsos do LEVANTAMENTO (fibra óptica, proteção passiva) ficam em M-5 como input manual.

### M-3: Dimensionador de Instrumentação

**No CostAI:** Análogo ao M-2 mas para instrumentação. Input = quantidade de instrumentos por tipo (TT, PDT, FT, LT, válvulas) × distância média → Output = BOM de instrumentação.

Cada tipo de instrumento = um **assembly** (composição padrão).

### M-4: Configurador de Painéis

**No CostAI:** Input = tipo de partida (Direta/ET/SS/Inversor) × potência (kW) → Output = BOM do painel (disjuntor, contator, relé, bornes, etc.) com preço.

Usa BD-1 (catálogo Siemens) como fonte de preços dos componentes.

### M-5: Quantitativo de Materiais (BOM)

**Absorve:** Materiais-industrial (966 linhas, 10.458 fórmulas)

**No CostAI:** View consolidada que agrega:

- Output do M-2 (Dimensionador de Força) → cabos, eletrodutos, leitos
- Output do M-3 (Dimensionador de Instrumentação) → cabos sinal, tubing, conectores
- Output do M-4 (Painéis) → componentes de painéis
- Itens manuais (input direto do usuário)

Multiplicadores por categoria (cabos, eletrodutos, leitos, ferragens, demais) = **F_escala**. Separação CONCEPT/DIRETO = regra de Condições Comerciais. Preços vêm de BD-1, Hxh de BD-1.

### M-6: Mobilização / Desmobilização

**Merge:** Mobilização + Desmobilização + bloco mob/desmob do LEVANTAMENTO + bloco Hospedagem do LEVANTAMENTO + bloco Veículos do LEVANTAMENTO

**No CostAI:** Uma única calculadora com toggle Mob/Desmob. Inputs: equipe (função × qtd × dias), hospedagem, alimentação, transporte, veículos. Usa MC-1 para custo HH.

### M-7: Custos Complementares

**Merge:** Seguros e Outros + PROJETOS + Prog. Segurança + Despesas Viagens + Pintura

**No CostAI:** Coleção de itens de custo "avulsos" que não vêm dos dimensionadores. Cada um é uma mini-composição:

- Seguros: % do contrato (Performance Bond, RC) ou valor fixo (ART)
- Projetos: Hxh engenheiro × custo/hora
- Segurança: itens obrigatórios × efetivo
- Viagens gerenciais: itens × quantidade
- Pintura: m² calculado dos perfis × custo/m²

Todos passam pelo MC-2 (BDI) com o mesmo bloco de encargos 42,53%.

### M-8: Horas Improdutivas

**No CostAI:** Calculador do F_produtividade. Inputs: distância casa-obra, tempo DDS, tempo liberação frentes → Output: % improdutivo que ajusta Hxh em toda a BOM.

Já mapeado em F2 do Jira.

### M-9: Resumo / Dashboard

**Absorve:** RESUMO PREÇOS Industrial + Custo Obra_Industrial + Custos MOI Mensal + TAB HH

**No CostAI:** View gerada automaticamente. Não é input — é output. Contém:

- EAP hierárquica do orçamento (1. Gerenciamento, 2. Engenharia, 3. Montagem...)
- Hxh total por seção, Serviços, Materiais
- Curva ABC (MO e Materiais)
- KPI: Valor HH médio equipado (sanity check do Sandro)
- BDI detalhado: lucro MO × lucro materiais × impostos
- **Preço total do orçamento**

---

## 4. FORA DO MVP (Planejamento)

|Aba|Motivo|Futuro?|
|---|---|---|
|histograma|Cronograma de alocação semanal — planejamento de execução, não orçamento|Sim, v2|
|Cronograma de Desembolso|Fluxo de caixa do projeto — vai além de custo|Sim, v2|
|Cronograma macro|Gantt de execução|Sim, v2 (ou integra com PWC)|
|Custo Obra_Industrial (parte "Realizado")|Controle de custos durante obra — escopo de ERP/PWC|Não — pertence ao PWC|

**Nota:** O histograma ALIMENTA o cálculo de MOD/MOI (dias × pessoas). No MVP, o CostAI precisa de um **estimador simplificado de equipe** (prazo × composição de equipe → Hxh total) sem o grid semanal completo.

---

## 5. DESCARTE

|Aba|Motivo|
|---|---|
|Cronograma macro|Template de projeto antigo (2014), dados específicos|

---

## 6. FLUXO DE DADOS (como tudo se conecta)

```
[BD-1 Insumos] ──────────────────────────────────────────┐
[BD-2 MO] ──→ [MC-1 Composição HH] ──→ Custo HH/função  │
[BD-3 Equipamentos] ──────────────────────────────────────┤
[BD-4 Canteiro] ──────────────────────────────────────────┤
                                                          │
[M-1 Cadastro] ──→ Parâmetros globais ────────────────────┤
                                                          │
[M-2 Dimensionador Força] ────→ BOM Força ────────────────┤
[M-3 Dimensionador Instrumentação] ──→ BOM Instrum. ──────┤
[M-4 Configurador Painéis] ──→ BOM Painéis ───────────────┤
                                                          ▼
                                              [M-5 BOM Consolidado]
                                                     │
                    ┌──────────────────────────────────┤
                    ▼                                  ▼
         [M-8 Horas Improdutivas]          [M-6 Mob/Desmob]
         (ajusta Hxh total)                [M-7 Custos Complementares]
                    │                                  │
                    └──────────┬───────────────────────┘
                               ▼
                      [MC-2 Motor BDI]
                      (aplica impostos, lucro, ADM)
                               │
                               ▼
                      [M-9 RESUMO / DASHBOARD]
                      (EAP + Curva ABC + KPIs)
                               │
                               ▼
                      [Monte Carlo Beta-PERT]
                      (min/provável/máx)
                               │
                               ▼
                      [Export: Excel + PDF Proposta]
```

---

## 7. MAPA DE ABSORÇÃO (Aba → Módulo CostAI)

| #   | Aba Original                | Tipo         | → Módulo CostAI                        | Ação                                       |
| --- | --------------------------- | ------------ | -------------------------------------- | ------------------------------------------ |
| 1   | Formula Reajuste Cabos      | PARAMETRO    | MC-3 Motor Reajuste                    | **ABSORVE** — vira atributo do insumo      |
| 3   | LEVANTAMENTO                | CONFIG       | M-1 Cadastro + M-6 Mob (parcial)       | **DECOMPÕE** em 2 módulos                  |
| 4   | Administração Central IND   | CALCULO_BDI  | MC-2 Motor BDI                         | **ABSORVE**                                |
| 5   | Alimentação-industrial      | CALCULADORA  | M-2 Dimensionador Força                | **MIGRA** (módulo dedicado)                |
| 6   | Pintura                     | CALCULO      | M-7 Custos Complementares              | **ABSORVE** como sub-composição            |
| 7   | Base de Materiais           | BASE_DADOS   | BD-1 Banco de Insumos                  | **MIGRA** (fonte primária)                 |
| 8   | Impostos-industrial         | IMPOSTO      | MC-2 Motor BDI                         | **ABSORVE**                                |
| 9   | Horas improdutivas          | PARAMETRO    | M-8 Horas Improdutivas                 | **MIGRA** (calculador F_produtividade)     |
| 10  | Materiais-industrial        | ORCAMENTO    | M-5 BOM Consolidado                    | **MIGRA** (view calculada)                 |
| 13  | Instrumentação-industrial   | CALCULADORA  | M-3 Dimensionador Instrumentação       | **MIGRA** (módulo dedicado)                |
| 14  | RESUMO PREÇOS Industrial    | RESUMO       | M-9 Dashboard                          | **MIGRA** (output automático)              |
| 15  | BASE DADOS PAINEIS          | BASE_DADOS   | BD-1 Banco de Insumos                  | **MIGRA** (sub-catálogo Siemens)           |
| 16  | Paineis (2)                 | CONFIGURADOR | M-4 Configurador Painéis               | **MIGRA** (módulo dedicado)                |
| 17  | histograma                  | PLANEJAMENTO | Fora MVP                               | **POSTERGA** → v2                          |
| 18  | Custos MOI Mensal           | RESUMO       | M-9 Dashboard                          | **ABSORVE** (view derivada)                |
| 19  | Cronograma Desembolso       | PLANEJAMENTO | Fora MVP                               | **POSTERGA** → v2                          |
| 20  | Cronograma macro            | PLANEJAMENTO | —                                      | **DESCARTA** (sujeira)                     |
| 21  | PROJETOS                    | CALCULO      | M-7 Custos Complementares              | **ABSORVE**                                |
| 22  | Manutenção de Canteiro      | CALCULO      | BD-4 + M-7                             | **DECOMPÕE** (dados → BD-4, cálculo → M-7) |
| 23  | Equipamentos                | BASE_DADOS   | BD-3 + M-7                             | **DECOMPÕE** (dados → BD-3, cálculo → M-7) |
| 24  | Tabela Entrada de Preços    | BASE_DADOS   | BD-2 Banco de MO                       | **MIGRA**                                  |
| 25  | Cálculo Custo Equipamentos  | CALCULO      | BD-3 (calculador interno)              | **ABSORVE**                                |
| 26  | M.O.I                       | CALCULO      | MC-1 Motor Composição HH               | **ABSORVE**                                |
| 27  | COMPOSIÇÃO Hh               | COMPOSICAO   | MC-1 Motor Composição HH               | **ABSORVE** (é o core do MC-1)             |
| 28  | M.O.D. Elétrica             | CALCULO      | MC-1 Motor Composição HH               | **ABSORVE**                                |
| 29  | TAB HH                      | RESUMO       | M-9 Dashboard                          | **ABSORVE** (output do MC-1)               |
| 30  | EPI e Ferramentas           | BASE_DADOS   | BD-4 + BD-2                            | **DECOMPÕE**                               |
| 31  | Seguros e Outros            | CALCULO      | M-7 Custos Complementares              | **ABSORVE**                                |
| 32  | Custo Obra_Industrial       | CONTROLE     | M-9 (parcial orçado) + PWC (realizado) | **DECOMPÕE**                               |
| 33  | Mobilização                 | CALCULO      | M-6 Mob/Desmob                         | **MERGE** com Desmobilização               |
| 34  | Desmobilização              | CALCULO      | M-6 Mob/Desmob                         | **MERGE** com Mobilização                  |
| 35  | Encargos                    | BASE_DADOS   | BD-2 Banco de MO                       | **MIGRA** (tabela de encargos)             |
| 36  | Despesas Viagens Gerenciais | CALCULO      | M-7 Custos Complementares              | **ABSORVE**                                |
| 37  | Prog. Segurança e Exames    | CALCULO      | M-7 Custos Complementares              | **ABSORVE**                                |

---

## 8. CONTAGEM FINAL

|Categoria|Quantidade|Abas absorvidas|
|---|---|---|
|Bancos de Dados (BD)|4|10 abas|
|Motores de Cálculo (MC)|3|8 abas|
|Módulos Funcionais (M)|9|16 abas|
|Fora MVP|3|3 abas|
|Descarte|1|1 aba|
|**Total**|**20 componentes**|**37 abas (exceto 1 descartada)**|

37 abas → 16 componentes (4 BD + 3 MC + 9 M) + outputs automáticos.

---

## 9. OBSERVAÇÕES PARA DISCUSSÃO

1. **O bloco "Encargos sobre Faturamento" (42,53%)** se repete em 8 abas com valores idênticos. No CostAI é uma chamada ao MC-2 com parâmetros. Economia brutal de complexidade.
    
2. **COMPOSIÇÃO Hh é o cálculo mais crítico** — dele derivam todos os preços de MO. Se errar aqui, o orçamento inteiro está errado. Precisa de validação com Sandro como primeira coisa.
    
3. **O LEVANTAMENTO mistura 5 módulos** numa única tela. A decomposição em M-1/M-6/M-7/M-8 é a mudança mais visível para o usuário.
    
4. **BASE DADOS PAINEIS (30k linhas Siemens jan/2019)** precisa de atualização de preços. No CostAI, o catálogo Siemens entra como fonte no BD-1 com data_base e mecanismo de atualização.
    
5. **Histograma e Cronograma de Desembolso** ficam fora do MVP mas o CostAI precisa de um **estimador simplificado de equipe** para calcular MOD/MOI sem o grid semanal completo.
    
6. **Custo Obra_Industrial (Orçado vs Realizado)** tem a parte "Orçado" que vai pro M-9 e a parte "Realizado" que pertence ao PWC (controle de obra), não ao CostAI (estimativa).


![[Pasted image 20260403235436.png]]

![[Pasted image 20260404011538.png]]