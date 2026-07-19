# SPEC 1 — Dimensionador de Alimentadores Elétricos
# Módulo CostAI: Electrical Feeder Sizing & BOM Generator

## 1. O que existe hoje (planilha HOLLOS, aba Alimentação-industrial)

A aba é uma calculadora em Excel com 9.326 fórmulas. O usuário insere dados de cada motor/carga e a planilha gera automaticamente a infraestrutura elétrica necessária.

### Inputs do usuário (por alimentador):
- Descrição do circuito (ex: "ELE 306", "TC 201")
- Tipo de partida (Direta, Estrela-Triângulo, Soft-Starter, Inversor)
- Potência (KW)
- Tensão (V) — 380V, 220V, etc.
- Distância (metros) — do quadro ao motor
- Fatores de correção: Agrupamento (0.65), Temperatura 40°C EPR (0.91), Potência (0.92), Queda de tensão (4.00%)

### Outputs calculados (por alimentador):
- Corrente nominal (A)
- Seção do cabo (mm²) — cabos de potência
- Tipo de cabo (tetrapolar, tripolar, unipolar, MT)
- Quantidade de cabos
- Seção do eletroduto ou leito
- Quantidade de eletrodutos
- Terminais necessários
- Cabos auxiliares (gerador, pulso, resistência, aquecimento, comando, temp, PT100)
- Cabos Força: bitola(ic), bitola(Q.T.), bitola adotado

### Fórmulas-chave embutidas:
- I = P / (√3 × V × cos φ × η) — corrente nominal
- Seção = (√3 × L × I × ρ) / (Vd% × V) — dimensionamento por queda de tensão
- Fatores de correção: agrupamento × temperatura × potência
- Seleção de cabo: maior entre dimensionamento por ampacidade e por queda de tensão
- Seleção de eletroduto: baseado na seção total dos cabos (taxa de ocupação NBR 5410)

### Limitações da planilha atual:
- Rígida: se precisa de mais alimentadores, copia linhas e reza pra não quebrar fórmulas
- Sem validação: aceita qualquer dado sem verificar consistência
- Sem histórico: cada orçamento recomeça do zero
- Sem reuso: não puxa de orçamentos anteriores
- Tabelas de cabo/eletroduto embutidas nas fórmulas (difícil atualizar)
- Layout fixo: duas colunas lado a lado (motores "BT" lado esquerdo, lado direito)


## 2. Como o mercado faz (benchmarks)

### Softwares de dimensionamento elétrico industrial:

**ETAP (Operation Technology, Inc.)**
- Software enterprise para projeto e análise de sistemas elétricos
- Módulo Load Analyzer: load list → cable sizing → panel schedule → one-line diagram
- Fluxo: lista de cargas → cálculo de potência por barramento → dimensionamento de alimentadores → estudos de curto-circuito
- Preço: enterprise (dezenas de milhares de USD)
- Referência: padrão da indústria em plantas industriais grandes

**EPLAN Electric P8 + Cable proD**
- Projeto elétrico com 2.2 milhões de componentes no Data Portal
- Cable proD: roteamento 3D de cabos com cálculo automático de comprimentos
- Macros de circuitos reutilizáveis (motor starter, star-delta, DOL)
- Variantes: muda a potência do motor e todos os componentes associados se ajustam automaticamente
- Preço: licença anual (milhares de EUR)

**Aeries CARS (Cable Automatic Routing System)**
- Especializado em plantas industriais
- LoadMatic: load scheduling → automatic panel schedules → one-line diagrams
- CableMatic: cable routing automático com verificação de fill ratio e separação por classe de tensão
- TrayMatic: modelagem 3D de eletrocalhas com BOM automática
- Foco: pré-construção e estimativa, não só projeto

**Design Master (ElectroBIM para Revit)**
- Add-in do Revit para dimensionamento de alimentadores
- Sizing automático baseado na proteção do equipamento
- Integrado ao modelo BIM

**Calculadoras web/planilhas (mercado baixo):**
- FeederCalc.com: calculadora NEC gratuita (corrente → seção → conduit)
- Construction Monkey: feeder calculator online
- EEP (Electrical Engineering Portal): dezenas de planilhas Excel para cable sizing, voltage drop
- ElectriCalc Pro: app móvel ($25) com NEC embutido

