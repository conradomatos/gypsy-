---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

## Tabelas Operacionais

Tabelas que suportam a operação diária: orçamentos, projetos, propostas. Referenciam as tabelas core mas pertencem ao contexto específico de cada projeto.

### Resumo das Tabelas Operacionais

|   |   |   |
|---|---|---|
|**Tabela**|**Descrição**|**Principais Colunas (além das padrão)**|
|**organizations**|Empresas/tenants. Raíz do multi-tenancy.|nome, cnpj, plano (starter/pro/enterprise), settings (JSONB)|
|**users**|Usuários do sistema. Vinculados a auth.users do Supabase.|auth_user_id (FK auth.users), organization_id, role (admin/manager/user), nome, email|
|**projetos**|Agrupa orçamentos de uma mesma obra/contrato.|organization_id, cliente_id, nome, descricao, status, localizacao (JSONB com lat/lng/cidade/uf)|
|**clientes**|Cadastro de clientes da organização.|organization_id, razao_social, cnpj, contato_nome, contato_email, contato_telefone|
|**orcamentos**|Orçamento completo com WBS e itens.|projeto_id, encargo_bdi_id, status (rascunho/em_revisao/aprovado/enviado), valor_total, revisao, moeda|
|**orcamento_itens**|Itens do orçamento (linha a linha da WBS).|orcamento_id, composicao_id (versão específica), wbs_code, quantidade, custo_unitario_ajustado, custo_total, fatores_aplicados (JSONB)|
|**propostas**|Propostas comerciais geradas a partir de orçamentos.|orcamento_id, template_id, conteudo (JSONB), status, pdf_url, enviado_em|
|**audit_log**|Log imutável de todas as mutações.|user_id, organization_id, tabela, registro_id, acao (INSERT/UPDATE/DELETE), dados_antes (JSONB), dados_depois (JSONB), ip|
|**fatores_projeto**|Fatores de ajuste aplicados a um projeto específico.|projeto_id, tipo_fator, valor, justificativa, fonte_dado, aplicado_por|
