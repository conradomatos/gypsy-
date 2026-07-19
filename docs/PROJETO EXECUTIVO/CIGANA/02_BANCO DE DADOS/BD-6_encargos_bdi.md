---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, banco-dados]
---

### encargos_bdi

Tabela de configuração de BDI (Bonificação e Despesas Indiretas) e encargos. Cada organização pode ter múltiplos perfis de BDI (ex: obra pública, obra privada, manutenção).

|   |   |   |   |
|---|---|---|---|
|**Coluna**|**Tipo**|**Constraints**|**Descrição**|
|**id**|UUID|PK|Identificador único|
|**organization_id**|UUID|FK organizations, NOT NULL|Tenant owner|
|**nome_perfil**|VARCHAR(100)|NOT NULL|Ex: BDI Obra Privada, BDI Manutenção|
|**administracao_central_pct**|NUMERIC(6,4)|NOT NULL|% Administração central|
|**seguro_garantia_pct**|NUMERIC(6,4)|NOT NULL|% Seguro e garantia|
|**risco_pct**|NUMERIC(6,4)|NOT NULL|% Risco/contingência|
|**despesas_financeiras_pct**|NUMERIC(6,4)|NOT NULL|% Despesas financeiras|
|**lucro_pct**|NUMERIC(6,4)|NOT NULL|% Lucro/bonificação|
|**impostos_pct**|NUMERIC(6,4)|NOT NULL|% Impostos (ISS, PIS, COFINS, IRPJ, CSLL)|
|**bdi_total**|NUMERIC(6,4)|GENERATED|Fórmula BDI consolidada (SINAPI/TCU)|
|**is_default**|BOOLEAN|DEFAULT false|Perfil padrão da organização|

**Fórmula BDI (TCU):** BDI = ((1 + AC + S + R + DF + L) / (1 - I)) - 1, onde AC=Adm Central, S=Seguro, R=Risco, DF=Desp Financeiras, L=Lucro, I=Impostos. Exemplo: ((1 + 0.04 + 0.01 + 0.015 + 0.012 + 0.08) / (1 - 0.0865)) - 1 = 0.2676 (26,76%).