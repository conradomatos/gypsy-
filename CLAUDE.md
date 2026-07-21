# CLAUDE.md

As instruções canônicas deste repo vivem em `AGENTS.md` (portável entre ferramentas).
O Claude Code as carrega pelo import abaixo — não duplicar conteúdo aqui.

@AGENTS.md

## Específico do Claude Code

- As `.claude/rules/*.md` são carregadas automaticamente em toda sessão (regras granulares
  enforçadas); `AGENTS.md` as indexa, não as substitui.
- `destilacao/` tem `AGENTS.md`/`CLAUDE.md` próprios, carregados sob demanda ao trabalhar lá.
- Processo de trabalho: skills `superpowers` + agents (`planner`, `reviewer`, `debugger`,
  `Explore`). Mapa em `docs/projeto-executivo/cigana/01_arquitetura/skills_e_toolchain.md`.
