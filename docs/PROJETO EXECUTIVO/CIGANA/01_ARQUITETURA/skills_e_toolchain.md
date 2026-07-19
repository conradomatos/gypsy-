---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Skills, agents e toolchain — Gypsy

> Decisão 2026-07-19: **reusar skills e agents existentes, não criar novos.**
> Skill de projeto só nasce quando não existir nada pronto E a fase que precisa chegar.
> O processo (quando usar o quê) está em `pipeline_de_execucao.md` — este doc é o inventário.

## Skills — processo (superpowers, espinha dorsal)

| Skill | Uso |
|---|---|
| `superpowers:brainstorming` | Antes de qualquer trabalho criativo: spec de tela, design de módulo |
| `superpowers:writing-plans` | Plano de implementação a partir de spec aprovada |
| `superpowers:executing-plans` | Execução com checkpoints de review |
| `superpowers:subagent-driven-development` | Tarefas independentes em paralelo |
| `superpowers:test-driven-development` | Todo engine — teste antes do código |
| `superpowers:systematic-debugging` | Todo bug — causa raiz, não band-aid |
| `superpowers:requesting-code-review` | Antes de merge |
| `superpowers:verification-before-completion` | Evidência antes de dizer "pronto" |
| `superpowers:finishing-a-development-branch` | Merge/PR/cleanup |

## Skills — implementação

| Necessidade | Skill | Origem | Fase |
|---|---|---|---|
| Direção visual dos mockups | `frontend-design` | plugin oficial | 1 |
| Gráficos/dashboards (Monte Carlo, resumo) | `dataviz` | global | 1, 5 |
| Manipular planilhas (dados fake, seed) | `xlsx` | ai_fabric skills-main | 1, 2 |
| Commits e PRs | `commit-commands` | plugin oficial | todas |
| Extração das fontes (destilação) | `extrair-fonte` | `../01_DESTILACAO/.claude/skills/` | paralela |

## Agents

| Agent | Uso |
|---|---|
| `planner` | Plano de implementação antes de código (par do writing-plans) |
| `reviewer` | Review antes de merge — bugs reais, performance, segurança |
| `debugger` | Causa raiz de bugs (reproduz, isola, traça, diagnostica) |
| `Explore` | Buscas amplas em código/docs sem poluir o contexto da sessão |
| `feature-dev:code-architect` | Blueprint de arquitetura de feature nova |
| `feature-dev:code-explorer` | Mapear código existente antes de mexer |
| `feature-dev:code-reviewer` | Segundo revisor quando a mudança for crítica (engines) |

## Skills de projeto a criar (futuro, quando a fase chegar)

| Skill | Cria quando | O que fará |
|---|---|---|
| `seed-dados` | início Fase 2 | Importa EXTRACAO_*.xlsx → banco, valida schema, relatório de carga |
| `golden-test` | início Fase 3 | Roda orçamento de referência × HOLLOS (R$ 216.188,04), diff item a item |

## Padrão visual dos mockups (substitui skill própria)

Documentado uma vez em `mockups/PADRAO.md` quando o primeiro mockup for aprovado:
header/nav comum, tipografia, paleta, componentes (tabela, formulário, card).
Todo mockup seguinte referencia o padrão.

## Referências de repo maduro

- **PWC** (`01-POWER_CONCEPT`): `.claude/rules/` granular, agents revisores próprios — copiar o formato quando o código crescer.
- **CONCILIADOR** (`08 - CONCILIADOR`): estrutura `docs/`, mockups HTML, engine separado do Django.
- **ALMOX** (`07 - ALMOX`): ordem de construção Django-first (modelos → Admin → DRF → frontend → seed → validação).

> `toolchain.md` (dbdiagram/Vitest/Sentry/Supabase CLI) é da era React/Supabase —
> REVOGADO em 2026-07-19; toolchain Django será definida no CLAUDE.md do repo.
