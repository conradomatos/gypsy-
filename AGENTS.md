# AGENTS.md — Gypsy

> Fonte canônica de instruções de trabalho para agentes de IA neste repo, **portável entre
> ferramentas** (Claude Code, Cursor, Copilot, etc.). O `CLAUDE.md` da raiz apenas importa
> este arquivo (`@AGENTS.md`). É um roteador de *como trabalhar* — o *conteúdo* (regras de
> negócio, arquitetura, schema) vive em `docs/` e nas `.claude/rules/`; aqui não se duplica.

## O que é o Gypsy

Motor de orçamentação por modelagem financeira da Concept Engenharia (montagem elétrica
industrial). Substitui as planilhas HOLLOS/MURILO por um sistema com base de custos
consolidada, composições auditáveis, dimensionador elétrico (NBR) e análise de risco.

**Estado: docs-first. Ainda NÃO há código** — sem app Django, sem frontend, sem migrations.

## Fonte de verdade (leia antes de agir)

Precedência (maior → menor): decisões registradas → INDEX → doc canônico → este arquivo →
`.claude/rules/` → spec da feature → plano da tarefa.

1. `docs/INDEX.md` — qual documento é canônico por assunto.
2. `docs/projeto-executivo/cigana/01_arquitetura/registro_de_decisoes.md` — decisões;
   prevalece sobre doc antigo.
3. `docs/LOG.md` — diário operacional.
4. Docs em `_historico/` ou marcados REVOGADO/HISTÓRICO **não** orientam implementação.

## Arquitetura vigente

- **Frontend:** React + TypeScript + Vite + Tailwind + shadcn/ui.
- **Backend:** Django + DRF + PostgreSQL (Python via `uv`).
- **Engine de cálculo:** Python puro, isolado (sem ORM/HTTP/I/O), `Decimal` para dinheiro.
- **Integração:** API REST. Local-first; infraestrutura de produção PENDENTE.
- **Revogado:** Supabase, Edge Functions, Deno, RLS-como-autorização, Coolify.

Detalhe: `01_arquitetura/stack_tecnica.md`. Estrutura de código (DECIDIDO): monorepo
`apps/engine`, `apps/backend`, `apps/frontend`, `infra/` — pasta nasce no scaffold, não antes
(ver `padroes_de_codigo.md`).

## Como o trabalho é fatiado

Produto → **SP-xx** → M-xxx → F-xxx → T-xxx. Um SP por contexto (`/clear` ao trocar);
informe sempre SP/módulo/feature/tarefa ativos. Mapa: `cigana/00_SUBPROJETOS.md`.
**SP ativo: SP-01 (fundação).** SP-00 (`destilacao/`) tem `AGENTS.md` próprio.

## Comandos

**Nenhum comando de build/lint/test/migration existe até o scaffold — não invente nenhum.**
A toolchain (Ruff, Pyright, pytest, Vitest…) está **PROPOSTA**, não decidida
(`01_arquitetura/toolchain.md`). Esta seção será preenchida no scaffold de cada app.

## Testes

- Todo cálculo crítico exige teste (pytest). Engine sem teste não está concluído.
- **Gate do MVP — golden test:** reproduzir o orçamento de referência × HOLLOS batendo
  **R$ 216.188,04**, com divergência item a item explicável.

## Estilo e nomenclatura

- **Código, banco e API em inglês**; UI, `docs/` e textos ao usuário em PT-BR.
- **TypeScript strict** — nunca `any` nem `@ts-ignore`.
- `Decimal` para valores monetários, nunca `float`; arredondamento explícito quando a
  norma/HOLLOS exigir.
- Detalhe: `01_arquitetura/convencoes_nomenclatura.md` e `padroes_de_codigo.md`.

## Git

Branch → PR → merge, com gates verdes e após checar trabalho paralelo na base.
Commits descritivos em PT-BR. Push do Claude para `main` é bloqueado por deny global
(push manual do Conrado).

## Regras granulares (enforçadas)

As normas completas estão em `.claude/rules/` (auto-carregadas pelo Claude Code). Não
duplicá-las aqui — segui-las:
`00` governança · `01` subprojetos/gates · `02` arquitetura · `03` engine/testes ·
`04` dados/parâmetros · `05` backend/frontend · `06` nomenclatura · `07` git/segurança.

---

## LIMITES — três camadas

### ✅ SEMPRE
- Ler `INDEX.md` + `registro_de_decisoes.md` antes de agir num assunto.
- Trabalhar em branch; mostrar `git diff` antes de commit.
- `Decimal` para dinheiro; dado sem fonte fica vazio (campo vazio é informação).
- Entregar evidência (comandos, resultados, `git status`) antes de dizer "pronto";
  diferenciar fato · inferência · recomendação · decisão aprovada.

### ⚠️ PERGUNTAR ANTES
- Commit ou push.
- Criar dependência, biblioteca ou ferramenta nova (PROPOSTO não vira DECIDIDO sozinho).
- Definir/alterar schema, models ou migrations (schema não aprovado — SP-04).
- Divergir de um doc canônico sem decisão registrada.
- Executar entrega de um SP que não é o ativo.
- Ação destrutiva/externa difícil de reverter (deletar, sobrescrever, publicar).

### ⛔ NUNCA
- Token/chave/segredo hardcoded — usar `.env` ou secrets. Não ler nem expor `.env`.
- `any` ou `@ts-ignore` em TypeScript.
- Force push; alterar `main` diretamente; remover bloqueios/denys globais.
- RLS-como-autorização, Supabase, Edge Functions, Deno, Coolify (revogados).
- Sobrescrever `destilacao/fontes/` (read-only, fora do git).
- Inventar regra de negócio, fórmula, nome de tabela/campo ou fluxo.
