---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura, toolchain]
revisado: 2026-07-19
---

# Toolchain — Gypsy

> **Escopo:** ferramentas usadas para **desenvolver, testar, validar e operar** o projeto.
> As tecnologias que compõem o produto estão em [`stack_tecnica.md`](stack_tecnica.md) —
> não duplicar aqui.
>
> Classificação: **DECIDIDO** · **PROPOSTO** · **PENDENTE**.
> Versão anterior (Supabase CLI/Vitest/dbdiagram/Coolify) em
> [`_historico/`](_historico/toolchain.supabase.2026-04-04.md).

> **Importante:** este documento **não registra comandos** (build, lint, test, migration,
> scripts de frontend, Docker). Comandos concretos entram no `CLAUDE.md` da raiz e/ou nos
> READMEs **quando o scaffold existir**. Hoje não há código; inventar comando seria erro.

## Ferramentas DECIDIDAS

Adotadas ou em uso comprovado no projeto.

| Ferramenta | Finalidade |
|---|---|
| **uv** | Gerência de Python e dependências do backend/engine |
| **Git** | Versionamento (branch → PR → merge) |
| **Ambiente local** | Desenvolvimento local-first (Postgres local, API local, frontend local) |
| **Vite** | Build e dev server do frontend (faz parte da stack; ver `stack_tecnica.md`) |

## Ferramentas PROPOSTAS

Registradas para validação futura. **Nenhuma é decisão definitiva.** Cada uma será
avaliada no momento indicado; até lá, não configurar como obrigatória nem documentar
seus comandos.

| Ferramenta | Finalidade | Ganho esperado | Validar quando | Status |
|---|---|---|---|---|
| **Ruff** | Lint + format Python | Padrão de código consistente, rápido | Início do scaffold backend | PROPOSTO |
| **Pyright** | Type-check Python | Tipagem estática no backend/engine | Início do scaffold backend | PROPOSTO |
| **pytest** | Testes backend + engine | Base do TDD e do golden test | 1º engine (Fase 3) | PROPOSTO |
| **DRF-Spectacular** | Gera schema **OpenAPI** do DRF | Contrato de API versionado e verificável | Ao expor os 1ºs endpoints | PROPOSTO |
| **Cliente TS gerado** | Cliente TypeScript a partir do OpenAPI | Frontend tipado ponta a ponta, menos drift | Depois do OpenAPI estável | PROPOSTO |
| **Vitest** | Testes unitários do frontend | Cobertura de lógica de UI/hooks | Quando o frontend tiver lógica | PROPOSTO |
| **Playwright** | Testes end-to-end | Validar fluxos de tela reais | Após telas integradas à API | PROPOSTO |
| **Storybook** | Catálogo de componentes | Desenvolver/validar UI isolada | Se a UI crescer o suficiente | PROPOSTO |
| **GitHub Actions** | CI (lint + testes por PR) | Gate automático antes do merge | Quando houver testes a rodar | PROPOSTO |
| **Observabilidade** | Logs/erros/métricas em produção | Diagnóstico pós-deploy | Junto da decisão de produção | PROPOSTO |

## Pendências de toolchain (PENDENTE)

- Escolha final entre as ferramentas propostas — depende do início do código.
- Ferramenta de observabilidade específica — atrelada à decisão de infraestrutura de
  produção, que é **PENDENTE** (ver [`deploy_pipeline.md`](deploy_pipeline.md)).
