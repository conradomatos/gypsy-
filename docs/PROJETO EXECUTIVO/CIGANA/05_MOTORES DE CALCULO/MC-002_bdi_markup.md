---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, motores-calculo]
---

# MC-002 — Motor de BDI / Formação de Preço

## O que é

Transforma custo direto em preço de venda aplicando encargos sobre faturamento.
Absorve as abas "Administração Central IND" e "Impostos-industrial" da planilha HOLLOS.
O bloco "Encargos sobre Faturamento" (42,53%) que se repete em 8 abas da planilha = uma chamada ao MC-2.

## Fórmula SINAPI/TCU

```
BDI = ((1 + AC + S + R + DF + L) / (1 - I)) - 1
```

Onde:
- AC = Administração Central (3%-8%)
- S = Seguro e Garantia (0,5%-2%)
- R = Risco/Contingência (0,5%-5%)
- DF = Despesas Financeiras (0,5%-2%)
- L = Lucro (5%-15%)
- I = Impostos (ISS + PIS + COFINS + IRPJ + CSLL)

## Cenários da Concept

| Cenário | Descrição |
|---------|-----------|
| Todo Fornecimento | Concept compra e fornece material. BDI sobre tudo |
| Faturamento Direto | Cliente compra material. BDI só sobre MO e serviços |

## Lucro diferenciado (prática Concept)

| Natureza | Lucro % |
|----------|---------|
| MO Direta | 15% |
| Materiais | 12% |
| Equipamentos | 15% |
| Terceiros | 15% |

## Bloco padrão Concept (HOLLOS)

| Item | % |
|------|---|
| ISS | 3,00 |
| PIS | 0,65 |
| COFINS | 3,00 |
| ADM Central | 10,00 |
| Lucro (MO) | 15,00 |
| IR | 4,80 |
| IR Adicional | 3,20 |
| CSLL | 2,88 |
| **Total encargos sobre faturamento** | **42,53%** |

## Implementação

Arquivo: `src/engines/bdi-markup.ts`

```typescript
interface BdiProfile {
  name: string;
  adminCentral: number;
  insurance: number;
  risk: number;
  financialExpenses: number;
  profit: { labor: number; materials: number; equipment: number; thirdParty: number };
  taxes: { iss: number; pis: number; cofins: number; irpj: number; irAdditional: number; csll: number };
}

function calculateBdi(profile: BdiProfile, costNature: 'labor' | 'materials' | 'equipment' | 'thirdParty'): number {
  const { adminCentral, insurance, risk, financialExpenses, profit, taxes } = profile;
  const profitRate = profit[costNature];
  const totalTax = taxes.iss + taxes.pis + taxes.cofins + taxes.irpj + taxes.irAdditional + taxes.csll;
  return ((1 + adminCentral + insurance + risk + financialExpenses + profitRate) / (1 - totalTax)) - 1;
}
```

## Dependências

- Parâmetros globais: perfil BDI default da empresa
- Parâmetros do projeto: override por orçamento (obra pública vs privada)
- MC-001: consome o custo/hora sem BDI e aplica markup
