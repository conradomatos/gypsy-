---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Registro de decisões — Gypsy

Decisões novas entram no topo. Decisão revogada fica marcada, nunca apagada.

Cada item é classificado: **DECIDIDO** · **PROPOSTO** · **PENDENTE** · **REVOGADO** · **HISTÓRICO**.

---

## 2026-07-20 (SP-01) — Reorganização estrutural + governança AGENTS.md (Conrado + Claude)

### Estrutura de código — layout DECIDIDO (pasta só no scaffold)
- **DECIDIDO:** monorepo com `apps/engine`, `apps/backend`, `apps/frontend` e `infra/`.
  Promove a PROPOSTA de layout em `padroes_de_codigo.md` a **DECIDIDO** (só os *nomes/estrutura*).
- A **pasta física não é criada agora** — nasce no SP do scaffold. Materializar `apps/*` vazio
  hoje congelaria layout sem necessidade (pasta vazia não tem histórico a preservar).
- **Continuam PROPOSTO** (não promovidos): toolchain concreta (Ruff/Pyright/pytest/Vitest…) e
  o caminho exato das tabelas normativas NBR dentro do engine.

### Higiene de nomes — DECIDIDO e aplicado (PR de rename)
- Pastas de `docs/` renomeadas para minúsculo-com-hífen, sem espaços/parênteses, via `git mv`
  (histórico preservado). Códigos identificadores (`M-###`, `BD-#`, `C1/C2/C3`, `MC-###`)
  preservados; codinome `CIGANA → cigana`. Arquivos `.md` internos não renomeados nesta etapa.

### Governança — migração para AGENTS.md — DECIDIDO
- **`AGENTS.md` é a fonte canônica portável** de instruções de trabalho, nos níveis que existem:
  **raiz** e **`destilacao/`**. Formato PRD + limites em três camadas (SEMPRE / PERGUNTAR ANTES / NUNCA).
- **`CLAUDE.md` vira ponteiro** que importa o `AGENTS.md` via `@AGENTS.md` (Claude Code **não**
  auto-carrega AGENTS.md; carrega CLAUDE.md + `.claude/rules/`. Import nativo confirmado nos docs
  oficiais). `.claude/rules/` **permanecem** auto-carregadas; AGENTS.md as indexa, não duplica.
- Não se cria AGENTS.md/CLAUDE.md em `apps/*` enquanto as pastas não existirem.

### Sementes de futuro — PROPOSTO (design, não implementação)
- Revisor adversarial de PR + CI como portão de merge desenhados em `revisao_e_ci.md`
  (**PROPOSTO**). Não implementam nada; ativam quando houver código.

---

## 2026-07-19 (SP-02) — Fluxo de telas: Claude Code especifica, Claude Design prototipa

Fluxo **padrão** (DECIDIDO) para produzir telas:
1. **Claude Code → especifica** o funcionamento: descritivo funcional em `06_telas/`.
2. **Claude Design → protótipo** interativo (fora do repo), a partir do descritivo.
3. **Conrado + Sandro/Guilherme → validam** o fluxo.
4. **Claude Code → implementa em React**.

- **Papel do Claude Code:** especifica e implementa; **não** produz o protótipo visual
  por padrão. Direção visual (paleta, tipografia, densidade) é decidida no Claude Design.
- **Rota rápida (LEVE):** se o Conrado quiser gerar algo rápido sem o Design, pode pedir
  um mockup direto ao Claude Code. É exceção sob demanda, não o padrão. Não é camisa de força.
- **Fonte de verdade:** comportamento/regra = descritivo em `06_telas/` (canônico);
  visual = protótipo validado (referência); implementação = React. Conflito de
  *comportamento* → o descritivo vence; de *aparência* → o protótipo vence.
- **`frontend-design`** é ferramenta da **implementação React** (etapa 4), não da prototipagem.
- **`mockups/`** deixa de ser onde o Claude Code escreve HTML; guarda, se útil, referência
  dos protótipos validados (opcional).
- **Etapa 5 — "Claude Design recebe os componentes reais": PROPOSTO.** Mecanismo (Storybook,
  export de componentes, screenshots) ainda não definido; não adotar como decisão até definir.

---

## 2026-07-19 (SP-01) — Consolidação da fundação documental (Conrado + Claude)

Sessão dedicada ao SP-01 (Arquitetura): eliminar contradições da era React/Supabase,
adequar a documentação à arquitetura vigente e arquivar o histórico sem apagá-lo.

### Frontend — permanece (DECIDIDO)
A revogação de 2026-07-19 revoga **React + Supabase como conjunto arquitetural**, e
**não** o React como frontend. Permanecem, como camada de apresentação que consome a
API Django/DRF:
- **React**, **TypeScript**, **Vite**, **Tailwind CSS**, **shadcn/ui**.