### Padrão da indústria (fluxo ideal):
1. **Load List** — lista de todas as cargas elétricas com potência, tensão, FP, eficiência, tipo de partida
2. **Load Schedule** — agrega cargas por barramento/quadro, aplica fatores de demanda e diversidade
3. **Cable Schedule** — para cada alimentador: seção, tipo, comprimento, conduit, queda de tensão
4. **BOM** — lista de materiais consolidada: cabos (metros), eletrodutos (metros), terminais (unidades), acessórios
5. **Cost Estimate** — BOM × preços unitários = custo de materiais + HH de instalação

### O que nenhum deles faz bem (gap de mercado):
- ETAP/EPLAN são de projeto, não de orçamento — não geram custo
- Calculadoras web são unitárias (1 alimentador por vez), não batch
- Planilhas Excel fazem o batch mas são frágeis e sem validação
- Ninguém integra dimensionamento + custo + composição de MO numa ferramenta só


## 3. Como deveria funcionar no CostAI (visão de produto)

### Conceito: Load List → Cable Schedule → BOM → Custo (em um fluxo)

O módulo não é uma calculadora de 1 alimentador — é um gerador de BOM completo a partir de uma lista de cargas. O usuário insere a load list (ou importa de um PDF/Excel do cliente), e o sistema gera toda a infraestrutura com custo.

### Fluxo proposto:

**Etapa 1: Load List (input)**
- Importar lista de cargas de Excel/PDF do cliente (IA pode ajudar a parsear)
- Ou inserir manualmente: TAG, descrição, tipo partida, KW, V, distância, localização
- Validação em tempo real: potência vs. tensão faz sentido? Distância plausível?

**Etapa 2: Dimensionamento automático (engine)**
- Para cada carga: calcular corrente → seção de cabo → eletroduto → acessórios
- Normas: NBR 5410, NBR 14039 (MT), NEC (quando aplicável)
- Fatores de correção parametrizáveis: temperatura, agrupamento, queda de tensão admissível
- Tabelas de referência configuráveis (fabricantes diferentes = bitolas diferentes)
- Output: Cable Schedule completo

**Etapa 3: BOM (geração automática)**
- Consolidar todos os alimentadores em lista de materiais:
  - Cabos por seção e tipo (m) — com fator de sobra parametrizável (5%, 10%)
  - Eletrodutos por bitola (m)
  - Terminais por tipo (un)
  - Conexões, abraçadeiras, suportes (composição automática)
- Vincular cada item ao catálogo de insumos do CostAI (com preço e HH)

**Etapa 4: Custo (integração com motor CostAI)**
- BOM × preço unitário = custo de materiais
- BOM × HH unitário × custo/hora MO = custo de mão de obra
- Aplicar fatores de ajuste (regional, produtividade, escala)
- Aplicar BDI
- Resultado: custo do sistema de alimentadores com faixa min/provável/máx

### Diferenciais vs. planilha atual:
- Lista de cargas dinâmica (adiciona/remove sem quebrar)
- Validação em tempo real (alerta se bitola parecer errada)
- Histórico: reusa load lists de obras anteriores
- Composições automáticas: dimensionamento → BOM → custo em um clique
- Exporta Cable Schedule em formato padrão (Excel)
- Integrado ao motor de custo (fatores + Monte Carlo)

### Diferenciais vs. mercado:
- ETAP/EPLAN dimensionam mas não orçam
- CostAI dimensiona E orça no mesmo fluxo
- Pensado para orçamentista (não para projetista) — foco em custo, não em projeto executivo
- Composições de MO integradas (não só material)


## 4. Normas e referências técnicas

- **NBR 5410:2004** — Instalações elétricas de baixa tensão (dimensionamento de condutores, proteção, queda de tensão)
- **NBR 14039:2005** — Instalações elétricas de média tensão
- **NEC (National Electrical Code)** — Art. 210, 215, 220, 310 (feeder sizing, conductor ampacities)
- **IEC 60364** — Instalações elétricas de edifícios (internacional)
- **NBR 5419** — Proteção contra descargas atmosféricas (SPDA)
- **Tabelas de fabricantes**: Prysmian, Nexans, Conduspar (cabos); Tigre, Tramontina (eletrodutos)

