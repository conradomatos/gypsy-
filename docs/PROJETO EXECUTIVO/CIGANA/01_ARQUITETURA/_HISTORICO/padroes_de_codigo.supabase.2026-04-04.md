> **STATUS: REVOGADO**
>
> - **Stack histórica:** Engines em TypeScript (src/engines) + cliente Supabase + RLS + ParametrosProvider (React context)
> - **Data da revogação:** 2026-07-19
> - **Decisão substituta:** `../registro_de_decisoes.md` — entrada de 2026-07-19
> - **Motivo:** convergência dos apps da Concept para **Django + DRF + PostgreSQL**; Supabase, Edge Functions, Deno, cliente Supabase e RLS-como-autorização foram abandonados.
> - **Documento vigente:** `../padroes_de_codigo.md`
>
> Este documento existe **apenas para auditoria e rastreabilidade**. Não orienta implementação.
> Decisões vigentes prevalecem sobre este histórico.

<!-- FIM DO CABECALHO DE HISTORICO -- CONTEUDO ORIGINAL PRESERVADO ABAIXO -->

---
tipo: referencia
status: ativo
area: gypsy
tags: [gypsy, arquitetura]
---

# Padrões de código — Gypsy

## Estrutura de pastas

```
src/
├── engines/              ← lógica pura, ZERO React, ZERO Supabase
│   ├── composicao-hh.ts           (MC-1)
│   ├── bdi-markup.ts              (MC-2)
│   ├── reajuste-commodities.ts    (MC-3)
│   ├── estimador-equipe.ts        (M-005)
│   ├── dimensionador/
│   │   ├── forca.ts               (NBR 5410 — bitola, corrente)
│   │   ├── infra.ts               (ocupação, enchimento)
│   │   ├── alimentadores.ts
│   │   ├── iluminacao.ts
│   │   ├── instrumentacao.ts
│   │   ├── pintura.ts
│   │   └── spda.ts
│   └── __tests__/                 ← testes obrigatórios
│       ├── composicao-hh.test.ts
│       ├── bdi-markup.test.ts
│       ├── forca.test.ts
│       └── golden.test.ts         ← validação contra planilha real
├── data/                 ← tabelas estáticas de normas e referências
│   ├── nbr5410/                   (capacidade corrente, queda tensão, agrupamento)
│   ├── nbr5419/                   (SPDA)
│   └── index.ts
├── types/                ← schemas centralizados
│   ├── motor.ts
│   ├── trecho.ts
│   ├── assembly.ts
│   ├── orcamento.ts
│   └── parametros.ts
├── hooks/                ← React hooks (wrappers dos engines)
├── pages/                ← UI (páginas)
├── components/           ← UI reutilizável
├── providers/            ← Context providers
│   └── ParametrosProvider.tsx
├── lib/                  ← utilitários (formatCurrency, etc)
└── integrations/         ← Supabase client, tipos gerados

```

> **Nota:** Tabelas de NBR (5410, 5419) ficam em `src/data/` como constantes TypeScript — são referências normativas estáticas. Catálogos de fabricantes (Siemens, WEG) ficam no banco de dados via `materials` + `material_prices` — são dados dinâmicos com preço e data-base.

## Regra #1: engines são funções puras

Um engine recebe dados e retorna resultado. Sem useState, sem useEffect, sem Supabase direto, sem import de React.

```typescript
// engines/composicao-hh.ts — CORRETO
export function calcularCustoHH(
  funcao: Funcao,
  parametros: ParametrosProjeto
): CustoHH {
  const salarioBase = funcao.valorMensal;
  const encargos = salarioBase * parametros.encargos.totalHorista;
  const alimentacao = parametros.alimentacao.cafe + parametros.alimentacao.almoco + parametros.alimentacao.jantar;
  // ... cálculo puro
  return { custoHoraSemBDI, custoHoraComBDI, decomposicao };
}
```

O hook é o wrapper que conecta engine ao React:

```typescript
// hooks/useComposicaoHH.ts
export function useComposicaoHH(funcaoId: string) {
  const { parametros } = useParametros();
  const { data: funcao } = useQuery(['funcao', funcaoId], ...);
  return useMemo(() => calcularCustoHH(funcao, parametros), [funcao, parametros]);
}
```

## Regra #2: testes obrigatórios nos engines

