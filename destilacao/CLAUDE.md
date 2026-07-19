# CLAUDE.md — Spec 0: Destilação de Dados CostAI

## Contexto

Este projeto é a fase de data engineering ("projeto antes do projeto") do CostAI — um motor de cost intelligence para orçamentação de obras de montagem elétrica industrial. O objetivo é extrair, normalizar e consolidar dados de múltiplas fontes heterogêneas em tabelas padronizadas que alimentarão o banco de dados do CostAI.

**Operador:** Conrado Matos (engenheiro eletricista, Concept Engenharia)
**Validação de domínio:** Conrado + Sandro (orçamentista sênior)

## Regras

1. **NUNCA modifique os arquivos-fonte.** Sempre leia como read-only e gere novos arquivos de saída.
2. **Uma fonte por vez.** Não misture dados de fontes diferentes no mesmo passo de extração.
3. **Sempre gere Excel (.xlsx)** como output intermediário, com uma aba por tabela-destino.
4. **Inclua coluna `_fonte`** em todas as tabelas com o nome da planilha de origem.
5. **Inclua coluna `_aba_origem`** com o nome da aba de onde o dado foi extraído.
6. **Inclua coluna `_linha_origem`** com o número da linha no arquivo fonte (para auditoria).
7. **Inclua coluna `_confianca`** (alta/media/baixa) quando houver interpretação.
8. **Marque com `_revisar = SIM`** qualquer dado que precisar de validação humana.
9. **Normalize unidades:** PÇ/PC/pç/UN → UN | M/m/ML/ml → M | M2/m2/m² → M2 | KG/kg/Kg → KG | H/h/HH/Hh → H | VB/vb → VB | CJ/cj → CJ | L/l → L
10. **Normalize texto:** UPPERCASE para descrições. Remover espaços duplos. Remover caracteres especiais desnecessários.
11. **Preços sempre em R$ sem imposto** (quando possível identificar). Se incluir imposto, marcar `_inclui_imposto = SIM`.
12. **Datas no formato ISO:** YYYY-MM-DD.
13. **Não invente dados.** Se um campo não existe na fonte, deixe vazio. Nunca preencha com estimativa.
14. **Fórmulas Excel:** Quando encontrar composições implícitas em fórmulas, extraia a fórmula E o valor calculado. Documente a lógica na coluna `_formula_original`.

## Tabelas-Destino (schema padrão)

### 1. Insumos
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| codigo_fonte | texto | sim | Código no arquivo original |
| nome | texto | sim | Descrição normalizada (UPPERCASE) |
| unidade | texto | sim | Normalizada (UN, M, M2, KG, H, VB, CJ, L) |
| familia | texto | sim | Nível 1 da hierarquia: ELETRODUTO, CABO, LEITO, ELETROCALHA, FERRAGEM, CONECTOR, TERMINAL, FIXADOR, QUADRO, DISJUNTOR, PORTICO, etc. |
| subfamilia | texto | não | Nível 2: GALVANIZADO A FOGO, PVC, CORRUGADO, METALICO FLEXIVEL, COBRE FLEXIVEL, PERFURADO, etc. Deixar vazio se não identificável na fonte. |
| classe | texto | não | Nível 3: especificação dimensional ou técnica (1", 3/4", 2.5mm², 300x100, 15KV, etc.). Deixar vazio se não identificável na fonte. |
| preco_unitario | número | não | Preço unitário R$ (sem imposto quando possível) |
| preco_fabricante | número | não | Preço do fabricante (antes de markup/reajuste), quando disponível |
| hh_unitario | número | não | Homem-hora por unidade do insumo (HH/UN). OBRIGATÓRIO extrair quando disponível na fonte — dado crítico para composições |
| data_referencia | data | não | Data do preço |
| fabricante | texto | não | Fabricante/marca |
| ncm | texto | não | NCM quando disponível |
| _fonte | texto | sim | Nome do arquivo origem |
| _aba_origem | texto | sim | Aba de onde veio |
| _linha_origem | número | sim | Linha no arquivo original |
| _confianca | texto | não | alta/media/baixa |
| _revisar | texto | não | SIM se precisar validação humana |
| _inclui_imposto | texto | não | SIM se preço inclui imposto |
| _observacao | texto | não | Notas sobre o dado |

