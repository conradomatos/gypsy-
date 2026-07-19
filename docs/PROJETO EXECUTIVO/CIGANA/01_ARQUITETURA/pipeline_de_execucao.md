---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Pipeline de execução — Gypsy

> Versão 2026-07-19. Revoga o pipeline de 2026-04-04 ("engine primeiro, tela depois").
> Duas mudanças: **telas primeiro** e **processo = skills superpowers + agents**
> (nada de processo inventado por sessão — o fluxo é sempre o mesmo).

## Espinha dorsal: superpowers

Todo trabalho não-trivial neste repo segue o ciclo das skills do plugin superpowers:

```
1. superpowers:brainstorming        → refinar a ideia, apresentar design, aprovar
2. superpowers:writing-plans        → plano de implementação escrito
3. superpowers:executing-plans      → executar com checkpoints de review
   (ou subagent-driven-development para tarefas independentes em paralelo)
4. superpowers:test-driven-development → em TODO engine (teste antes do código)
5. superpowers:requesting-code-review  → antes de merge
6. superpowers:verification-before-completion → evidência antes de dizer "pronto"
7. superpowers:finishing-a-development-branch → merge/PR/cleanup
```

Bug → `superpowers:systematic-debugging` (com o agent `debugger`), nunca band-aid.

## Agents

| Agent | Quando usar |
|---|---|
| `planner` | Criar plano de implementação antes de código (par do writing-plans) |
| `reviewer` | Review de código antes de merge — bugs reais, performance, segurança |
| `debugger` | Causa raiz de bugs (reproduz, isola, traça) |
| `Explore` | Buscas amplas no código/docs sem poluir o contexto |
| `feature-dev:code-architect` | Desenho de arquitetura de feature nova (blueprint) |

Regra: trabalho de review e debug passa pelo agent correspondente — não fazer inline
em sessão longa.

## Fases do projeto

### Fase 0 — Fundação documental
```
1. Repo + estrutura docs/                      ✓ 2026-07-19
2. Docs do vault importados                    ✓ 2026-07-19
3. Regras (.claude/rules/)                     → rascunho feito; Conrado escreve a final
4. Registro das decisões novas                 ✓ 2026-07-19
5. CLAUDE.md do repo                           → escrever com Conrado (por último)
```
**Gate:** revisão do Conrado.

### Fase 1 — Telas primeiro
Para cada uma das 8 áreas (`modulos_e_navegacao.md`): Home, Orçamentos, Dimensionador,
Base de custos, Custos operacionais, Planejamento, Relatórios, Configurações.

```
1. superpowers:brainstorming → spec da tela em 06_TELAS/
2. Mockup HTML em mockups/ (frontend-design + dados fake realistas da HOLLOS via xlsx)
3. Revisão Conrado → ajuste
4. Validação Sandro/Guilherme
5. Congela a spec (mudança depois = decisão registrada)
```
**Gate:** navegação completa clicável validada pelos usuários.

### Fase 2 — Banco e seed
```
1. brainstorming + writing-plans do schema (specs BD-x → modelos Django, inglês)
2. Migrations + Django Admin
3. Seed via management command ← EXTRACAO_*.xlsx da destilação
4. Relatório do seed (o que entrou, falhou, órfãos)
```
**Gate:** banco populado com dados reais, navegável no Admin.

### Fase 3 — Engines por fatia vertical
Ordem mantida: MC-001 HH → M-005 Equipe → MC-002 BDI → M-001.1 Força → M-004 → M-006.1.

Ciclo por módulo (ciclo superpowers completo):
```
1. writing-plans do módulo (agent planner)
2. TDD no engine (Python puro, casos do Sandro + valores HOLLOS)
3. Golden test parcial (o pedaço bate com a planilha?)
4. Ligar a tela real (já validada na Fase 1) via DRF
5. requesting-code-review (agent reviewer) → PR → merge
6. Validar com Sandro
```
**Gate:** testes verdes por módulo.

### Fase 4 — Golden test completo
Orçamento de referência inteiro × HOLLOS: **R$ 216.188,04**, divergências explicadas.
**Gate:** MVP pronto. Só aqui se fala em deploy.

### Fase 5 — Pós-MVP
Instrumentação, Pintura, Cotações, Monte Carlo, Proposta PDF, deploy VPS/Coolify.

## Trilha paralela — Destilação (Spec 0)
`../01_DESTILACAO/` segue no próprio ritmo. Precisa estar consolidada antes do seed
da Fase 2. Não bloqueia as Fases 0–1.
