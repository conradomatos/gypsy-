---
name: extrair-fonte
description: Guia de extração por fonte de dados do projeto CostAI Destilação (mapeamento de abas para HOLLOS e MURILO, prioridades, composições paramétricas de Alimentação-industrial). Use ao extrair dados de uma fonte específica (Passo 2 do workflow em CLAUDE.md), não para consolidação ou validação.
---

## Fonte Atual: HOLLOS (ex-Planilha Pequenas Obras)

**Arquivo:** PLANILHA ORCAMENTOS - HOLLOS.xlsx
**Tamanho:** 5.1 MB | **Abas:** 35

### Mapeamento de abas → tabelas-destino:

| Aba | Tabela-Destino | Prioridade | Notas |
|-----|---------------|------------|-------|
| Base de Materiais | Insumos + Preços | ALTA | 2.982 linhas, tem preço unit/revenda/fabricante |
| BASE DADOS PAINEIS | Insumos | MEDIA | 30.557 itens Siemens (Jan/2019, defasado) |
| Tabela de Entrada de Preços | Mão de Obra | ALTA | 135 funções com salário, PJ/CLT, periculosidade |
| COMPOSIÇÃO Hh | Composições + Itens | ALTA | Composição salarial completa por função |
| Encargos | Encargos/BDI | ALTA | Encargos horista detalhado (Grupo A/B/C) |
| Horas Improdutivas | Referência (fator produtividade) | MEDIA | Não é tabela direta, é parâmetro |
| Impostos-industrial | Encargos/BDI | ALTA | Impostos por cenário |
| Equipamentos | Equipamentos | ALTA | Ferramentas e equipamentos de obra |
| Cálculo Custo Equipamentos | Equipamentos | ALTA | Caminhões/guindastes com depreciação |
| EPI e Ferramentas | Equipamentos | MEDIA | Custo depreciado por item |
| Materiais - industrial | Composições (implícitas) | ALTA | FÓRMULAS — composições embutidas com multiplicadores |
| Alimentação-industrial | Composições (implícitas) | ALTA | Alimentadores — composições em fórmulas |
| M.O.I | Mão de Obra (indireta) | ALTA | MO elétrica indireta |
| M.O.D. Elétrica | Mão de Obra (direta) | ALTA | MO direta elétrica |
| TAB HH | Referência | MEDIA | Tabela de HH |
| Pintura | Composições (implícitas) | BAIXA | Cálculo de área e pintura |
| Mobilização | Referência | BAIXA | Custos de mobilização |
| Desmobilização | Referência | BAIXA | Custos de desmobilização |
| Seguros e Outros | Encargos/BDI | BAIXA | Seguros |
| Custo Obra_Industrial | Referência | BAIXA | Resumo geral — não extrair, só referência |

### Abas ignoradas (operacionais, não extraem):
Formula Reajuste Cabos, Plan1, LEVANTAMENTO, Administração Central IND, RESUMO PREÇOS Industrial, Paineis (2), histograma, Custos MOI, Cronograma de desembolso, Cronograma macro, PROJETOS, Manutenção de Canteiro, Prog. segurança e exames, DESPESAS VIAGENS GERENCIAIS.

### Ordem de extração recomendada:
1. Base de Materiais → Insumos (fundação — tudo referencia isso)
2. Tabela de Entrada de Preços + M.O.I + M.O.D. → Mão de Obra
3. Encargos + Impostos → Encargos/BDI
4. Equipamentos + Cálculo Custo Equipamentos + EPI → Equipamentos
5. COMPOSIÇÃO Hh → Composições MO
6. Materiais - industrial + Alimentação → Composições implícitas (fórmulas)
7. BASE DADOS PAINEIS → Insumos Siemens (volume grande, prioridade média)

## Nota Crítica: Composições Paramétricas (Alimentação-industrial → Materiais)

A aba "Materiais - industrial" NÃO é fonte primária — é resultado de cálculos. Os dados vêm da aba "Alimentação-industrial" via fórmulas.

