---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, subprojetos]
---

# Subprojetos — Gypsy

> Decisão 2026-07-19: o trabalho é fatiado em subprojetos que espelham 1:1 a árvore
> de documentação. Cada subprojeto roda um ciclo superpowers completo (brainstorming →
> spec → plan → execução → review) e fecha com gate de validação humana. Um subprojeto
> por vez, contexto limpo (`/clear` ao trocar).

## Mapa de subprojetos

| SP | Nome | Pasta (docs ou raiz) | Entregável | Gate |
|----|------|---------------------|------------|------|
| SP-00 | **Destilação** | `destilacao/` (raiz do repo) | Tabelas consolidadas (Insumos, MO, Equipamentos, Composições, Encargos) → seed | MASTER validado Conrado/Sandro |
| SP-01 | **Arquitetura** | `01_ARQUITETURA/` | Decisões, pipeline, regras, CLAUDE.md | revisão Conrado (contínuo) |
| SP-02 | **Telas** | `06_TELAS/` + `mockups/` | Spec + mockup HTML das 8 áreas de navegação | navegação validada Sandro/Guilherme |
| SP-03 | **Parâmetros** | `03_PARAMETROS/` (B1 projeto, B2 globais) | Camada de parâmetros: globais + override por orçamento | spec fechada + modelos |
| SP-04 | **Banco de Dados** | `02_BANCO DE DADOS/` (BD-1..BD-6) | Modelos Django + migrations + Admin + seed | banco populado, navegável |
| SP-05 | **C1 — Módulos Funcionais** | `04_MODULOS/C1/` | M-000 Cadastro · M-001 Dimensionador · M-002 Estimativa · M-003 Base de custos | testes verdes por módulo |
| SP-06 | **C2 — Módulos Transversais** | `04_MODULOS/C2/` | M-004 Custos operacionais · M-005 Estimador de equipe | testes verdes por módulo |
| SP-07 | **C3 — Módulo Saída** | `04_MODULOS/C3/` | M-006 Resumo · Monte Carlo · Proposta · Dashboards · IA · Auditoria | golden test completo (R$ 216.188,04) |
| SP-08 | **MC-001 Composição HH** | `05_MOTORES DE CALCULO/MC-001/` | Engine custo/hora por função (encargos, alimentação, adicionais) | teste × HOLLOS |
| SP-09 | **MC-002 BDI/Markup** | `05_MOTORES DE CALCULO/` | Engine formação de preço de venda | teste × HOLLOS |
| SP-10 | **MC-003 Reajuste Commodities** | `05_MOTORES DE CALCULO/` | Engine reajuste cabos (LME cobre × câmbio) | pós-MVP |

## Ordem de execução

A ordem vem do pipeline (`pipeline_de_execucao.md`), não da numeração:

```
SP-01 Arquitetura (fase 0, contínuo)
SP-02 Telas (fase 1 — em curso a seguir)
SP-03 Parâmetros + SP-04 Banco (fase 2)    ← SP-00 Destilação alimenta o seed
SP-08 MC-001 → SP-06 (M-005) → SP-09 MC-002 → SP-05 (M-001.1) → SP-06 (M-004) → SP-07 (M-006.1)   (fase 3)
SP-07 golden test completo (fase 4)
SP-10 MC-003 + resto do SP-07 (fase 5, pós-MVP)
```

SP-00 Destilação roda em trilha paralela — não bloqueia SP-01..SP-03.

## Status

| SP | Status |
|----|--------|
| SP-00 | Em andamento — HOLLOS extraída parcialmente, MURILO na fila |
| SP-01 | Fundação documental concluída (docs vigentes, 8 rules, CLAUDE.md) — aguardando gate final do Conrado |
| SP-02..SP-10 | Não iniciados |
