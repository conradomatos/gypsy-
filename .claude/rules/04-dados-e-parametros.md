# Dados e parâmetros

## Parâmetros
- Alíquotas, encargos, impostos, fatores de correção, horas improdutivas etc.:
  parâmetro no banco, em dois níveis — global (empresa) + override por orçamento.
  Nunca constante no código.
- Exceção: tabelas normativas (NBR 5410/14039/5419) são constantes versionadas
  em estrutura própria do engine (local a fixar no SP do engine — hoje PROPOSTO).

## Orçamento e derivação
- Revisão de orçamento é snapshot imutável.
- Totais são derivados (calculados), nunca digitados.

## Rastreabilidade
- Todo número carrega fonte, data-base, flag de imposto e revisão quando aplicável.
- Origem da destilação: colunas `_fonte`, `_aba_origem`, `_linha_origem`,
  `_confianca` alimentam o seed.
- Nunca preencher com estimativa um dado que não existe na fonte — campo vazio é
  informação; número inventado é bug.

## Schema e fontes
- Schema ainda NÃO aprovado. Não criar DBML nem models fora do SP responsável (SP-04).
- Planilhas-fonte (`destilacao/fontes/`) são read-only — nunca sobrescrever;
  ficam fora do git.
