---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura, deploy]
revisado: 2026-07-19
---

# Deploy pipeline — Gypsy

> **Escopo:** o **fluxo lógico** do código até produção, **independente de provedor**.
> Nenhuma infraestrutura de produção foi escolhida — ver "Infraestrutura" abaixo.
> Classificação: **DECIDIDO** · **PENDENTE**. Versão anterior (Vite + Supabase + Coolify)
> em [`_historico/`](_historico/deploy_pipeline.supabase.2026-04-04.md).

## Princípios

- **Local-first (DECIDIDO):** todo desenvolvimento e validação acontecem localmente até
  o MVP fechar. Deploy só entra em cena depois do golden test.
- **Independente de provedor:** o pipeline lógico não pressupõe VPS, PaaS nem cloud
  específica. A etapa de execução em produção é abstrata até a infraestrutura ser decidida.

## Fluxo lógico

```
desenvolvimento local
  → branch
  → revisão
  → testes automatizados
  → aprovação
  → merge
  → geração de artefato
  → homologação (futura)
  → aprovação
  → produção (futura)
```

| Etapa | O que é | Status |
|---|---|---|
| Desenvolvimento local | Postgres, API e frontend rodando na máquina | DECIDIDO |
| Branch | Trabalho isolado por fatia (`branch → PR`) | DECIDIDO |
| Revisão | Code review antes do merge (agent `reviewer`) | DECIDIDO |
| Testes automatizados | pytest/engine + golden test verdes | PROPOSTO (toolchain) |
| Aprovação | Gate humano (Conrado; Sandro/Guilherme quando aplicável) | DECIDIDO |
| Merge | Só com gates verdes e sem trabalho paralelo conflitante | DECIDIDO |
| Geração de artefato | Empacotar backend + engine + build do frontend | PENDENTE (forma a definir) |
| Homologação | Ambiente de validação pré-produção | PENDENTE |
| Produção | Execução para usuários finais | PENDENTE |

## Infraestrutura de produção — PENDENTE

**Nenhum provedor foi escolhido.** Coolify foi abandonado (REVOGADO); não há substituto
definido, e este documento **não recomenda** VPS, PaaS ou cloud nesta etapa.

A decisão de infraestrutura será tomada **somente após**:

- validação funcional do MVP;
- conclusão do golden test (R$ 216.188,04);
- definição dos requisitos de segurança;
- definição de backup e recuperação;
- estimativa de usuários, processamento e armazenamento;
- análise de custo e de manutenção;
- definição de observabilidade.

Rollback, backup e observabilidade são **pendências futuras**, atreladas a essa decisão.

## Revogado (REVOGADO — 2026-07-19)

Não usar como vigente: **Coolify**, **Supabase**, **Edge Functions**, `app.costai.com.br`,
e variáveis `VITE_*` como configuração de **backend**. Referências antigas preservadas
apenas em [`_historico/`](_historico/deploy_pipeline.supabase.2026-04-04.md) e no
`registro_de_decisoes.md`.
