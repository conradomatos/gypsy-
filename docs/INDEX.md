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
> `projeto-executivo/cigana/01_arquitetura/registro_de_decisoes.md` e a pasta
> `01_arquitetura/_historico/`.

> **Governança (2026-07-20):** instruções de trabalho para agentes de IA são canônicas em
> **`AGENTS.md`** (raiz + `destilacao/`); `CLAUDE.md` importa via `@AGENTS.md`; regras
> granulares em `.claude/rules/`. Estrutura de código DECIDIDA: monorepo `apps/{engine,
> backend,frontend}` + `infra/` (pasta só no scaffold).

---

## Estrutura de pastas

| Pasta | Status | Conteúdo |
|-------|--------|----------|
| `projeto-executivo/cigana/` | **VIGENTE** — source of truth | Arquitetura, padrões, módulos, motores, parâmetros, telas, pipeline |
| `projeto-executivo/cigana/01_arquitetura/_historico/` | **HISTÓRICO** — não orienta implementação | Versões revogadas (React/Supabase) preservadas para auditoria |
| `pre-projeto/gate-apresentacao/` | **VIGENTE** — referência de negócio | Mapa de 37 abas HOLLOS → componentes Gypsy, problema, objetivo, personas |
| `pre-projeto/gate-destilacao/` | **VIGENTE** — data engineering | Spec 0, fontes de dados, referências de mercado |
| `pre-projeto/monte-carlo/` | **REFERÊNCIA** — conceitual | Estimativa paramétrica, casos, fases |
| `pre-projeto/_arquivo/` (doc-1, doc-2) | **ARQUIVADO** — não usar como spec | Charter, market research, schema antigo. Contraditórios com o Projeto Executivo; úteis só como histórico de visão. Mantêm o branding antigo "CostAI" por serem históricos |

## Documento autoritativo por assunto

| Assunto | Documento vigente | NÃO usar como fonte |
|---------|-------------------|---------------------|
| Stack técnica | `cigana/01_arquitetura/stack_tecnica.md` | `_historico/stack_tecnica.react-supabase.2026-04-04.md`; `_arquivo/doc-1/4_arquitetura_tecnica.md` |
| Toolchain | `cigana/01_arquitetura/toolchain.md` | `_historico/toolchain.supabase.2026-04-04.md` |
| Deploy | `cigana/01_arquitetura/deploy_pipeline.md` | `_historico/deploy_pipeline.supabase.2026-04-04.md` |
| Padrões de código | `cigana/01_arquitetura/padroes_de_codigo.md` | `_historico/padroes_de_codigo.supabase.2026-04-04.md` |
| Nomenclatura | `cigana/01_arquitetura/convencoes_nomenclatura.md` | — |
| Módulos e navegação | `cigana/01_arquitetura/modulos_e_navegacao.md` | `_arquivo/doc-1/5_roadmap` |
| Pipeline de execução | `cigana/01_arquitetura/pipeline_de_execucao.md` | `_arquivo/doc-1/5_roadmap` |
| Subprojetos | `cigana/00_SUBPROJETOS.md` | — |
| Governança / instruções de agentes | `AGENTS.md` (raiz) + `destilacao/AGENTS.md` | — |
| Revisão adversarial + CI (PROPOSTO) | `cigana/01_arquitetura/revisao_e_ci.md` | — |
| Mapa de abas → módulos | `pre-projeto/gate-apresentacao/bloco-001/discussao_modulos_planilha_hollos.md` | — |
| BDI / Formação de preço | `cigana/05_motores-de-calculo/MC-002_bdi_markup.md` | `_arquivo/doc-1/3_catalogo` |
| **Schema do banco** | **PENDENTE — ver nota abaixo** | qualquer schema antigo (doc-2, BD-1..BD-6 são preliminares, não aprovados) |

> **Modelo de dados ainda não aprovado. Será definido no subprojeto responsável pelo
> banco de dados, após validação das telas e regras de negócio.**

## Decisões de nomenclatura

- **Inglês 100%** para código (Python e TypeScript), banco de dados e API.
- **Português** para interface e documentação em `docs/`.
- **Nome do produto:** Gypsy (não "CostAI" — branding antigo, só em docs arquivados/histórico).
- Detalhe em `cigana/01_arquitetura/convencoes_nomenclatura.md`.

## Pendências documentais

- [x] ~~Mover `doc-1` e `doc-2` para `_arquivo/`~~ ✅ movidos (2026-07-19)
- [x] ~~`.claude/rules/` finalizadas~~ ✅ 8 rules gravadas (2026-07-19)
- [x] ~~`CLAUDE.md` da raiz~~ ✅ escrito (2026-07-19)
- [ ] Converter as specs `02_banco-de-dados/BD-1..BD-6` para nomenclatura inglesa quando o
      schema for desenhado no SP-04 (ou deletar). **BD-4 não existe** (a sequência tem
      BD-1, 2, 3, 5, 6) — decidir no SP-04 se o número será usado ou a lacuna documentada.
- [ ] **Dívidas de migração** (RLS, auth Supabase, Edge Functions) nos docs de `02_BANCO` e
      `04_modulos` — correção pertence aos SP-04/05/07 no gate de cada um. Lista completa em
      `cigana/01_arquitetura/pendencias_arquitetura.md` › "Pendências de migração por subprojeto".

> **Wikilinks Obsidian** (`[[MOC_...]]`) apontavam para o vault externo (gypsy-vault) e
> não resolvem neste repo — removidos desta versão do índice.
