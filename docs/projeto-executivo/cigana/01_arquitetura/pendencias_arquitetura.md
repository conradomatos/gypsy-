---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura, pendencias]
revisado: 2026-07-19
---

# Itens pendentes de definição — Arquitetura Gypsy

> Classificação: **PENDENTE** (a decidir) · **PROPOSTO** (sugerido, não decidido).
> Documentos vigentes de arquitetura estão em `01_arquitetura/` (canônicos); os revogados,
> em `_historico/`. Nenhuma pendência abaixo autoriza escrever código nesta etapa.

## 1. Modelo de dados — PENDENTE

**Schema não aprovado.** Não há schema vigente e **não existe DBML aprovado**. Será
definido no **subprojeto responsável pelo banco de dados (SP-04)**, após a validação das
telas (SP-02) e das regras de negócio. As specs `02_banco-de-dados/BD-1..BD-6` são
material preliminar de referência, não schema aprovado, e ainda precisam ser convertidas
para nomenclatura inglesa quando o schema for desenhado.

> Nota vigente (também no INDEX): "Modelo de dados ainda não aprovado. Será definido no
> subprojeto responsável pelo banco de dados, após validação das telas e regras de negócio."

## 2. Infraestrutura de produção — PENDENTE

Nenhum provedor escolhido (Coolify abandonado, sem substituto). Decisão só após MVP
validado, golden test concluído e definição de segurança, backup, observabilidade,
estimativas de uso e custo. Ver [`deploy_pipeline.md`](deploy_pipeline.md).

## 3. Toolchain — ferramentas PROPOSTAS pendentes de validação

Ruff, Pyright, pytest, DRF-Spectacular (OpenAPI), cliente TypeScript gerado, Vitest,
Playwright, Storybook, GitHub Actions, observabilidade. Cada uma será validada no momento
próprio — ver [`toolchain.md`](toolchain.md). Não são decisões.

## 4. Dados normativos (NBR) — localização PROPOSTA

Tabelas NBR (5410/14039/5419) ficam em **estrutura própria do engine** como constantes
versionadas (não no banco, não por tenant). O **caminho exato** (`engine/data/` ou
equivalente) é **PROPOSTO** e será fixado no subprojeto do engine. Ver
[`padroes_de_codigo.md`](padroes_de_codigo.md).

## Pendências de migração por subprojeto

Contradições da era React/Supabase encontradas em documentos **fora do SP-01** (banco,
módulos, saída). **Não foram alteradas nesta sessão** — a correção pertence ao subprojeto
dono, no gate indicado. Registradas aqui como dívida de migração.

| Caminho exato | Problema | Tecnologia antiga | SP responsável | Gate de correção | Impacto se não corrigir |
|---|---|---|---|---|---|
| `02_banco-de-dados/000.md` | Declara "schema autoritativo em `costai_schema.dbml`" (inexistente) e seção **RLS** | DBML CostAI + RLS | **SP-04** | Desenho e aprovação do schema | Induz uso de schema inexistente e de RLS como autorização |
| `02_banco-de-dados/tabelas_operacionais.md` | `users` "vinculados a **`auth.users` do Supabase**" (FK `auth_user_id`) | Supabase Auth | **SP-04** | Modelagem de usuários/auth | Modelo de autenticação incorreto (deve ser auth do Django) |
| `04_modulos/C1-modulos-funcionais/M-001_dimensionador/M-001.1_forca_(motores).md` | Task **T-101** "Criar migration + **RLS**" | RLS | **SP-05** | Implementação do M-001.1 | Task orienta criar RLS |
| `04_modulos/C1-modulos-funcionais/M-001_dimensionador/M-001.2_infra_(trechos).md` | Task **T-131** "Criar migration + **RLS**" | RLS | **SP-05** | Implementação do M-001.2 | Task orienta criar RLS |
| `04_modulos/C1-modulos-funcionais/M-002_motor_de_estimativa/M-002.2_assemblies_parametrizaveis.md` | Task **T-202** "migrations + **RLS** + triggers" | RLS | **SP-05** | Implementação do M-002.2 | Task orienta criar RLS |
| `04_modulos/C3-modulo-saida-resultados/M-006.1_resumo_de_precos.md` e `M-006.3_proposta_pdf_excel.md` | "**Edge Function** existe (generate-budget-pdf)" | Edge Functions (Supabase/Deno) | **SP-07** | Implementação do M-006 (saída) | Aponta função Supabase inexistente no backend Django |
| `projeto-executivo/cigana/02_banco-de-dados/000.md`, specs `BD-1..BD-6` | Nomenclatura de tabelas/colunas em português; a definir em inglês | — (nomenclatura) | **SP-04** | Desenho do schema | Retrabalho de nomes; divergência com `convencoes_nomenclatura.md` |

### Branding "CostAI" — RESOLVIDO nos docs vigentes (2026-07-19)

- **Docs vigentes:** `pre-projeto/gate-apresentacao/bloco-001/` (`discussao_modulos_planilha_hollos.md`,
  `visao_geral.md`) migrados de "CostAI" → **"Gypsy"**. ✅
- **Docs arquivados:** `pre-projeto/_arquivo/doc-1/` **mantém "CostAI" de propósito** — são
  históricos, e a convenção é que o branding antigo só aparece em arquivado/histórico
  (ver `convencoes_nomenclatura.md`). Não migrar.

## 5. Fundação documental — etapas finais do SP-01 (ordem) — CONCLUÍDO

1. **`.claude/rules/`** — 8 rules numeradas gravadas. ✅
2. **Governança em `AGENTS.md`** (2026-07-20) — fonte canônica portável na raiz e em
   `destilacao/`; `CLAUDE.md` virou ponteiro que importa via `@AGENTS.md`. `.claude/rules/`
   permanecem auto-carregadas e indexadas pelo AGENTS.md. Sem comandos de build/lint/test
   inventados (não há scaffold); sem duplicar as rules. ✅

Checklist do `AGENTS.md`/`CLAUDE.md` (referenciar **documentos vigentes**):
- Stack → [`stack_tecnica.md`](stack_tecnica.md)
- Toolchain → [`toolchain.md`](toolchain.md)
- Padrões → [`padroes_de_codigo.md`](padroes_de_codigo.md)
- Nomenclatura → [`convencoes_nomenclatura.md`](convencoes_nomenclatura.md)
- Módulos e navegação → [`modulos_e_navegacao.md`](modulos_e_navegacao.md)
- Pipeline → [`pipeline_de_execucao.md`](pipeline_de_execucao.md)
- Deploy → [`deploy_pipeline.md`](deploy_pipeline.md)
- Regras invioláveis → `.claude/rules/` (engine puro + testes, golden test, parâmetros,
  rastreabilidade, nomenclatura, local-first)