### Backend e engine — vigentes (DECIDIDO)
- Backend: **Django + Django REST Framework + PostgreSQL**, Python gerenciado por **uv**.
- Engine de cálculo: **Python puro**, isolado do Django — sem ORM, sem HTTP, sem I/O nas
  funções de cálculo; determinístico e testável direto. **Valores monetários em `Decimal`,
  nunca `float`.**
- Integração: **API REST** entre frontend e backend.

### Revogado (REVOGADO)
Supabase, Edge Functions, Deno, cliente Supabase, backend implementado no Supabase e
**RLS como mecanismo principal de autorização**. Autorização vigente = auth do Django +
permissions do DRF. Docs da era antiga arquivados em `01_arquitetura/_historico/` com
banner `REVOGADO` — conteúdo preservado, não orienta implementação.

### Deploy — Coolify abandonado; infraestrutura PENDENTE
- **Coolify não será usado no Gypsy** (REVOGADO). Removido das docs vigentes.
- Nenhum provedor (VPS/PaaS/cloud) é escolhido nesta etapa. Projeto segue **local-first**.
- **Infraestrutura de produção = PENDENTE**, a decidir só após: MVP validado, golden test
  concluído, requisitos de segurança/backup/observabilidade, estimativas de uso e custo.
- `deploy_pipeline.md` documenta apenas o **fluxo lógico independente de provedor**.

### Ferramentas propostas (PROPOSTO — não decidido)
Registradas para validação futura, sem status de decisão: OpenAPI/DRF-Spectacular,
geração de cliente TypeScript, Ruff, Pyright, pytest, Vitest, Playwright, Storybook,
GitHub Actions, observabilidade. Detalhe e critério de validação em `toolchain.md`.

### Modelo de dados — PENDENTE
Schema (incl. DBML) **não aprovado**. Será definido no subprojeto de banco de dados,
após validação das telas e das regras de negócio. Localização das tabelas normativas
(NBR) em estrutura própria do engine é **PROPOSTA**, não congelada.

### Escopo desta sessão
SP-01 consolida a **fundação documental**. `.claude/rules/` (finalização) e o `CLAUDE.md`
da raiz são as últimas etapas do SP-01, nesta ordem, cada uma com aprovação do Conrado.
SP-02 (Telas) tem trabalho preliminar (spec T-01 + LOG) mas segue **bloqueado até o gate
do SP-01**.

---

## 2026-07-19 — Sessão de retomada do plano (Conrado + Claude)

### Subprojetos espelham a árvore de docs; destilação DENTRO do Gypsy
- Trabalho fatiado em SP-00..SP-10 (ver `00_SUBPROJETOS.md`): Telas, Parâmetros,
  Banco, C1/C2/C3, MC-001..MC-003 — um ciclo superpowers completo por subprojeto.
