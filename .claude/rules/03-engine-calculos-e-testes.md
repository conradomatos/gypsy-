# Engine, cálculos e testes

## Engine
- Cálculo vive num pacote de engine isolado do Django (estrutura em
  `padroes_de_codigo.md` — ainda PROPOSTO, não congelar caminho).
- Sem Django, sem ORM, sem HTTP, sem I/O nas funções de cálculo.
- Funções determinísticas.
- `Decimal` para valores monetários, nunca `float`; arredondamento explícito
  onde a norma/HOLLOS exigir.
- Engine recebe parâmetros como entrada — nunca os hardcoda (ver rule 04).
- Não copiar fórmula da HOLLOS às cegas: dimensionamento vem da norma; a HOLLOS
  é referência de comportamento e de valores esperados, não de implementação.

## Testes
- Cálculo crítico exige teste pytest. Engine sem teste não está concluído.
- Golden test é o gate do MVP: reproduzir o orçamento de referência batendo
  **R$ 216.188,04**; divergência item a item deve ser explicável.
- Testes verificam regras, não apenas cobertura.
- Mostrar comandos executados e resultados. Não inventar comandos enquanto não
  houver scaffold.
