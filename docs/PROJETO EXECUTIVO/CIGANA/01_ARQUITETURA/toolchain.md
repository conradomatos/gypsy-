---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Toolchain profissional — Gypsy

## Stack de ferramentas

### Gestão de projeto
| Ferramenta | Uso | Status |
|---|---|---|
| Jira | Épicos, features, tasks, sprints (projeto IP101) | Já existe |
| Obsidian | Documentação técnica, arquitetura, specs, decisões | Já montado |

### Desenvolvimento
| Ferramenta | Uso | Status |
|---|---|---|
| Claude Code | Dev principal (branches claude/*) | Já usa |
| Claude Chat | Copiloto — arquitetura, pesquisa, review | Já usa |
| GitHub | Repo, branches, PRs | Configurar (repo novo) |
| VS Code | Edição manual quando necessário | Já tem |

### Modelagem de dados
| Ferramenta | Uso | Status |
|---|---|---|
| dbdiagram.io | ERD visual, exporta SQL pra Postgres | Configurar |
| Supabase CLI | Migrations versionadas, db diff automático | Configurar |

### Qualidade
| Ferramenta | Uso | Status |
|---|---|---|
| Vitest | Testes unitários dos engines | Configurar com scaffold |
| GitHub Actions | CI automático: testes + build a cada PR | Configurar |
| Golden tests | Validação contra planilha HOLLOS | Configurar com seed |

### Infraestrutura
| Ferramenta | Uso | Status |
|---|---|---|
| Supabase | Banco + auth + storage + edge functions | Criar projeto novo |
| Coolify | Deploy automático (segundo app no VPS) | Configurar |
| Caddy | Reverse proxy + HTTPS automático | Já existe no VPS |
| Docker | Container do frontend (Node + Nginx) | Via Coolify |

### Monitoramento (pós-deploy)
| Ferramenta | Uso | Status |
|---|---|---|
| Sentry | Captura erros em produção (free tier) | Configurar no deploy |
| Supabase Dashboard | Logs, métricas API, uso de banco | Já vem com Supabase |

### O que NÃO usar (e por quê)
| Ferramenta | Por que não |
|---|---|
| Figma | Dev solo + shadcn + front-review skill é mais rápido |
| Storybook | Overkill pra dev solo com shadcn |
| Docker local | Coolify resolve build e deploy |
| Terraform/Pulumi | Infra simples demais pra IaC |
| Datadog/NewRelic | Sentry + Supabase dashboard é suficiente |