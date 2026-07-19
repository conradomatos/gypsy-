---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Pipeline de execução — Gypsy

## Princípio: engine primeiro, tela depois, polish no final

Não fazer Figma antes de validar a lógica. Não fazer tela antes de ter o engine testado.
shadcn + Tailwind dá UI funcional sem design prévio. Front-review skill ajusta depois.

## Fase 0 — Fundação (pré-código)

Abordagem database-first: schema completo antes de qualquer código.
A planilha HOLLOS é a spec funcional — o modelo de dados está implícito nela.

```
1. Arquitetura no Obsidian                    ✓ feito
2. ERD completo (todas tabelas, relações)     → pendente
3. Review do ERD                              → pendente
4. Migrations SQL versionadas                 → pendente
5. Aplicar no Supabase (projeto novo)         → pendente
6. Seed com dados reais (HOLLOS + SINAPI)     → pendente
7. CLAUDE.md (constituição do repo)           → pendente
8. Criar repo GitHub + scaffold Vite          → pendente
9. Gerar types do Supabase                    → pendente
```

Resultado: banco completo, populado com dados reais, types gerados. Zero UI.

## Fase 1 — Desenvolvimento vertical (módulo a módulo)

Cada módulo é uma fatia completa do banco à tela. Não avança pro próximo sem validar o atual.
Não fazer camada horizontal (todos engines → todos hooks → todas telas). Isso atrasa a descoberta de erros.

Para cada módulo, na ordem:

```
1. Migration (tabelas deste módulo, se não criadas na Fase 0)
2. Engine (src/engines/ — TypeScript puro, sem React)
3. Teste unitário (Vitest, casos de validação do Sandro)
4. Golden test parcial (resultado bate com planilha HOLLOS?)
5. Hook React (wrapper do engine)
6. Tela funcional (shadcn, sem design — feia mas funciona)
7. Validar com Sandro
8. Commit + PR
9. Próximo módulo
```

### Ordem de execução dos módulos

| # | Módulo | Justificativa |
|---|--------|--------------|
| 1 | MC-1 Composição HH | Mais crítico — tudo depende do custo/hora |
| 2 | M-005 Estimador de equipe | Desbloqueia custos que dependem de pessoas |
| 3 | MC-2 BDI/Markup | Fecha o preço de venda |
| 4 | M-001.1 Dimensionador força | Core técnico, pode ir parcialmente em paralelo |
| 5 | M-004 Custos operacionais | Depende de MC-1 e M-005 |
| 6 | M-006.1 Resumo | Consolida tudo — é o output |
| 7 | Golden test completo | R$ 216.188,04 bate? |
| 8 | Restante | Instrumentação, Pintura, Cotações, Monte Carlo, PDF |
## Fase 2 — Polish

```
1. UI review (prints → front-review skill → issues)
2. Ajustes visuais e fluxo de navegação
3. Proposta PDF (template Concept)
4. Deploy produção
```

## Sem Figma

Figma só se precisar vender a ideia pra investidor ou mostrar pra cliente.
Para dev solo + Claude Code, shadcn + front-review é mais rápido.
Se um dia precisar de Figma, faz com a tela funcionando como referência.

## Por que engine antes de tela

Se faz tela primeiro, descobre na hora do cálculo que:
- O modelo de dados está errado
- Falta um campo que a tela não previu
- A fórmula precisa de um input diferente
Aí refaz tudo. Engine primeiro força entender a lógica antes de desenhar.