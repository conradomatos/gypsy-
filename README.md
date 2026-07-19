# Gypsy — Cost Intelligence para Montagem Elétrica Industrial

Motor de orçamentação por modelagem financeira da Concept Engenharia.
Substitui as planilhas de orçamento (HOLLOS/MURILO) por um sistema com base de
custos consolidada, composições auditáveis, dimensionador elétrico e análise de risco.

**Stack:** Django + DRF, Postgres, Python via `uv` — mesmo padrão dos apps ALMOX e
CONCILIADOR. Local-first: roda local até validação; deploy depois.

**Estado atual: planejamento.** Nenhum código escrito. A documentação está sendo
migrada do vault Obsidian (gypsy-vault) para `docs/`.

## Estrutura

```
docs/
├── INDEX.md                     Índice: documento autoritativo por assunto
├── PRE PROJETO/                 Visão estratégica (charter, gates, Monte Carlo, DOCS_WORD)
└── PROJETO EXECUTIVO/CIGANA/
    ├── 01_ARQUITETURA/          Decisões, pipeline de execução, skills e agents
    ├── 02_BANCO DE DADOS/       Specs de tabela (BD-1..BD-6, orçamentos, RBAC)
    ├── 03_PARAMETROS/           Parâmetros globais (B2) + por projeto (B1)
    ├── 04_MODULOS/              M-000 Cadastro · M-001 Dimensionador · M-002 Estimativa
    │                            M-003 Base de custos · M-004 Custos operacionais
    │                            M-005 Estimador de equipe · M-006 Saída/Resultados
    ├── 05_MOTORES DE CALCULO/   MC-001 Composição HH · MC-002 BDI/Markup · MC-003 Reajuste
    └── 06_TELAS/                Specs das 8 áreas de navegação (telas primeiro)
mockups/                         HTML clicável com dados fake (valida UX antes do código)
referencias/                     Material de apoio (entrevistas, benchmarks)
destilacao/                      SP-00 — data engineering (Spec 0): extrai e normaliza
                                 as planilhas-fonte; alimenta o seed. CLAUDE.md próprio.
                                 (fontes .xlsx ficam fora do git)
.claude/rules/                   Regras do projeto (rascunho — versão final: Conrado)
.claude/skills/extrair-fonte/    Skill de extração por fonte (destilação)
```

## Subprojetos

O trabalho é fatiado em SP-00..SP-10 espelhando a árvore de docs — ver
`docs/PROJETO EXECUTIVO/CIGANA/00_SUBPROJETOS.md`.

## Marcos

| Fase | Entrega | Gate |
|------|---------|------|
| 0 | Repo + docs migrados + decisões registradas | revisão Conrado |
| 1 | Specs de telas + mockups HTML das 8 áreas | validação Sandro/Guilherme |
| 2 | Modelos Django + migrations + Admin + seed (dados da destilação) | banco populado |
| 3 | Engines por fatia vertical (MC-001 → M-005 → MC-002 → M-001.1 → M-004 → M-006.1) | testes unitários |
| 4 | Golden test completo | R$ 216.188,04 bate com a HOLLOS |
| 5 | Instrumentação, Pintura, Cotações, Monte Carlo, Proposta PDF | pós-MVP |