### Fluxo real:
1. **Alimentação-industrial**: Usuário insere motores (potência, distância, circuito)
2. **Cálculo automático**: Fórmulas determinam infraestrutura necessária (cabo, eletroduto, conectores, quantidades)
3. **Materiais - industrial**: Consolida quantitativos + materiais adicionais manuais

### Como extrair:
**Da aba Materiais - industrial** → Extrair apenas CATÁLOGO (código, descrição, unidade, fornecimento) para tabela Insumos. NÃO extrair quantidades — são específicas de um orçamento, não são dados de referência.

**Da aba Alimentação-industrial** → Esta é a composição paramétrica real. Extrair:
- Estrutura de inputs (motor, potência, distância)
- Lógica das fórmulas que calculam infra (qual cabo para qual potência, qual eletroduto para qual seção de cabo)
- Documentar como Composição tipo PARAMETRICA com _formula_original

### CUIDADO com ajustes manuais:
Fórmulas podem ter sido adulteradas (ex: `=ARREDONDAR.PARA.CIMA('Alimentação-industrial'!CV77;0)+280`). O "+280" é ajuste manual que alguém colocou por cima. Sempre registrar na coluna _observacao quando detectar ajustes manuais sobre fórmulas.

### Prioridade: 
Extrair catálogo de itens = ALTA (fácil, direto)
Extrair composições paramétricas = ALTA mas COMPLEXA (requer engenharia reversa das fórmulas da Alimentação-industrial)


## Fontes de Dados — Nomes e Conteúdo

### FONTE 1: HOLLOS (`PLANILHA ORCAMENTOS - HOLLOS.xlsx`)
Planilha operacional da Concept (a que usam no dia a dia). 35 abas, 5.1 MB.

**Abas ALTA prioridade (dados extraíveis):**
- Base de Materiais → 2.771 insumos com preço, HH, família. FUNDAÇÃO.
- Tabela de Entrada de Preços → 41 funções MO (CLT/PJ, salário, periculosidade, dissídio 2020)
- M.O.I → MO indireta (10 funções gestão, HH normal/extra, alimentação/transporte)
- M.O.D. Elétrica → MO direta (10 funções operacionais, periculosidade 30%, encargos 78.7%)
- COMPOSIÇÃO Hh → Composição salarial completa por função (salário + periculosidade + encargos + alimentação + transporte + EPI + admissional + seguro). 20 funções.
- Encargos → Encargos horista detalhado (Grupo A 36.8%, B 43.2% horista/22.7% mensalista, C 10.9%, D incidência). Total: 106.7% horista, 78.7% mensalista.
- Impostos-industrial → COFINS 3%, PIS 0.65%, ICMS 18%, ISS 3%. Por regime tributário.
- Equipamentos + Cálculo Custo Equipamentos + EPI → 78 itens com depreciação e custo/hora
- BASE DADOS PAINEIS → 30.552 itens Siemens (lista preços Jan/2019, defasado)

**Abas ALTA prioridade (composições implícitas — requer engenharia reversa):**
- Alimentação-industrial → CALCULADORA: motor (KW, V, distância) → cabos, eletrodutos, leitos, terminais. 9.326 fórmulas. Core paramétrico.
- Materiais - industrial → Template orçamento com multiplicadores por categoria. 10.458 fórmulas.
- Instrumentação-industrial → Calculadora: transmissores/válvulas → cabos sinal, tubing, eletrodutos
- Paineis (2) → Configurador painéis: tipo partida + potência → BOM (disjuntor, contator, relé, bornes)

**Abas parâmetros (não extraem tabela, mas são referência):**
- Horas improdutivas → Fator produtividade 0.898 (10.2% improdutivo)
- Formula Reajuste Cabos → Fórmula LME cobre × câmbio USD/BRL
- Administração Central → Composição BDI completa (ISS, PIS, COFINS, Adm 10%, Lucro 15%, IR 4.8%)
- Pintura → Coeficientes kg/m → m² (área pintura)

