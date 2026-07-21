# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é o Gypsy

Motor de orçamentação por modelagem financeira da Concept Engenharia (montagem
elétrica industrial). Substitui as planilhas HOLLOS/MURILO por um sistema com base
de custos consolidada, composições auditáveis, dimensionador elétrico (NBR) e
análise de risco.

**Estado: docs-first. Ainda NÃO há código** — sem app Django, sem frontend, sem
migrations. Não há comandos de build/lint/test até o scaffold; não invente nenhum.

## Fonte de verdade (leia antes de agir)

1. **`docs/INDEX.md`** — qual documento é canônico por assunto.
2. **`docs/projeto-executivo/cigana/01_arquitetura/registro_de_decisoes.md`** —
   decisões; prevalece sobre doc antigo.
3. **`docs/LOG.md`** — diário operacional (o que foi feito, pendências).
4. Docs em `_historico/` ou marcados REVOGADO/HISTÓRICO **não** orientam implementação.

Divergiu de um doc sem decisão registrada? Pare e alinhe com o Conrado.

## Regras operacionais

As normas do projeto estão em **`.claude/rules/`** (carregadas automaticamente):
governança, subprojetos/gates, arquitetura vigente, engine/cálculos/testes,
dados/parâmetros, backend/frontend, nomenclatura, git/segurança/comunicação.
Não duplicá-las aqui — segui-las.

## Arquitetura vigente (detalhe em `01_arquitetura/stack_tecnica.md`)

- Frontend: React + TypeScript + Vite + Tailwind + shadcn/ui.
- Backend: Django + DRF + PostgreSQL (Python via uv).
- Engine de cálculo: Python puro, isolado (sem ORM/HTTP/I/O), `Decimal`.
- Integração: API REST. Local-first; produção PENDENTE.
- Revogado: Supabase, Edge Functions, Deno, RLS-como-autorização, Coolify.

## Como o trabalho é fatiado

Produto → **SP-xx** → M-xxx → F-xxx → T-xxx. Um SP por contexto (`/clear` ao trocar);
informe sempre o SP/módulo/feature/tarefa ativos. Mapa: `00_SUBPROJETOS.md`.
SP-00 (`destilacao/`) tem CLAUDE.md próprio. **SP ativo: SP-01 (fundação).** SP-02
(Telas) tem trabalho preliminar mas está bloqueado até o gate do SP-01.

## Gate do MVP

Golden test contra a HOLLOS: **R$ 216.188,04**, com divergência item a item explicável.

## Git

Branch → PR → merge, com gates verdes e após checar trabalho paralelo na base.
Push do Claude para `main` é bloqueado por deny rule global (push manual do Conrado).
Commit/push só com autorização; nunca force push nem alterar `main` direto.
