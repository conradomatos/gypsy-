---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

## Auth & RBAC (12 tabelas)
| Tabela                         | Rows | Uso                    |
| ------------------------------ | ---- | ---------------------- |
| user_roles                     | 6    | Roles legado           |
| profiles                       | 4    | Perfis de usuário      |
| system_modules                 | 9    | Módulos do sistema     |
| system_resources               | 35   | Recursos por módulo    |
| system_actions                 | 8    | Ações (CRUD)           |
| system_permissions             | 281  | Permissões disponíveis |
| rbac_roles                     | 9    | Roles RBAC             |
| rbac_role_permissions          | 888  | Permissões por role    |
| rbac_user_roles                | 8    | Roles por usuário      |
| rbac_user_permission_overrides | 0    | Overrides individuais  |
| rbac_audit_log                 | 4    | Log de auditoria       |
| activity_log                   | 0    | Log de atividade       |
|                                |      |                        |
