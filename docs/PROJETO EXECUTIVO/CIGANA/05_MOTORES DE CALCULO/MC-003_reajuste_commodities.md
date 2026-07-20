---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, motores-calculo]
---

# MC-003 — Motor de Reajuste de Commodities

## O que é

Calcula reajuste de preço de insumos atrelados a commodities (cobre, aço, alumínio).
Absorve a aba "Formula Reajuste Cabos" da planilha HOLLOS. Extensível para outros materiais.

## Fórmula (cabos de cobre)

```
Preço_Reajustado = Pi + (ΔLMEf × US$f - ΔLMEi × US$i) × K / 1000
```

Onde:
- Pi = preço inicial do cabo (data-base da proposta)
- ΔLMEf = cotação LME do cobre na data final (US$/ton)
- ΔLMEi = cotação LME do cobre na data inicial (US$/ton)
- US$f = câmbio USD/BRL na data final
- US$i = câmbio USD/BRL na data inicial
- K = fator de conversão por tipo de cabo (kg cobre / km de cabo)

## Quando usar

- Propostas com prazo de validade > 30 dias
- Contratos de longo prazo com cláusula de reajuste
- Comparação de orçamentos em datas-base diferentes

## Implementação

Arquivo: `src/engines/commodity-adjustment.ts`

No MVP, os inputs (LME, câmbio) são manuais. Futuro: API de cotação automática.
O fator K é **atributo do insumo** no BD-1 (`materials.commodity`, `material_prices.commodity_factor`).