Cálculos críticos — se errar, o orçamento inteiro está errado. Vitest com casos do Sandro.

```typescript
// engines/__tests__/forca.test.ts
import { calcularBitola } from '../dimensionador/forca';

test('motor 50cv/380V/100m retorna bitola correta', () => {
  const resultado = calcularBitola({
    potencia: 50, // cv
    tensao: 380,  // V
    distancia: 100, // m
    fatorPotencia: 0.85,
    fatorServico: 1.15,
  });
  expect(resultado.bitolaFinal).toBe(35); // mm²
  expect(resultado.criterioDecisivo).toBe('queda_tensao');
});
```
## Regra #3: golden test contra planilha real

O orçamento da HOLLOS (R$ 216.188,04) é o benchmark. Rodar pelo CostAI com mesmos inputs, resultado tem que bater.

```typescript
// engines/__tests__/golden.test.ts
import { calcularOrcamentoCompleto } from '../orcamento-completo';
import { HOLLOS_INPUTS } from './fixtures/hollos-inputs';

test('orçamento HOLLOS reproduz valor da planilha', () => {
  const resultado = calcularOrcamentoCompleto(HOLLOS_INPUTS);
  expect(resultado.totalComImpostos).toBeCloseTo(216188.04, 0);
  expect(resultado.hxhTotal).toBeCloseTo(2377.84, 0);
  expect(resultado.valorHHMedio).toBeCloseTo(61.29, 0);
});
```

## Regra #4: parâmetros como context React

ParametrosProvider carrega uma vez, distribui via context. Engines recebem como argumento.

```typescript
// providers/ParametrosProvider.tsx
const ParametrosContext = createContext<Parametros>(null);

export function ParametrosProvider({ orcamentoId, children }) {
  const { data: globais } = useQuery(['parametros-globais'], fetchGlobais);
  const { data: projeto } = useQuery(['parametros-projeto', orcamentoId], fetchProjeto);

  // merge: projeto sobrescreve globais (defaults com override)
  const parametros = useMemo(() => mergeParametros(globais, projeto), [globais, projeto]);

  return <ParametrosContext.Provider value={parametros}>{children}</ParametrosContext.Provider>;
}

export const useParametros = () => useContext(ParametrosContext);
```

## Regra #5: tipos centralizados

```typescript
// types/parametros.ts
export interface ParametrosProjeto {
  encargos: PerfilEncargos;
  alimentacao: { cafe: number; almoco: number; jantar: number };
  horasImprodutivas: { percentual: number; deslocamento: number; dds: number; liberacao: number };
  localObra: { uf: string; distanciaCasaObra: number };
  faturamentoDireto: boolean;
  prazoSemanas: number;
  perfilCliente: string;
}
```
## Padrões herdados do PWC (mantidos)

### Página CRUD
```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { supabase } from '@/integrations/supabase/client';
import { toast } from 'sonner';
// shadcn/ui: Card, Table, Dialog, Select, Input, Button, Badge
```

### Navegação (ao adicionar módulo/página)
1. `Layout.tsx` → adicionar em `routeToArea`
2. `AppSidebar.tsx` → adicionar em `areaNavItems`
3. `App.tsx` → registrar `<Route>`

### Supabase (ao criar tabelas)
- RLS habilitado + policies CRUD para `authenticated`
- Trigger `update_updated_at_column` em todas as tabelas
- Campos padrão: `id` (UUID), `created_at`, `updated_at`, `created_by` (FK auth.users)
- Textos em PT-BR

### Formulários
- react-hook-form + zod para validação
- Toast de sucesso/erro via sonner
- NUNCA usar `SelectItem value=""` (causa React crash)

### RLS Policies
```sql
CREATE POLICY "nome_policy" ON tabela
  FOR SELECT TO authenticated
  USING (true); -- MVP single-user, restringir depois
```

## Resumo: melhorias vs PWC

| PWC (atual) | Gypsy (melhorado) |
|---|---|
| Cálculo misturado com UI | `src/engines/` puro, sem React |
| Zero testes | Vitest nos engines + golden tests |
| Tipos espalhados | `src/types/` centralizado |
| Parâmetros buscados ad hoc | `ParametrosProvider` context |
| Sem validação de regressão | Golden test contra planilha real |