### 2. Mão de Obra
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| codigo_fonte | texto | não | Código CBO ou interno |
| funcao | texto | sim | Nome da função (UPPERCASE) |
| tipo | texto | sim | CLT / PJ / HORISTA |
| salario_mensal | número | não | Salário base mensal R$ |
| custo_hora | número | não | Custo por hora R$ |
| periculosidade | número | não | Percentual (0.30 = 30%) |
| encargos_percentual | número | não | Percentual total de encargos |
| custo_hora_com_encargos | número | não | Custo/hora tudo incluído |
| dissidio_referencia | texto | não | Ano/sindicato do dissídio |
| _fonte | texto | sim | Nome do arquivo origem |
| _aba_origem | texto | sim | Aba de onde veio |
| _linha_origem | número | sim | Linha no arquivo original |
| _confianca | texto | não | alta/media/baixa |
| _revisar | texto | não | SIM se precisar validação humana |
| _formula_original | texto | não | Fórmula Excel se custo foi calculado |

### 3. Equipamentos
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| codigo_fonte | texto | não | Código interno |
| nome | texto | sim | Descrição (UPPERCASE) |
| tipo | texto | sim | PROPRIO / ALUGADO / TERCEIRIZADO |
| custo_mensal | número | não | Custo mensal R$ |
| custo_hora | número | não | Custo por hora R$ |
| depreciacao_meses | número | não | Vida útil em meses |
| valor_aquisicao | número | não | Preço de compra R$ |
| _fonte | texto | sim | Nome do arquivo origem |
| _aba_origem | texto | sim | Aba de onde veio |
| _linha_origem | número | sim | Linha no arquivo original |
| _confianca | texto | não | alta/media/baixa |
| _revisar | texto | não | SIM se precisar validação humana |

### 4. Composições
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| codigo | texto | sim | Código da composição |
| nome | texto | sim | Descrição do serviço (UPPERCASE) |
| unidade | texto | sim | Unidade de medição (M, UN, CJ, VB) |
| tipo | texto | sim | MOI / MOD / SERVICO / MATERIAL_COMPOSTO |
| custo_unitario_calculado | número | não | Custo total calculado |
| _fonte | texto | sim | Nome do arquivo origem |
| _aba_origem | texto | sim | Aba de onde veio |
| _linha_origem | número | sim | Linha no arquivo original |
| _confianca | texto | não | alta/media/baixa |
| _revisar | texto | não | SIM se precisar validação humana |
| _formula_original | texto | não | Se composição veio de fórmula |

### 5. Itens da Composição
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| composicao_codigo | texto | sim | Código da composição pai |
| tipo_item | texto | sim | INSUMO / MAO_DE_OBRA / EQUIPAMENTO |
| item_codigo | texto | sim | Código do insumo/MO/equip referenciado |
| item_nome | texto | sim | Descrição (redundante, para legibilidade) |
| quantidade | número | sim | Rendimento / coeficiente |
| unidade | texto | sim | Unidade do rendimento |
| custo_unitario | número | não | Preço unitário no momento |
| custo_total | número | não | quantidade × custo_unitario |
| _fonte | texto | sim | Nome do arquivo origem |
| _aba_origem | texto | sim | Aba de onde veio |
| _linha_origem | número | sim | Linha no arquivo original |
| _formula_original | texto | não | Fórmula Excel original |

### 6. Encargos e BDI
| Coluna | Tipo | Obrigatório | Descrição |
|--------|------|-------------|-----------|
| codigo | texto | sim | Identificador (INSS, FGTS, AC, ML, etc.) |
| nome | texto | sim | Descrição do encargo/componente BDI |
| grupo | texto | sim | ENCARGO_SOCIAL / IMPOSTO / BDI_OVERHEAD / CUSTO_FINANCEIRO |
| aliquota | número | sim | Percentual (0.20 = 20%) |
| base_calculo | texto | não | Sobre o que incide (salario_base, custo_direto, etc.) |
| observacao | texto | não | Notas, referência legal |
| _fonte | texto | sim | Nome do arquivo origem |
| _aba_origem | texto | sim | Aba de onde veio |
| _linha_origem | número | sim | Linha no arquivo original |

## Workflow por Fonte

