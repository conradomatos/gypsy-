---
tipo: referencia
status: historico
area: gypsy
tags: [gypsy, arquitetura, historico]
---

# _HISTORICO — Arquivo de documentos revogados

## Finalidade

Esta pasta guarda **versões revogadas** de documentos de arquitetura do Gypsy.
Existe para **auditoria e rastreabilidade** — poder recuperar o que se decidiu no
passado e por que foi mudado.

## Regras

- **Documentos históricos NÃO orientam implementação.** São registro, não guia.
- O **documento vigente permanece no caminho canônico** (`01_ARQUITETURA/<nome>.md`),
  com o mesmo nome de sempre, para não quebrar referências.
- **Decisões vigentes prevalecem sobre o histórico.** Em qualquer conflito, vale o
  documento canônico e o `registro_de_decisoes.md`.
- Cada arquivo aqui tem, no topo, um cabeçalho `STATUS: REVOGADO` com a data da
  revogação, a decisão substituta e o caminho do documento vigente.
- **Nada aqui é apagado.** Conteúdo histórico é preservado integralmente (abaixo do
  cabeçalho, o corpo é cópia byte-a-byte do original).

## Nomenclatura dos arquivos

`<nome-original>.<stack-revogada>.<data-da-versão>.md`

Exemplo: `stack_tecnica.react-supabase.2026-04-04.md` — a versão de 2026-04-04 do
`stack_tecnica.md`, baseada em React + Supabase.

## Conteúdo atual (revogado em 2026-07-19)

| Arquivo histórico | Documento vigente | Stack revogada |
|-------------------|-------------------|----------------|
| `stack_tecnica.react-supabase.2026-04-04.md` | `../stack_tecnica.md` | React + Supabase + Edge Functions (Deno) |
| `toolchain.supabase.2026-04-04.md` | `../toolchain.md` | Supabase CLI + Vitest + dbdiagram + Coolify |
| `deploy_pipeline.supabase.2026-04-04.md` | `../deploy_pipeline.md` | Vite + Supabase + Coolify |
| `padroes_de_codigo.supabase.2026-04-04.md` | `../padroes_de_codigo.md` | Engines TypeScript + cliente Supabase + RLS |

Decisão que motivou a revogação: `../registro_de_decisoes.md`, entrada de 2026-07-19
(convergência para Django + DRF + PostgreSQL; React permanece como frontend).
