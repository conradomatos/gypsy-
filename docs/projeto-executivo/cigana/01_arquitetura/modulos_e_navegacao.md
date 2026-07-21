---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Módulos e navegação — Gypsy

## 8 áreas de navegação

| Área                | NavigationArea        | Rotas principais                                                                                                                                                                                                                              |
| ------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Home                | `home`                | `/home`                                                                                                                                                                                                                                       |
| Orçamentos          | `orcamentos`          | `/orcamentos`, `/orcamentos/:id/*`                                                                                                                                                                                                            |
| Dimensionador       | `dimensionador`       | `/dimensionador/forca`, `/dimensionador/infra`, `/dimensionador/alimentadores`, `/dimensionador/iluminacao`, `/dimensionador/instrumentacao`, `/dimensionador/pintura`, `/dimensionador/spda`                                                 |
| Base de custos      | `base-custos`         | `/base-custos/insumos`, `/base-custos/mao-de-obra`, `/base-custos/equipamentos`, `/base-custos/historico`                                                                                                                                     |
| Custos operacionais | `custos-operacionais` | `/custos-operacionais/mob-desmob`, `/custos-operacionais/canteiro`, `/custos-operacionais/equipamentos`, `/custos-operacionais/engenharia`, `/custos-operacionais/seguros`, `/custos-operacionais/seguranca`, `/custos-operacionais/despesas` |
| Planejamento        | `planejamento`        | `/planejamento/equipe`                                                                                                                                                                                                                        |
| Relatórios          | `relatorios`          | `/relatorios/resumo`, `/relatorios/monte-carlo`, `/relatorios/proposta`, `/relatorios/dashboards`                                                                                                                                             |
| Configurações       | `config`              | `/config/parametros-globais`, `/config/parametros-projeto`, `/config/encargos`, `/config/impostos`                                                                                                                                            |

## Fluxo de navegação do orçamento

```
/orcamentos (lista) → /orcamentos/novo (cadastro M-000)
  → /orcamentos/:id/dimensionador (M-001)
  → /orcamentos/:id/estimativa (M-002 — WBS + assemblies)
  → /orcamentos/:id/equipe (M-005 — estimador)
  → /orcamentos/:id/custos-operacionais (M-004)
  → /orcamentos/:id/resumo (M-006 — saída)
```

Cada orçamento tem seu contexto (ParametrosProvider) carregado ao entrar na rota `/orcamentos/:id/*`.