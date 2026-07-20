---
tipo: projeto
status: ativo
area: gypsy
tags: [gypsy, visao-geral]
criado: 2026-04-07
revisado: 2026-07-19
---

# GYPSY — Índice da Documentação

**Produto:** Gypsy (motor de cost intelligence para montagem elétrica industrial)
**Jira:** IP101 | **Repo:** github.com/conradomatos/gypsy-
**Empresa:** Concept Engenharia
**Última revisão:** 2026-07-19

> **Arquitetura vigente:** frontend React + TypeScript + Vite + Tailwind + shadcn/ui;
> backend Django + DRF + PostgreSQL; engine Python puro isolado; integração REST.
> A stack anterior (React + Supabase) foi **revogada em 2026-07-19** — ver
> `PROJETO EXECUTIVO/CIGANA/01_ARQUITETURA/registro_de_decisoes.md` e a pasta
> `01_ARQUITETURA/_HISTORICO/`.

---

## Estrutura de pastas

| Pasta | Status | Conteúdo |
|-------|--------|----------|
| `PROJETO EXECUTIVO/CIGANA/` | **VIGENTE** — source of truth | Arquitetura, padrões, módulos, motores, parâmetros, telas, pipeline |
| `PROJETO EXECUTIVO/CIGANA/01_ARQUITETURA/_HISTORICO/` | **HISTÓRICO** — não orienta implementação | Versões revogadas (React/Supabase) preservadas para auditoria |
| `PRE PROJETO/GATE_APRESENTACAO/` | **VIGENTE** — referência de negócio | Mapa de 37 abas HOLLOS → componentes Gypsy, problema, objetivo, personas |
| `PRE PROJETO/GATE DESTILACAO/` | **VIGENTE** — data engineering | Spec 0, fontes de dados, referências de mercado |
| `PRE PROJETO/MONTE CARLO/` | **REFERÊNCIA** — conceitual | Estimativa paramétrica, casos, fases |
| `PRE PROJETO/_ARQUIVO/` (DOC_1, DOC_2) | **ARQUIVADO** — não usar como spec | Charter, market research, schema antigo. Contraditórios com o Projeto Executivo; úteis só como histórico de visão. Mantêm o branding antigo "CostAI" por serem históricos |

## Documento autoritativo por assunto

| Assunto | Documento vigente | NÃO usar como fonte |
|---------|-------------------|---------------------|
| Stack técnica | `CIGANA/01_ARQUITETURA/stack_tecnica.md` | `_HISTORICO/stack_tecnica.react-supabase.2026-04-04.md`; `_ARQUIVO/DOC_1/4_arquitetura_tecnica.md` |
| Toolchain | `CIGANA/01_ARQUITETURA/toolchain.md` | `_HISTORICO/toolchain.supabase.2026-04-04.md` |
| Deploy | `CIGANA/01_ARQUITETURA/deploy_pipeline.md` | `_HISTORICO/deploy_pipeline.supabase.2026-04-04.md` |
| Padrões de código | `CIGANA/01_ARQUITETURA/padroes_de_codigo.md` | `_HISTORICO/padroes_de_codigo.supabase.2026-04-04.md` |
| Nomenclatura | `CIGANA/01_ARQUITETURA/convencoes_nomenclatura.md` | — |
| Módulos e navegação | `CIGANA/01_ARQUITETURA/modulos_e_navegacao.md` | `_ARQUIVO/DOC_1/5_roadmap` |
| Pipeline de execução | `CIGANA/01_ARQUITETURA/pipeline_de_execucao.md` | `_ARQUIVO/DOC_1/5_roadmap` |
| Subprojetos | `CIGANA/00_SUBPROJETOS.md` | — |
| Mapa de abas → módulos | `PRE PROJETO/GATE_APRESENTACAO/BLOCO_001/discussao_modulos_planilha_hollos.md` | — |
| BDI / Formação de preço | `CIGANA/05_MOTORES DE CALCULO/MC-002_bdi_markup.md` | `_ARQUIVO/DOC_1/3_catalogo` |
| **Schema do banco** | **PENDENTE — ver nota abaixo** | qualquer schema antigo (DOC_2, BD-1..BD-6 são preliminares, não aprovados) |

> **Modelo de dados ainda não aprovado. Será definido no subprojeto responsável pelo
> banco de dados, após validação das telas e regras de negócio.**

## Decisões de nomenclatura

- **Inglês 100%** para código (Python e TypeScript), banco de dados e API.
- **Português** para interface e documentação em `docs/`.
- **Nome do produto:** Gypsy (não "CostAI" — branding antigo, só em docs arquivados/histórico).
- Detalhe em `CIGANA/01_ARQUITETURA/convencoes_nomenclatura.md`.

## Pendências documentais

- [x] ~~Mover `DOC_1` e `DOC_2` para `_ARQUIVO/`~~ ✅ movidos (2026-07-19)
- [x] ~~`.claude/rules/` finalizadas~~ ✅ 8 rules gravadas (2026-07-19)
- [x] ~~`CLAUDE.md` da raiz~~ ✅ escrito (2026-07-19)
- [ ] Converter as specs `02_BANCO DE DADOS/BD-1..BD-6` para nomenclatura inglesa quando o
      schema for desenhado no SP-04 (ou deletar). **BD-4 não existe** (a sequência tem
      BD-1, 2, 3, 5, 6) — decidir no SP-04 se o número será usado ou a lacuna documentada.
- [ ] **Dívidas de migração** (RLS, auth Supabase, Edge Functions) nos docs de `02_BANCO` e
      `04_MODULOS` — correção pertence aos SP-04/05/07 no gate de cada um. Lista completa em
      `CIGANA/01_ARQUITETURA/pendencias_arquitetura.md` › "Pendências de migração por subprojeto".

> **Wikilinks Obsidian** (`[[MOC_...]]`) apontavam para o vault externo (gypsy-vault) e
> não resolvem neste repo — removidos desta versão do índice.
