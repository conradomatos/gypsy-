---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Itens pendentes de definição — Arquitetura Gypsy

## 1. Schema do banco (modelo de dados)

Status: PENDENTE — definir quando detalhar cada módulo individualmente.

Tabelas core necessárias (lista preliminar):

### Orçamento
- `orcamentos` — metadados (cliente, obra, local, tipo, prazo, revisão)
- `parametros_projeto` — override dos globais por orçamento

### Dimensionador (M-001)
- `motores` — dados de placa (potência, tensão, corrente, FP, partida)
- `trechos` — rota, distância, tipo infra
- `motores_trecho` — N:N motor × trecho
- `resultados_dimensionamento` — bitola, eletroduto, terminações calculadas

### Motor de estimativa (M-002)
- `wbs_nos` — hierarquia da WBS (área/local/prédio)
- `assemblies` — composições parametrizáveis
- `itens_assembly` — materiais + MO + equipamento de cada assembly
- `itens_orcamento` — itens lançados (do dimensionador + manuais)

### Base de custos (M-003)
- `ref_insumos` — catálogo mestre de materiais
- `ref_precos` — preços por fonte/fornecedor/data
- `ref_funcoes` — funções com salário base
- `ref_encargos` — alíquotas por grupo (A/B/C/D) por perfil
- `ref_equipamentos` — catálogo com custo/dia

### Custos operacionais (M-004)
- `custos_mob_desmob` — equipe × dias × custo
- `custos_canteiro` — itens × dias
- `custos_equipamentos_obra` — equipamentos × dias
- `custos_seguros` — tipo × valor
- `custos_seguranca` — exames × efetivo
- `custos_engenharia` — Hxh × custo
- `custos_despesas_gerenciais` — itens × quantidade

### Parâmetros globais
- `parametros_globais` — chave/valor com tipo
- `perfis_encargos` — templates por regime tributário
- `ref_impostos` — alíquotas por UF

## 2. CLAUDE.md do CostAI

Status: PENDENTE — escrever quando iniciar o repo. Deve conter:
- Stack (referência ao doc stack_tecnica.md)
- Padrões (referência ao doc padroes_de_codigo.md)
- Convenções (referência ao doc convencoes_nomenclatura.md)
- Anti-patterns (lista do que NÃO fazer)
- Regras invioláveis (engines puros, testes obrigatórios, golden test)
- Módulos e navegação (referência ao doc)
- Deploy (referência ao doc)

## 3. Schema de tipos TypeScript

Status: PENDENTE — definir junto com o schema do banco. 
Arquivo: `src/types/` — um arquivo por domínio.

## 4. Tabelas de NBRs e características de fabricantes

Status: DECIDIDO (2026-04-07)

- **Tabelas de NBR (5410, 5419, etc.):** `src/data/` como constantes TypeScript exportadas. São tabelas estáticas de referência normativa (capacidade de corrente por bitola, fator de agrupamento, queda de tensão). Não vão no banco porque não mudam por tenant nem por orçamento — mudam só quando a norma é revisada.
- **Características de fabricantes (catálogo Siemens, WEG, etc.):** Banco de dados via `materials` + `material_prices` + `pricebooks`. São dados dinâmicos com preço, data-base, e fornecedor. Entram via importação (Excel/BC3) e ficam no Supabase.

Estrutura `src/data/`:
```
src/data/
├── nbr5410/
│   ├── current-capacity.ts      (tabelas de capacidade de corrente)
│   ├── voltage-drop.ts          (fatores de queda de tensão)
│   ├── grouping-factors.ts      (fatores de agrupamento)
│   └── conduit-fill.ts          (taxa de enchimento)
├── nbr5419/
│   └── spda.ts                  (tabelas SPDA)
└── index.ts                     (re-exports)
```