- **Destilação movida para `destilacao/` na raiz do repo** (supersede "01_DESTILACAO
  fora do repo" decidido mais cedo na mesma data). Planilhas-fonte continuam fora do
  git (`.gitignore`); scripts, specs e CLAUDE.md próprio versionam.
- Skill `extrair-fonte` movida para `.claude/skills/` do repo.

### Stack: Django + DRF + Postgres + uv (REVOGA React+Supabase de 2026-04-04)
Mesmo padrão dos apps ALMOX e CONCILIADOR. Motivo: convergência dos apps da Concept
para Django; reaproveitamento de padrões, docs e experiência entre projetos.
Engine de cálculo em Python puro (`engine/`), fora do Django.
Docs revogados por esta decisão: `stack_tecnica.md`, `toolchain.md`, `deploy_pipeline.md`
e `padroes_de_codigo.md` (partes React/Supabase) — reescrever quando o código começar.

### Telas primeiro (REVOGA "engine primeiro" de 2026-04-04)
Mockups HTML clicáveis das 8 áreas, com dados fake, validados com Sandro/Guilherme
ANTES de modelos e engines. Motivo: validar o produto visualmente é mais barato que
descobrir erro de conceito com o engine pronto. O rigor do engine (puro + testado +
golden test R$ 216.188,04) permanece — muda só a ordem.
Specs de tela em `06_telas/`, mockups em `mockups/` (raiz do repo).

### Casa do projeto: repo gypsy- + diretório 02_GYPSY
- Repo: github.com/conradomatos/gypsy- (main)
- Local: `04. ORCAMENTACAO_POR_MODELAGEM_FINANCEIRA/02_GYPSY/`
- `01_DESTILACAO/` é subprojeto irmão (fora do repo), segue intocado
- `docs/` deste repo é a fonte de verdade; o gypsy-vault (Obsidian) vira histórico

### Processo de desenvolvimento: skills superpowers + agents (sem skill nova)
Pipeline operacional baseado nas skills do plugin superpowers (brainstorming →
writing-plans → executing-plans → TDD → review) com os agents existentes (planner,
reviewer, debugger, Explore). Mapa completo em `skills_e_toolchain.md`.
Regras do projeto em `.claude/rules/` — **rascunho do Claude; versão final será
escrita pelo Conrado.**

### MVP: reproduzir um orçamento completo
Materiais + MO + equipamentos + encargos + BDI com composições manuais, batendo o
golden test (R$ 216.188,04 × HOLLOS). Dimensionador, Monte Carlo e leitura de edital
são pós-MVP.

---

## 2026-04-04 — Sessão: discussão de módulos, arquitetura e pipeline

> Decisões de stack e pipeline desta sessão foram REVOGADAS em 2026-07-19 (ver acima).
> Decisões de módulos, motores e parâmetros permanecem válidas.

## Decisões de módulos

### M-001 Dimensionador
- Absorve todo cálculo técnico de engenharia que gera lista de materiais
- Sub-módulos: Força (1.1), Infra (1.2), Alimentadores (1.3), Iluminação (1.4), Painéis (1.5 futuro), Instrumentação (1.6), Pintura (1.7), SPDA (1.8)
- Pintura foi movida de M-004 para M-001 — é cálculo técnico, não custo operacional
- SPDA incluído conforme decisão do Conrado

### M-004 Custos Operacionais (renomeado de "Custos Indiretos")
- Nome antigo "Custos Indiretos" estava errado — a maioria dos itens é custo direto rastreável
- Sub-módulos: Mob/Desmob (4.1), Canteiro (4.2), Equipamentos (4.3), Engenharia (4.4), Seguros (4.5), Segurança e Saúde (4.6), Despesas Gerenciais (4.7)
- Mob/Desmob é sub-módulo próprio com calculadora dedicada (não item avulso)

### M-005 Estimador de Equipe (renomeado de "Planejamento")
- NÃO é módulo de cronograma — é o cálculo Hxh total + prazo → equipe por função
- Essencial pro MVP: sem ele, custos que dependem de quantidade de pessoas não fecham
- Histograma visual e Cronograma de Desembolso ficam pra v2
### MC-1 Motor Composição HH
- Horas improdutivas entram como fator multiplicador sobre Hxh (não sobre custo/hora)
- Alimentação pessoal: abordagem HÍBRIDA — cálculo no MC-1, apresentação decomposta no Resumo (rastreabilidade pro memorial de cálculo)
- Encargos sociais: PARÂMETRO configurável, não valor fixo. Perfis por regime tributário (Lucro Real, Presumido, Simples, MEI/PJ)
- EPI, ferramentas, hospedagem, transporte: parâmetros do MC-1

### Camada de parâmetros
- Dois níveis: globais (nível empresa) + projeto (override por orçamento)
- Defaults com override: orçamentista cria orçamento → herda globais → ajusta o que for diferente
- Horas improdutivas: calculador dentro da camada de parâmetros do projeto

## Decisões de arquitetura

### Stack
- Manter mesma stack do PWC (React 18 + TS + Vite + shadcn + Supabase + Coolify)
- Projeto Supabase SEPARADO do PWC
- Mesmo VPS, segundo app no Coolify

### Padrões de código (melhorias vs PWC)
1. src/engines/ — lógica de cálculo pura, zero React, zero Supabase
2. Testes obrigatórios nos engines (Vitest)
3. Golden test contra planilha HOLLOS (R$ 216.188,04)
4. ParametrosProvider — context React que carrega uma vez
5. src/types/ — schemas centralizados

### Pipeline de execução
- Database-first: schema completo antes de qualquer código
- ERD no dbdiagram.io → review → migrations → seed com dados reais
- Desenvolvimento vertical: módulo a módulo (banco → engine → teste → hook → tela → validar)
- NÃO fazer camada horizontal (todos engines → todos hooks → todas telas)
- Sem Figma: shadcn + front-review skill

### Toolchain profissional
- dbdiagram.io — ERD e schema
- GitHub Actions — CI automático (testes + build a cada PR)
- Vitest — testes unitários
- Sentry — captura erros em produção (free tier)
- Supabase CLI — migrations versionadas

### Ordem de execução dos módulos
1. MC-1 Composição HH — mais crítico, tudo depende dele
2. M-005 Estimador de equipe — desbloqueia custos que dependem de pessoas
3. MC-2 BDI/Markup — fecha preço de venda
4. M-001.1 Dimensionador força — core técnico
5. M-004 Custos operacionais — depende de MC-1 e M-005
6. M-006.1 Resumo — consolida tudo
7. Golden test completo — R$ 216.188,04 bate?
8. Restante (Instrumentação, Pintura, Cotações, Monte Carlo, PDF)

## Mapa completo: 37 abas → módulos CostAI

Todas as 37 abas da planilha HOLLOS têm destino definido. Zero órfãs.
Doc detalhado: arquivo gypsy-arquitetura-modulos.md gerado na sessão.

## Próximo passo concreto

ERD completo no dbdiagram.io → review → migrations → seed → CLAUDE.md → scaffold repo