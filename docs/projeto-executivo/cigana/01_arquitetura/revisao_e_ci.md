---
tipo: referencia
status: proposto
area: gypsy
tags: [gypsy, arquitetura, ci, revisao]
criado: 2026-07-20
---

# Revisão adversarial de PR + CI — Gypsy

> **Classificação: PROPOSTO.** Este documento **desenha** dois portões de qualidade; não
> implementa nada e não decide toolchain. Ativa **quando houver código** (a partir do
> scaffold). Ferramentas citadas seguem PROPOSTO em [`toolchain.md`](toolchain.md).

## 1. Revisor adversarial de PR (design)

**Objetivo:** antes de todo merge, uma revisão que tenta *refutar* a mudança — foca bug
real, regressão, segurança e violação de regra do projeto, não estilo.

- **Quem:** agents já existentes — `reviewer` (sênior: bugs, performance, segurança) e,
  em mudança crítica (engines, cálculo, migrations), um segundo par com
  `feature-dev:code-reviewer`. Sem criar agente novo.
- **Postura:** adversarial — o revisor assume que há defeito e tenta prová-lo; em dúvida,
  reprova e pede evidência. Casa com a skill `superpowers:requesting-code-review`.
- **Checklist mínimo por PR:**
  - Engine: função pura, determinística, `Decimal`, teste cobrindo a regra (não só linha).
  - Golden test não regride (quando aplicável ao módulo).
  - Sem segredo, sem `any`/`@ts-ignore`, sem RLS/Supabase/Coolify, sem parâmetro hardcoded.
  - Regra de negócio fora de view/serializer/componente.
  - Nomes em inglês no código; número com fonte/data-base quando aplicável.
- **Saída:** achados priorizados (severidade), cada um com cenário de falha concreto.

## 2. CI como portão de merge (design)

**Objetivo:** todo PR passa por checagem automática antes de poder mergear. **Só faz
sentido com código** — não criar workflow que roda em repo docs-only.

- **Plataforma:** GitHub Actions (PROPOSTO).
- **Jobs previstos (ativam por app, conforme o scaffold chega):**
  - `backend/engine`: lint **Ruff** + type-check **Pyright** + **pytest** (inclui golden test
    quando o módulo existir).
  - `frontend`: type-check `tsc` (strict) + **Vitest** + build Vite.
- **Regra de merge:** CI verde obrigatório; alinhado ao branch protection da `main`
  (exigir PR + status checks).
- **Pré-commit local (opcional, com o scaffold):** Ruff format/lint e checagem de segredo,
  para pegar cedo o que a CI pegaria tarde.

## 3. Quando implementar

| Portão | Gatilho de implementação |
|---|---|
| Revisor adversarial (via agents) | Já usável em qualquer PR de conteúdo; obrigatório a partir do 1º código |
| Pré-commit hooks | Scaffold do backend |
| CI GitHub Actions | 1º teste automatizado no repo |
| Status checks no branch protection | Quando a CI existir |

Nada aqui promove ferramenta a DECIDIDO — a validação de toolchain segue seu próprio gate.
