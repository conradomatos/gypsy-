# LOG — Diário de bordo do Gypsy

> Uma entrada por sessão de trabalho: o que foi feito, decisões (link pro registro),
> pendências ao sair. Entradas novas no topo. Decisões formais vivem em
> `PROJETO EXECUTIVO/CIGANA/01_ARQUITETURA/registro_de_decisoes.md` — aqui é o rastro operacional.

---

## 2026-07-19 (SP-01) — Adequação da fundação para Django + React (Conrado + Claude)

**Feito:**
- Branch `chore/adequacao-fundacao-django-react` criada a partir da main local.
- Auditoria estrutural de `01_ARQUITETURA/` + INDEX: contradições React/Supabase mapeadas.
- Histórico preservado em `01_ARQUITETURA/_HISTORICO/` (4 cópias React/Supabase com banner
  REVOGADO + README de política); corpos verificados byte-a-byte (md5 == original).
- Docs canônicos reescritos para a stack vigente (Django+DRF+React+Postgres+engine Python
  puro): `stack_tecnica`, `toolchain`, `deploy_pipeline`, `padroes_de_codigo`,
  `convencoes_nomenclatura`, `pendencias_arquitetura`; `registro_de_decisoes` com entrada
  SP-01; `INDEX` corrigido (schema PENDENTE, sem `costai_schema.dbml`).
- READMEs gerais corrigidos (raiz completa a stack; CIGANA remove schema inexistente).
- Dívidas de migração de SP-04/05/07 (RLS, Supabase auth, Edge Functions) e branding CostAI
  registradas em `pendencias_arquitetura.md`, sem tocar nos docs donos.
- `.claude/rules/` finalizadas: 6 rascunhos → **8 rules** numeradas (governança, subprojetos/
  gates, arquitetura, engine/testes, dados/parâmetros, backend/frontend, nomenclatura,
  git/segurança/comunicação).
- **`CLAUDE.md` da raiz escrito** (índice operacional curto).

**Estado:** SP-01 (fundação documental) fechado; aguardando gate final do Conrado.
Commit na branch, sem push (push para main é manual).

**Pendências ao sair:**
- [ ] Conrado: gate final do SP-01 + push/merge da branch.
- [ ] Dívidas de migração nos SP-04/05/07 (ver `pendencias_arquitetura.md`).
- [ ] Branding "CostAI" em `PRE PROJETO/GATE_APRESENTACAO/*` (pendência separada).
- [ ] Desbloquear SP-02 (Telas) só após o gate do SP-01.

---

## 2026-07-19 — Retomada do projeto (Conrado + Claude)

**Feito:**
- Repo `gypsy-` clonado para `02_GYPSY/`, estrutura base criada (docs, mockups, referencias)
- Documentação do gypsy-vault (Obsidian) importada para `docs/` — vault vira histórico
- Estrutura unificada: `PROJETO EXECUTIVO/CIGANA/` é a canônica; `06_TELAS/` criada
- Pivôs registrados: stack Django+DRF+Postgres+uv; telas primeiro; processo superpowers+agents
- Regras em `.claude/rules/` (6 arquivos — RASCUNHO, versão final será do Conrado)
- Pipeline reescrito (fases 0–5) e toolchain de skills/agents documentada
- Subprojetos SP-00..SP-10 definidos espelhando a árvore de docs (`00_SUBPROJETOS.md`)
- Destilação movida para dentro do repo (`destilacao/`); skill `extrair-fonte` no `.claude/skills/`
- /doctor rodado: instalação saudável, v2.1.215 = latest; nenhuma limpeza aplicada (decisão Conrado)
- **SP-02 iniciado:** spec da área Orçamentos (`06_TELAS/T-01_orcamentos.md`) — hub com etapas,
  cadastro mínimo com herança de parâmetros, revisão = snapshot

**Descoberto:**
- `git push * main` é bloqueado por regra deny do próprio Conrado em `~/.claude/settings.json` —
  pushes para main são manuais (ou trabalhar via branch+PR)
- Lista de skills da sessão está ~75% acima do orçamento de contexto (descrições longas do claude-bpo)

**Pendências ao sair:**
- [ ] Push manual dos commits da main local (deny rule bloqueia o Claude)
- [ ] Conrado: reescrever as regras de `.claude/rules/` (hoje são rascunho)
- [ ] Conrado: revisar docs revogados (stack_tecnica, toolchain, deploy_pipeline — era React/Supabase)
- [ ] CLAUDE.md do repo — escrever juntos, por último
- [ ] Pasta `01_DESTILACAO/` vazia — apagar numa sessão futura aberta em `02_GYPSY`
- [ ] Próximo: mockup HTML da T-01 (lista + cadastro + hub) → revisão Conrado → Sandro/Guilherme
