---
tipo: projeto
status: ativo
area: gypsy
tags: [gypsy, visao-geral]
criado: 2026-04-07
---

# GYPSY — Índice da Documentação

**Produto:** Gypsy (motor de cost intelligence para montagem elétrica industrial)
**Jira:** IP101 | **Repo:** a definir | **Supabase:** projeto separado do [[MOC_PowerConcept|PWC]]
**Última revisão:** 2026-04-07
**Área:** [[MOC_Concept-Engenharia|Concept Engenharia]]

---

## Estrutura de pastas

| Pasta | Status | Conteúdo |
|-------|--------|----------|
| `PROJETO EXECUTIVO/CIGANA/` | **VIGENTE** — source of truth | Arquitetura, schema DBML, padrões de código, módulos, motores, parâmetros, pipeline |
| `PRE PROJETO/GATE_APRESENTACAO/` | **VIGENTE** — referência de negócio | Mapa de 37 abas HOLLOS → 16 componentes Gypsy, problema, objetivo, personas |
| `PRE PROJETO/GATE DESTILACAO/` | **VIGENTE** — data engineering | Spec 0, fontes de dados, referências de mercado |
| `PRE PROJETO/MONTE CARLO/` | **REFERÊNCIA** — conceitual | Explicações sobre estimativa paramétrica, casos, fases |
| `PRE PROJETO/_ARQUIVO/` | **ARQUIVADO** — não usar como spec | DOC_1 e DOC_2: charter, market research, schema antigo. Úteis como histórico de visão mas CONTRADITÓRIOS com Projeto Executivo |
| `Cálculos/` | **FORA DE ESCOPO** — pertence ao PWC | CUSTO CLT.md é memorial do PowerConcept módulo Recursos |

## Documento autoritativo por assunto

| Assunto | Documento vigente | NÃO usar |
|---------|-------------------|----------|
| Schema do banco | `PROJETO EXECUTIVO/CIGANA/02_BANCO DE DADOS/costai_schema.dbml` | DOC_2/schema, BD-1 a BD-6 (desatualizados) |
| Stack técnica | `PROJETO EXECUTIVO/CIGANA/01_ARQUITETURA/stack_tecnica.md` | DOC_1/4_arquitetura_tecnica.md |
| Módulos e navegação | `PROJETO EXECUTIVO/CIGANA/01_ARQUITETURA/modulos_e_navegacao.md` | DOC_1/5_roadmap |
| Pipeline de execução | `PROJETO EXECUTIVO/CIGANA/01_ARQUITETURA/pipeline_de_execucao.md` | DOC_1/5_roadmap |
| Mapa de abas → módulos | `PRE PROJETO/GATE_APRESENTACAO/BLOCO_001/discussao_modulos_planilha_hollos.md` | — |
| Benchmark competitivo | `PRE PROJETO/GATE_APRESENTACAO/BLOCO_001/visao_geral.md` | DOC_1/2_market_research |
| BDI / Formação de preço | `PROJETO EXECUTIVO/CIGANA/05_MOTORES DE CALCULO/MC-002_bdi_markup.md` | DOC_1/3_catalogo |

## Decisões de nomenclatura

- **Inglês 100%** para banco de dados, código e tipos TypeScript (decisão Conrado 2026-04-04)
- **Português** apenas para documentação no Obsidian e textos voltados ao usuário final
- **Nome do produto:** Gypsy (não "CostAI" — branding antigo, presente apenas nos docs arquivados)

## Pendências documentais

- [x] ~~Mover `Cálculos/CUSTO CLT.md` para pasta do PWC~~ ✅ movido
- [ ] Mover `PRE PROJETO/DOCS_WORD/DOC_1` e `DOC_2` para `PRE PROJETO/_ARQUIVO/`
- [ ] Reescrever BD-1 a BD-6 para refletir o DBML (inglês) ou deletar
- [ ] Preencher ou deletar arquivos vazios (MC-002, MC-003, B2-3.4, B2-3.5, BD-4, README)
- [ ] Resolver comentários `[!comment] Conrado` pendentes nos docs
- [ ] Escrever CLAUDE.md do repo Gypsy (pré-requisito para iniciar código)
