# AGENTS.md — SP-00 Destilação de Dados (Gypsy)

> **Herda o `AGENTS.md` da raiz.** Aqui só o que é **local à destilação**. Regras gerais
> (git, segurança, nomenclatura, limites SEMPRE/PERGUNTAR/NUNCA) valem como na raiz e não
> se repetem. O `CLAUDE.md` desta pasta apenas importa este arquivo.

## Contexto

Fase de data engineering ("projeto antes do projeto") do Gypsy: extrair, normalizar e
consolidar dados de fontes heterogêneas (planilhas HOLLOS/MURILO) em tabelas padronizadas
que alimentarão o seed do banco.

- **Operador:** Conrado Matos (Concept Engenharia).
- **Validação de domínio:** Conrado + Sandro (orçamentista sênior).
- Planilhas-fonte em `destilacao/fontes/` são **read-only** e ficam **fora do git**.

## Regras locais de extração

1. **NUNCA modifique os arquivos-fonte.** Leia como read-only e gere novos arquivos de saída.
2. **Uma fonte por vez.** Não misture dados de fontes diferentes no mesmo passo.
3. **Sempre gere Excel (.xlsx)** como output intermediário, uma aba por tabela-destino.
4. **`_fonte`** em toda tabela (nome da planilha de origem).
5. **`_aba_origem`** (aba de origem).
6. **`_linha_origem`** (linha no arquivo fonte, para auditoria).
7. **`_confianca`** (alta/media/baixa) quando houver interpretação.
8. **`_revisar = SIM`** para qualquer dado que precise de validação humana.
9. **Normalize unidades:** PÇ/PC/pç/UN → UN | M/m/ML/ml → M | M2/m2/m² → M2 | KG/kg/Kg → KG |
   H/h/HH/Hh → H | VB/vb → VB | CJ/cj → CJ | L/l → L.
10. **Normalize texto:** UPPERCASE nas descrições; remover espaços duplos e caracteres
    especiais desnecessários.
11. **Preços em R$ sem imposto** quando possível; se incluir imposto, `_inclui_imposto = SIM`.
12. **Datas em ISO:** YYYY-MM-DD.
13. **Não invente dados.** Campo inexistente na fonte fica vazio — nunca estimar.
14. **Fórmulas Excel:** ao encontrar composição implícita, extraia a fórmula E o valor
    calculado; documente em `_formula_original`.

## Tabelas-destino (schema padrão)

Colunas de auditoria (`_fonte`, `_aba_origem`, `_linha_origem`, `_confianca`, `_revisar`)
em todas. Tabelas: **Insumos · Mão de Obra · Equipamentos · Composições · Itens da
Composição · Encargos e BDI**. Definição de colunas por tabela: ver `TEMPLATE_DOCUMENTACAO_ABAS.md`
e as specs em `destilacao/specs/`.

> Este schema de extração é o formato **intermediário** da destilação — não é o schema do
> banco (que é PENDENTE, definido no SP-04). Colunas de origem alimentam o seed.

## Workflow por fonte

1. **Diagnóstico** — ler o arquivo inteiro; por aba: contar linhas reais, mapear a
   tabela-destino, listar fórmulas; relatório usando `TEMPLATE_DOCUMENTACAO_ABAS.md`.
2. **Extração** — para cada aba mapeada, extrair no formato da tabela-destino, normalizar,
   preencher auditoria, marcar `_revisar`; salvar em `intermediarios/EXTRACAO_{fonte}.xlsx`.
3. **Relatório** — registros por tabela, marcados para revisão, campos vazios relevantes,
   anomalias (preço negativo, rendimento > 100, etc.).
4. **Validação humana** — Conrado/Sandro revisam os `_revisar = SIM` e corrigem no Excel.
5. **Consolidação** (só após todas as fontes) — juntar `EXTRACAO_*.xlsx` num MASTER por tipo;
   identificar duplicatas entre fontes.

## Fonte atual e detalhe operacional

**HOLLOS** (`PLANILHA ORCAMENTOS - HOLLOS.xlsx`, ~35 abas). Mapeamento completo de abas →
tabelas-destino, prioridades e ordem de extração estão na skill `extrair-fonte`.

**Nota crítica:** a aba "Materiais - industrial" **não** é fonte primária — resulta de
cálculos da aba "Alimentação-industrial" via fórmulas. Fluxo, extração e comparativo
HOLLOS × MURILO na skill `extrair-fonte`; spec do módulo em
`specs/SPEC1_Dimensionador_Alimentadores.md`.

## Compatibilidade Omie (ERP da Concept)

Ao normalizar, manter compatível com o template Omie (`Omie_Produtos_*.xlsx`): preservar
`codigo_fonte` único, `ncm` (obrigatório no Omie para NF-e) e EAN/GTIN quando disponíveis;
`familia` com nomenclatura próxima à do Omie. A aba Estrutura/BOM e Kits do Omie mapeiam para
**Composições + Itens da Composição**. Arquivo de referência em `fontes/`.
