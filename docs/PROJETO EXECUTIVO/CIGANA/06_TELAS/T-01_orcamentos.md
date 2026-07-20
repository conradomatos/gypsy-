---
tipo: spec-tela
status: rascunho-aprovado-conrado
area: gypsy
tags: [gypsy, telas, sp-02]
criado: 2026-07-19
---

# T-01 — Área Orçamentos

> SP-02 Telas. Design aprovado pelo Conrado em 2026-07-19 (brainstorming).
> Pendente: mockup HTML + validação Sandro/Guilherme. Só congela após o gate.

Área-mãe do produto: todo o resto vive dentro do contexto de um orçamento.
Define o layout base (header, nav, padrão de tabela/formulário) que as outras telas herdam.

## Decisões de design (da sessão de brainstorming)

1. **Orçamento aberto = hub com etapas** (não abas estilo planilha, não direto na 1ª etapa)
2. **Cadastro mínimo + herança total** de parâmetros globais (ajuste depois, no hub)
3. **Revisão = snapshot imutável** + "Duplicar" para reuso entre obras

## 1. Lista — `/orcamentos`

Porta de entrada do sistema.

- **Tabela:** Nº · Cliente · Obra · Local/UF · Tipo (Industrial/Predial) · REV vigente ·
  Status · Valor total · Atualizado em
- **Status:** Rascunho / Em elaboração / Enviado / Ganho / Perdido
- **Busca:** por cliente, obra ou nº. **Filtros:** status, tipo
- **Ações por linha:** Abrir · Duplicar (novo orçamento a partir deste) · Nova revisão
- **Linha expansível:** histórico de revisões (snapshots read-only, com data e valor)
- **Botão primário:** Novo orçamento

## 2. Cadastro — `/orcamentos/novo`

Mínimo — criar orçamento leva ~30 segundos.

- **Campos:** Cliente (select do cadastro + criação rápida inline) · Obra (nome/descrição) ·
  Local (cidade/UF) · Tipo (Industrial/Predial) · Data · Observação
- **Automáticos:** Nº sequencial · REV-00 · status Rascunho
- **Parâmetros:** herda 100% dos globais — nenhum parâmetro aparece no cadastro
- **Ao salvar:** redireciona para o hub do orçamento

## 3. Hub do orçamento — `/orcamentos/:id`

Centro de comando. O que o Sandro vê ao abrir um orçamento.

- **Topo:** identificação (nº, cliente, obra, REV, status) + totais ao vivo:
  Custo direto · BDI · Preço de venda · HH total (zerados até os módulos alimentarem)
- **Cards de etapa** com status (vazio / em andamento / concluído):
  Dimensionador → Estimativa (WBS) → Equipe → Custos Operacionais → Resumo
- **Card lateral Parâmetros do Projeto:** exibe "herdando globais" ou "N overrides";
  é o caminho para ajustar encargos/impostos/fatores deste orçamento
- **Ações:** Nova revisão (congela snapshot da atual, cria REV-N+1 editável) ·
  Duplicar · Exportar (fase 5)

## Implicações para o modelo de dados (SP-04)

- Revisão é snapshot imutável; a lista mostra a revisão vigente
- Totais do hub são derivados dos módulos — nunca digitados
- Status do orçamento é workflow simples (sem máquina de estados complexa no MVP)
- Cliente é cadastro próprio (select + criação rápida)

## Estados e vazios

- Lista vazia: empty state com CTA "Criar primeiro orçamento"
- Hub recém-criado: todos os cards em "vazio", totais zerados
- Snapshot aberto (revisão antiga): banner read-only "REV-N congelada em DD/MM — visualização"