## 5. Dados necessários (pré-requisito para o módulo)

### Do catálogo de insumos CostAI:
- Tabela de cabos: seção (mm²), tipo (EPR, PVC, XLPE), tensão, preço/m, HH/m
- Tabela de eletrodutos: bitola, tipo (GF, PVC, metálico flexível), preço/m, HH/m
- Tabela de terminais: tipo, seção compatível, preço/un, HH/un
- Tabela de acessórios: curvas, luvas, abraçadeiras, buchas por tipo de eletroduto

### Tabelas de engenharia (embutidas no motor de cálculo):
- Ampacidade por seção/tipo de cabo/método de instalação (NBR 5410 Tab. 36-39)
- Fatores de correção de temperatura (NBR 5410 Tab. 40)
- Fatores de agrupamento (NBR 5410 Tab. 42)
- Taxa de ocupação máxima de eletrodutos (NBR 5410 Tab. 47)
- Queda de tensão admissível por tipo de circuito

## 6. Questões em aberto (para resolver com Guilherme/Sandro)

- [ ] As tabelas de ampacidade da planilha atual estão em conformidade com NBR 5410 vigente?
- [ ] Quais fabricantes de cabo a Concept usa? (Prysmian? Nexans? Afeta bitolas disponíveis)
- [ ] O fator de agrupamento 0.65 é padrão ou muda por obra?
- [ ] Queda de tensão admissível: 4% é padrão Concept ou varia por cliente?
- [ ] A planilha atual cobre MT (média tensão) ou só BT?
- [ ] Quantos alimentadores tem um orçamento típico? 20? 50? 200?
- [ ] O cliente já manda load list estruturada ou a Concept monta do edital?

## 7. Prioridade e dependências

**Prioridade:** ALTA — é a funcionalidade que mais diferencia o CostAI de uma planilha
**Dependência:** Catálogo de insumos (cabos, eletrodutos, terminais) precisa estar extraído e normalizado antes
**Fase no roadmap:** Pós-MVP (o MVP valida o motor de custo com composições manuais; o dimensionador entra na fase 2)
**Estimativa de esforço:** Módulo complexo — 3-4 sprints dedicadas (6-8 semanas)

## 8. Riscos

- Engenharia reversa das fórmulas da planilha pode revelar erros acumulados ao longo dos anos
- Tabelas de ampacidade podem estar desatualizadas (NBR 5410 tem revisões)
- Complexidade de normas (NBR 5410 é densa) — precisa de validação de engenheiro eletricista
- Risco de overengineering: projetar um ETAP quando o usuário precisa de uma calculadora de orçamento


## 9. Ajustes pós-briefing (decisões do Conrado)

### DECISÃO: Não usar dados/fórmulas da planilha HOLLOS
- As tabelas de ampacidade, fatores e fórmulas da aba Alimentação-industrial NÃO serão reaproveitadas
- O CostAI terá suas próprias tabelas, baseadas diretamente nas normas (NBR 5410, NBR 14039)
- Motivo: as fórmulas da planilha podem ter erros acumulados e tabelas desatualizadas

### DECISÃO: Não é software de projeto, é ferramenta de orçamento
- O dimensionamento aqui é RÁPIDO, para fins de orçamentação (~15% de precisão)
- O projeto executivo será recalculado depois por software de projeto (EPLAN, AutoCAD, etc.)
- Foco: gerar BOM com custo, não prancha de projeto

### FUNCIONALIDADES que faltam na planilha e devem entrar no CostAI:
- Definir trechos/roteamento dos cabos (de onde até onde passam)
- Associar cargas a painéis (qual motor em qual painel)
- Dimensionar alimentadores de painel (não só circuitos individuais)
- Dimensionar iluminação (que hoje nem existe na planilha)
- Infra de iluminação (eletrodutos, caixas, fiação)

### STATUS: Briefing em andamento
Este briefing está incompleto. As funcionalidades acima expandem o escopo significativamente.
O módulo de dimensionamento é praticamente um produto separado dentro do CostAI.
Próximos passos: continuar detalhamento em sessão futura.
