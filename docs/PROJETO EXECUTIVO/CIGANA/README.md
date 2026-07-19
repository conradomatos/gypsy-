---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy]
---

# Gypsy — Projeto Executivo

Motor de cost intelligence para orçamentação de montagem elétrica industrial.
Substitui Arquimedes + planilhas Excel + calculadora NBR 5410 por plataforma única.

## Estrutura

```
01_ARQUITETURA/     — Stack, padrões, pipeline, decisões, convenções
02_BANCO DE DADOS/  — Schema DBML (source of truth), specs por domínio
03_PARAMETROS/      — Parâmetros globais (empresa) e de projeto (orçamento)
04_MODULOS/         — Specs funcionais por módulo (C1 funcionais, C2 transversais, C3 saída)
05_MOTORES DE CALCULO/ — MC-001 Composição HH, MC-002 BDI, MC-003 Reajuste
```

## Source of truth

- **Schema:** `02_BANCO DE DADOS/costai_schema.dbml` (inglês, DBML)
- **Decisões:** `01_ARQUITETURA/registro_de_decisoes.md`
- **Pipeline:** `01_ARQUITETURA/pipeline_de_execucao.md`
- **Mapa 37 abas → módulos:** `../../PRE PROJETO/GATE_APRESENTACAO/BLOCO_001/discussao_modulos_planilha_hollos.md`

## Golden test

Planilha HOLLOS (Pequenas Obras): **R$ 216.188,04** — benchmark de validação.
O Gypsy com os mesmos inputs deve reproduzir este valor.