**Abas ignoradas:** Plan1, histograma, Custos MOI mensal, Cronogramas, PROJETOS, Manutenção Canteiro, Mobilização, Desmobilização, Custo Obra, DESPESAS VIAGENS, Prog. segurança.

### FONTE 2: MURILO (`PLANILHA ORCAMENTOS - MURILO.xlsm`)
Planilha de orçamento de concorrente maior. 39 abas, 21 MB.

**Abas ALTA prioridade (dados extraíveis):**
- (2) Base Dados → ~5.000+ insumos com família, código, descrição, unidade, HH, preço
- (6) Profissionais (Salários) → ~140 funções com salário 2025, R$/hora
- (8) Encargos Sociais → INSS 20%, FGTS 8%, 13º, férias, multa, seguro. Total ~60%
- (9) Incidências MOI → Custos adicionais sobre MOI: admissionais (exames R$500, treinamento), benefícios (VA, VT, hospedagem, EPI), custos operacionais
- (10) Composição MOI → 900 linhas. Salário + encargos + incidências A/B/C + HE + noturno + periculosidade. Custo/hora em múltiplas modalidades.
- (11) Incidências MOD → Mesma estrutura da MOI para MOD
- (12) Composição MOD → 1.200 linhas. Mesma lógica. Mais funções (soldador, montador, etc.)
- (13) Valores Custo-Venda_HH → 140 funções com custo/hora E preço venda. Markup ~1.92x
- (23) Máq. e Ferramentas → 58 itens (esmerilhadeira, oxicorte, estufas, máquinas solda, talhas)
- (24) Equipamentos → 78 itens (empilhadeiras, plataformas, guindastes, caminhões, ônibus)
- (26) Memória Cálculo PV → BDI por componente: MO, materiais, desp.oper, equip. ISS, PIS, COFINS, IRPJ, CSLL, lucro.

**Abas ALTA prioridade (composições de serviço):**
- (1) Atividades → WBS: Escopo → Disciplina → Atividade (cadastro mestre de serviços)
- (3) Plan. Quant. → Quantitativos por atividade com VLOOKUP na Base Dados
- Equipes → 1.000 atividades × 140 funções. DADO MUITO RICO — composição de equipe por tipo de serviço.

**Abas MEDIA (referência útil):**
- (20) Equipe Mobilização → Equipe + custo de mobilização
- (21) Mob. & Desm. → Containers, fretes, caminhões
- (22) Despesas Operacionais → Custos mensais contínuos
- (25) Preço Custo Total → Composição de preços completa (cliente: Demuth, obra: Pátio Madeiras LD Celulose)
- (27) Preço Venda Total → Custo × BDI

**Abas ignoradas:** Histogramas (01/02/03), Resumos HH (01/02/03), Resumos Preço Custo/Venda (01-03), Cronograma, MOI-MOD(2), Macro1, Planilha1, (5) Tab Dinâm, (4) Plan Quant Resumo.

### COMPARATIVO: ONDE CADA FONTE É MAIS RICA

| Tipo de dado | HOLLOS (Pequenas Obras) | MURILO (FAZZER) |
|---|---|---|
| Insumos/Materiais | 2.771 + 30k Siemens | ~5.000 |
| MO (funções) | 41 | 140 ✅ |
| Composição MO | 20 funções | 900+1.200 ✅ |
| Incidências MO | Não tem separado | MOI+MOD detalhadas ✅ |
| Encargos | 44 itens detalhado ✅ | 19 itens resumido |
| Equipamentos | 78 com depreciação ✅ | 136 com locação ✅ |
| BDI/Memorial | Adm Central + Impostos | Memorial completo ✅ |
| Composições paramétricas | Alimentação-industrial ✅ (9.326 fórmulas) | Não tem |
| Equipes por atividade | Não tem | 1.000 ativ × 140 funções ✅ |
| Siemens | 30k itens ✅ | Não tem |

São COMPLEMENTARES, não duplicatas. Na consolidação, MURILO provavelmente vence em MO/composições, HOLLOS vence em materiais/paramétricos.
