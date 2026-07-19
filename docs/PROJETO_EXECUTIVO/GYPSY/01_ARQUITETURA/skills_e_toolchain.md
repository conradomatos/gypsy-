# Skills e toolchain — Gypsy

> Decisão 2026-07-19: **reusar skills existentes, não criar novas.** Skill de projeto
> só nasce quando não existir nada pronto E a fase que precisa dela chegar.

## Mapa: necessidade → skill existente

| Necessidade | Skill/ferramenta | Origem | Fase |
|---|---|---|---|
| Spec de tela antes do HTML | `superpowers:brainstorming` | plugin superpowers | 1 |
| Direção visual dos mockups | `frontend-design` | plugin oficial | 1 |
| Gráficos/dashboards (Monte Carlo, resumo) | `dataviz` | global | 1, 5 |
| Manipular planilhas (ler HOLLOS p/ dados fake, seed) | `xlsx` | ai_fabric skills-main | 1, 2 |
| TDD nos engines | `superpowers:test-driven-development` | plugin superpowers | 3 |
| Executar planos com checkpoints | `superpowers:executing-plans` | plugin superpowers | 3 |
| Review de código | `/review` + `code-review` | global + plugin | 3+ |
| Commits e PRs | `commit-commands` | plugin oficial | todas |
| Extração das fontes (destilação) | `extrair-fonte` | `../01_DESTILACAO/.claude/skills/` | paralela |

## Skills de projeto a criar (futuro, quando a fase chegar)

| Skill | Cria quando | O que fará |
|---|---|---|
| `seed-dados` | início Fase 2 | Importa EXTRACAO_*.xlsx → banco, valida schema, relatório de carga |
| `golden-test` | início Fase 3 | Roda orçamento de referência × HOLLOS (R$ 216.188,04), diff item a item |

## Padrão visual dos mockups (substitui skill própria)

Documentado uma vez em `mockups/PADRAO.md` quando o primeiro mockup for aprovado:
header/nav comum, tipografia, paleta, componentes (tabela, formulário, card).
Todo mockup seguinte referencia o padrão — consistência sem skill dedicada.

## Referências de repo maduro

- **PWC** (`01-POWER_CONCEPT`): `.claude/rules/` granular, agents revisores, skills de contexto por módulo — copiar o formato quando o código crescer.
- **CONCILIADOR** (`08 - CONCILIADOR`): estrutura `docs/` (este projeto espelha), mockups HTML, engine separado do Django.
- **ALMOX** (`07 - ALMOX`): ordem de construção Django-first (modelos → Admin → DRF → frontend → seed → validação).
