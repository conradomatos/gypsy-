> **RASCUNHO** (Claude, 2026-07-19) — proposta a partir das decisões da sessão.
> A versão final destas regras será escrita pelo Conrado.

# Parâmetros — nada hardcoded

1. Alíquotas, encargos, impostos, fatores de correção, queda de tensão admissível,
   fator de sobra de cabo, horas improdutivas: **tudo é parâmetro no banco**, em dois
   níveis — global (empresa) + override por orçamento. Nunca constante no código.

2. **Exceção:** tabelas normativas (NBR 5410, NBR 14039, NBR 5419) são constantes
   versionadas no código (`engine/data/`). Mudam só quando a norma é revisada — não
   por tenant nem por orçamento.

3. **Não copiar fórmula da HOLLOS às cegas.** Dimensionamento vem da norma, não da
   planilha (decisão SPEC1 — fórmulas da planilha podem ter erros acumulados e ajustes
   manuais tipo `+280`). A HOLLOS é referência de comportamento e de valores esperados,
   não de implementação.
