# Registro de decisões — Gypsy

Formato: data · decisão · motivo. Decisões novas entram no topo.

---

## 2026-07-19 — Sessão de retomada do plano (Conrado + Claude)

### Stack: Django + DRF + Postgres + uv (REVOGA React+Supabase de 2026-04-04)
Mesmo padrão dos apps ALMOX e CONCILIADOR. Motivo: convergência dos apps da Concept
para Django; reaproveitamento de padrões, docs e experiência entre projetos.
Engine de cálculo em Python puro (`engine/`), fora do Django.

### Telas primeiro (REVOGA "engine primeiro" de 2026-04-04)
Mockups HTML clicáveis das 8 áreas, com dados fake, validados com Sandro/Guilherme
ANTES de modelos e engines. Motivo: validar o produto visualmente é mais barato que
descobrir erro de conceito com o engine pronto. O rigor do engine (puro + testado +
golden test) permanece — muda só a ordem.

### Casa do projeto: repo gypsy- + diretório 02_GYPSY
- Repo: github.com/conradomatos/gypsy- (main)
- Local: `04. ORCAMENTACAO_POR_MODELAGEM_FINANCEIRA/02_GYPSY/`
- `01_DESTILACAO/` é subprojeto irmão (fora do repo), segue intocado
- Docs migram do gypsy-vault (Obsidian) para `docs/` — o vault vira histórico
- Estrutura de docs espelha o CONCILIADOR (PRE_PROJETO + PROJETO_EXECUTIVO)

### Skills: reusar, não criar
Nenhuma skill nova agora. Mapa em `skills_e_toolchain.md`. Duas skills finas de
projeto (`seed-dados`, `golden-test`) nascem quando as fases 2 e 3 chegarem.

### MVP: reproduzir um orçamento completo
Materiais + MO + equipamentos + encargos + BDI com composições manuais, batendo o
golden test (R$ 216.188,04 × HOLLOS). Dimensionador, Monte Carlo e leitura de edital
são pós-MVP.

---

## 2026-04-04 / 2026-04-07 — Decisões anteriores (vault, ainda válidas salvo revogação acima)

- **Módulos M-000..M-006 e motores MC-001..MC-003** — estrutura mantida
- **Ordem dos engines:** MC-001 HH → M-005 Equipe → MC-002 BDI → M-001.1 Força → M-004 → M-006.1
- **Inglês no código/banco, PT-BR em docs/UI**
- **Nome do produto: Gypsy** (CostAI é branding antigo)
- **Tabelas NBR como constantes no código; catálogos de fabricante no banco**
- **Parâmetros em dois níveis: globais + override por orçamento**
- **Encargos sociais como parâmetro configurável, perfis por regime tributário**
- **Horas improdutivas como fator multiplicador sobre Hxh**
- **M-005 não é cronograma — é Hxh total + prazo → equipe por função**
- ~~Stack React 18 + Vite + shadcn + Supabase~~ → REVOGADA 2026-07-19
- ~~Engine primeiro, tela depois, sem Figma~~ → REVOGADA 2026-07-19 (telas primeiro)
