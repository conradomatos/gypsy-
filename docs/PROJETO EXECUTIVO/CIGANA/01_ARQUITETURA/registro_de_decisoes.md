---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Registro de decisões — Gypsy

Decisões novas entram no topo. Decisão revogada fica marcada, nunca apagada.

---

## 2026-07-19 — Sessão de retomada do plano (Conrado + Claude)

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
Specs de tela em `06_TELAS/`, mockups em `mockups/` (raiz do repo).

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