### Passo 1: Diagnóstico
Ler o arquivo inteiro. Para cada aba:
- Contar linhas com dados reais (ignorar headers vazios e formatação)
- Identificar colunas com dados
- Mapear: esta aba alimenta qual tabela-destino?
- Listar fórmulas encontradas (se relevante)
- Gerar relatório de diagnóstico usando `TEMPLATE_DOCUMENTACAO_ABAS.md` como modelo (uma seção por aba relevante)

### Passo 2: Extração
Para cada aba mapeada:
- Extrair dados para o formato da tabela-destino correspondente
- Aplicar normalização (unidades, texto, datas)
- Preencher colunas de auditoria (_fonte, _aba_origem, _linha_origem)
- Marcar _revisar = SIM onde necessário
- Salvar em intermediarios/EXTRACAO_{fonte}.xlsx

### Passo 3: Relatório
Gerar resumo:
- Quantos registros extraídos por tabela
- Quantos marcados para revisão
- Campos vazios relevantes (ex: insumo sem preço)
- Anomalias encontradas (preço negativo, rendimento > 100, etc.)

### Passo 4: Validação Humana
Conrado/Sandro revisam os itens marcados _revisar = SIM. Corrigem no Excel e salvam.

### Passo 5: Consolidação (só após todas as fontes extraídas)
Juntar todos EXTRACAO_*.xlsx num MASTER por tipo. Adicionar coluna _fonte para rastreabilidade. Identificar duplicatas (mesmo insumo em fontes diferentes).

## Fonte Atual: HOLLOS (ex-Planilha Pequenas Obras)

**Arquivo:** PLANILHA ORCAMENTOS - HOLLOS.xlsx | **Tamanho:** 5.1 MB | **Abas:** 35

Para o mapeamento completo de abas → tabelas-destino, prioridades, ordem de extração e a documentação de HOLLOS/MURILO, use a skill `extrair-fonte`.

## Referência: Compatibilidade Omie

O sistema ERP da Concept (Omie) possui template de importação de produtos (`Omie_Produtos_v1_9_5.xlsx`) com os seguintes campos relevantes que devem ser considerados na normalização:

### Mapeamento Omie → CostAI (tabela Insumos)
| Campo Omie | Campo CostAI | Notas |
|------------|-------------|-------|
| Código do Produto | codigo_fonte | Manter compatível para futuro import/export |
| Descrição do Produto | nome | UPPERCASE no CostAI |
| Código NCM | ncm | Extrair quando disponível nas fontes |
| Código EAN (GTIN) | (não mapeado no MVP) | Manter se disponível |
| Preço Unitário de Venda | preco_unitario | |
| Preço Unitário de Custo | preco_fabricante | |
| Unidade | unidade | Normalizar para padrão CostAI |
| Família de Produto | familia | Nível 1 hierarquia |
| Marca | fabricante | |
| Modelo | (coluna adicional se disponível) | |
| Peso Líquido (Kg) | (não mapeado no MVP) | Útil para logística futura |

### Omie_Produtos_Estrutura (BOM)
A aba Estrutura do Omie (Produto Pai → Produto Filho → Quantidade → Perda%) é a mesma lógica de **Composições + Itens da Composição** no CostAI. Manter códigos de produto compatíveis facilita eventual import de BOMs do Omie para composições do CostAI.

### Omie_Produtos_Kit
Kits com componentes e quantidades — outra forma de composição. Mesmo princípio: código do kit = composição, componentes = itens da composição.

### Implicação para a extração
- Ao normalizar `familia`, usar nomenclatura compatível com o que já existe no Omie da Concept
- Preservar NCM quando disponível (obrigatório no Omie para NFe)
- Preservar EAN/GTIN quando disponível
- Código do produto deve ser único e rastreável para futuro cruzamento com Omie

### Arquivo de referência
Localização: `fontes/Omie_Produtos_v1_9_5 (1).xlsx`


## Nota Crítica: Composições Paramétricas (Alimentação-industrial → Materiais)

A aba "Materiais - industrial" NÃO é fonte primária — é resultado de cálculos vindos da aba "Alimentação-industrial" via fórmulas. Documentação completa do fluxo, como extrair e o comparativo HOLLOS × MURILO estão na skill `extrair-fonte`. Spec completa do módulo (inputs, lógica de dimensionamento, BOM) em `specs/SPEC1_Dimensionador_Alimentadores.md`.
