# Pipeline de execução — Gypsy

> Revoga o pipeline de 2026-04-04 ("engine primeiro, tela depois").
> Decisão de 2026-07-19: **telas primeiro** — mockups validam o produto antes do código.

## Princípio

Mockup → validação humana → banco → engine → tela real. A UI é especificada e validada
com dados fake antes de existir modelo ou cálculo. O engine continua puro e testado
(regra `engine-puro-e-testes`), só muda a ordem: ele nasce depois que a tela dele já
foi aprovada.

## Fase 0 — Fundação documental

```
1. Repo + estrutura docs/                      ✓ feito (2026-07-19)
2. Regras do projeto (.claude/rules/)          ✓ feito
3. Migrar docs do gypsy-vault para docs/       → Conrado traz o conteúdo
4. Registro das decisões novas                 ✓ feito
5. CLAUDE.md do repo                           → escrever com Conrado (por último)
```

**Gate:** revisão do Conrado.

## Fase 1 — Telas primeiro

Para cada uma das 8 áreas de navegação (ver `modulos_e_navegacao` no vault, a migrar):
Home, Orçamentos, Dimensionador, Base de custos, Custos operacionais, Planejamento,
Relatórios, Configurações.

```
1. Spec da tela em docs/.../06_TELAS/          (propósito, campos, ações, estados)
2. Mockup HTML em mockups/                     (dados fake realistas da HOLLOS,
                                                navegação clicável entre páginas,
                                                padrão visual único)
3. Revisão Conrado → ajuste
4. Validação Sandro/Guilherme
5. Congela a spec (mudança depois = decisão registrada)
```

**Gate:** navegação completa validada pelos usuários.

## Fase 2 — Banco e seed

```
1. Modelos Django (inglês) por app de domínio  ← specs BD-x de 02_BANCO_DE_DADOS
2. Migrations + Django Admin (CRUD de graça)
3. Seed via management command                 ← EXTRACAO_*.xlsx da destilação
4. Relatório do seed: o que entrou, o que falhou, órfãos
```

**Gate:** banco populado com dados reais, navegável no Admin.

## Fase 3 — Engines por fatia vertical

Ordem (do registro de decisões, mantida):

| # | Módulo | Por quê |
|---|--------|---------|
| 1 | MC-001 Composição HH | Tudo depende do custo/hora |
| 2 | M-005 Estimador de equipe | Desbloqueia custos que dependem de pessoas |
| 3 | MC-002 BDI/Markup | Fecha o preço de venda |
| 4 | M-001.1 Dimensionador força | Core técnico |
| 5 | M-004 Custos operacionais | Depende de MC-001 e M-005 |
| 6 | M-006.1 Resumo | Consolida tudo — é o output |

Ciclo por módulo (não pular etapa, não avançar sem validar):

```
1. Migration (se faltar tabela)
2. Engine (engine/ — Python puro)
3. Teste pytest (casos do Sandro + valores HOLLOS)
4. Golden test parcial (o pedaço bate com a planilha?)
5. Ligar a tela real (que já foi validada na Fase 1) via DRF
6. Validar com Sandro
7. PR + merge
```

**Gate:** todos os testes verdes por módulo.

## Fase 4 — Golden test completo

Orçamento de referência inteiro no sistema × HOLLOS: **R$ 216.188,04**.
Divergência item a item explicada (erro documentado da planilha ou bug nosso).

**Gate:** MVP pronto. Só aqui se fala em deploy.

## Fase 5 — Pós-MVP

Instrumentação, Pintura, Cotações, Monte Carlo, Proposta PDF, deploy VPS/Coolify.
Ordem a decidir quando chegar.

## Trilha paralela — Destilação (Spec 0)

`../01_DESTILACAO/` segue no próprio ritmo (HOLLOS em andamento, MURILO na fila).
Precisa estar consolidada antes do seed da Fase 2. Não bloqueia as Fases 0–1.
