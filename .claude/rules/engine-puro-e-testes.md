# Engine puro + testes obrigatórios

1. **Engine puro.** Todo cálculo vive em `engine/` — Python puro, sem Django, sem ORM,
   sem I/O. Recebe dados (dataclasses/dicts), devolve resultado. Testável isolado.
   Views e serializers só orquestram: buscam dados, chamam o engine, persistem.

2. **Teste obrigatório.** Engine sem teste pytest não mergeia. Casos de teste vêm dos
   exemplos validados pelo Sandro e dos valores da planilha HOLLOS.

3. **Golden test é o gate do MVP.** O orçamento de referência reproduzido no sistema
   deve bater com a HOLLOS: **R$ 216.188,04**. Enquanto não bater, o MVP não está pronto.
   Divergência item a item deve ser explicável (erro da planilha documentado ou bug nosso).
