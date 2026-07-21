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
01_arquitetura/     — Stack, padrões, pipeline, decisões, convenções
02_banco-de-dados/  — Specs por domínio (schema ainda NÃO aprovado — ver abaixo)
03_parametros/      — Parâmetros globais (empresa) e de projeto (orçamento)
04_modulos/         — Specs funcionais por módulo (C1 funcionais, C2 transversais, C3 saída)
05_motores-de-calculo/ — MC-001 Composição HH, MC-002 BDI, MC-003 Reajuste
```

## Índice autoritativo

O índice de "qual documento é fonte de verdade por assunto" é **`docs/INDEX.md`**.
Consulte-o antes de assumir qualquer documento como vigente.

## Source of truth

- **Índice geral:** `../../INDEX.md` (documento autoritativo por assunto)
- **Decisões:** `01_arquitetura/registro_de_decisoes.md`
- **Pipeline:** `01_arquitetura/pipeline_de_execucao.md`
- **Mapa 37 abas → módulos:** `../../pre-projeto/gate-apresentacao/bloco-001/discussao_modulos_planilha_hollos.md`

> **Modelo de dados ainda não aprovado.** Não há schema vigente (o antigo
> `costai_schema.dbml` não existe/foi descartado). O schema será definido no
> **subprojeto responsável pelo banco de dados (SP-04)**, após validação das telas e das
> regras de negócio. As specs em `02_banco-de-dados/` são preliminares, não schema aprovado.

## Golden test

Planilha HOLLOS (Pequenas Obras): **R$ 216.188,04** — benchmark de validação.
O Gypsy com os mesmos inputs deve reproduzir este valor.
